# Copyright 2018 The KaiJIN Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
r"""https://github.com/lukemelas/EfficientNet-PyTorch
"""
import re
import math
import collections
from functools import partial
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils import model_zoo
import tw

# Parameters for the entire model (stem, all blocks, and head)
GlobalParams = collections.namedtuple('GlobalParams', [
    'batch_norm_momentum', 'batch_norm_epsilon', 'dropout_rate',
    'num_classes', 'width_coefficient', 'depth_coefficient',
    'depth_divisor', 'min_depth', 'drop_connect_rate', 'image_size'])

# Parameters for an individual model block
BlockArgs = collections.namedtuple('BlockArgs', [
    'kernel_size', 'num_repeat', 'input_filters', 'output_filters',
    'expand_ratio', 'id_skip', 'stride', 'se_ratio'])

# Change namedtuple defaults
GlobalParams.__new__.__defaults__ = (None,) * len(GlobalParams._fields)
BlockArgs.__new__.__defaults__ = (None,) * len(BlockArgs._fields)


def round_filters(filters, global_params):
  """ Calculate and round number of filters based on depth multiplier. """
  multiplier = global_params.width_coefficient
  if not multiplier:
    return filters
  divisor = global_params.depth_divisor
  min_depth = global_params.min_depth
  filters *= multiplier
  min_depth = min_depth or divisor
  new_filters = max(min_depth, int(filters + divisor / 2) // divisor * divisor)
  if new_filters < 0.9 * filters:  # prevent rounding by more than 10%
    new_filters += divisor
  return int(new_filters)


def round_repeats(repeats, global_params):
  """ Round number of filters based on depth multiplier. """
  multiplier = global_params.depth_coefficient
  if not multiplier:
    return repeats
  return int(math.ceil(multiplier * repeats))


def drop_connect(inputs, p, training):
  """ Drop connect. """
  if not training:
    return inputs
  batch_size = inputs.shape[0]
  keep_prob = 1 - p
  random_tensor = keep_prob
  random_tensor += torch.rand([batch_size, 1, 1, 1],
                              dtype=inputs.dtype, device=inputs.device)
  binary_tensor = torch.floor(random_tensor)
  output = inputs / keep_prob * binary_tensor
  return output


def get_same_padding_conv2d(image_size=None):
  """ Chooses static padding if you have specified an image size, and dynamic padding otherwise.
      Static padding is necessary for ONNX exporting of models. """
  if image_size is None:
    return tw.nn.Conv2dDynamicSamePadding
  else:
    return partial(tw.nn.Conv2dStaticSamePadding, image_size=image_size)


def efficientnet_params(model_name):
  """ Map EfficientNet model name to parameter coefficients. """
  params_dict = {
      # Coefficients:   width,depth,res,dropout
      'efficientnet-b0': (1.0, 1.0, 224, 0.2),
      'efficientnet-b1': (1.0, 1.1, 240, 0.2),
      'efficientnet-b2': (1.1, 1.2, 260, 0.3),
      'efficientnet-b3': (1.2, 1.4, 300, 0.3),
      'efficientnet-b4': (1.4, 1.8, 380, 0.4),
      'efficientnet-b5': (1.6, 2.2, 456, 0.4),
      'efficientnet-b6': (1.8, 2.6, 528, 0.5),
      'efficientnet-b7': (2.0, 3.1, 600, 0.5),
  }
  return params_dict[model_name]


class BlockDecoder(object):
  """ Block Decoder for readability, straight from the official TensorFlow repository """

  @staticmethod
  def _decode_block_string(block_string):
    """ Gets a block through a string notation of arguments. """
    assert isinstance(block_string, str)

    ops = block_string.split('_')
    options = {}
    for op in ops:
      splits = re.split(r'(\d.*)', op)
      if len(splits) >= 2:
        key, value = splits[:2]
        options[key] = value

    # Check stride
    assert (('s' in options and len(options['s']) == 1) or
            (len(options['s']) == 2 and options['s'][0] == options['s'][1]))

    return BlockArgs(
        kernel_size=int(options['k']),
        num_repeat=int(options['r']),
        input_filters=int(options['i']),
        output_filters=int(options['o']),
        expand_ratio=int(options['e']),
        id_skip=('noskip' not in block_string),
        se_ratio=float(options['se']) if 'se' in options else None,
        stride=[int(options['s'][0])])

  @staticmethod
  def _encode_block_string(block):
    """Encodes a block to a string."""
    args = [
        'r%d' % block.num_repeat,
        'k%d' % block.kernel_size,
        's%d%d' % (block.strides[0], block.strides[1]),
        'e%s' % block.expand_ratio,
        'i%d' % block.input_filters,
        'o%d' % block.output_filters
    ]
    if 0 < block.se_ratio <= 1:
      args.append('se%s' % block.se_ratio)
    if block.id_skip is False:
      args.append('noskip')
    return '_'.join(args)

  @staticmethod
  def decode(string_list):
    """
    Decodes a list of string notations to specify blocks inside the network.

    :param string_list: a list of strings, each string is a notation of block
    :return: a list of BlockArgs namedtuples of block args
    """
    assert isinstance(string_list, list)
    blocks_args = []
    for block_string in string_list:
      blocks_args.append(BlockDecoder._decode_block_string(block_string))
    return blocks_args

  @staticmethod
  def encode(blocks_args):
    """
    Encodes a list of BlockArgs to a list of strings.

    :param blocks_args: a list of BlockArgs namedtuples of block args
    :return: a list of strings, each string is a notation of block
    """
    block_strings = []
    for block in blocks_args:
      block_strings.append(BlockDecoder._encode_block_string(block))
    return block_strings


class MBConvBlock(nn.Module):
  """
  Mobile Inverted Residual Bottleneck Block

  Args:
      block_args (namedtuple): BlockArgs, see above
      global_params (namedtuple): GlobalParam, see above

  Attributes:
      has_se (bool): Whether the block contains a Squeeze and Excitation layer.
  """

  def __init__(self, block_args, global_params):
    super().__init__()
    self._block_args = block_args
    self._bn_mom = 1 - global_params.batch_norm_momentum
    self._bn_eps = global_params.batch_norm_epsilon
    self.has_se = (self._block_args.se_ratio is not None) and (
        0 < self._block_args.se_ratio <= 1)
    self.id_skip = block_args.id_skip  # skip connection and drop connect

    # Get static or dynamic convolution depending on image size
    Conv2d = get_same_padding_conv2d(image_size=global_params.image_size)

    # Expansion phase
    inp = self._block_args.input_filters  # number of input channels
    oup = self._block_args.input_filters * \
        self._block_args.expand_ratio  # number of output channels
    if self._block_args.expand_ratio != 1:
      self._expand_conv = Conv2d(
          in_channels=inp, out_channels=oup, kernel_size=1, bias=False)
      self._bn0 = nn.BatchNorm2d(
          num_features=oup, momentum=self._bn_mom, eps=self._bn_eps)

    # Depthwise convolution phase
    k = self._block_args.kernel_size
    s = self._block_args.stride
    self._depthwise_conv = Conv2d(
        in_channels=oup, out_channels=oup, groups=oup,  # groups makes it depthwise
        kernel_size=k, stride=s, bias=False)
    self._bn1 = nn.BatchNorm2d(
        num_features=oup, momentum=self._bn_mom, eps=self._bn_eps)

    # Squeeze and Excitation layer, if desired
    if self.has_se:
      num_squeezed_channels = max(
          1, int(self._block_args.input_filters * self._block_args.se_ratio))
      self._se_reduce = Conv2d(
          in_channels=oup, out_channels=num_squeezed_channels, kernel_size=1)
      self._se_expand = Conv2d(
          in_channels=num_squeezed_channels, out_channels=oup, kernel_size=1)

    # Output phase
    final_oup = self._block_args.output_filters
    self._project_conv = Conv2d(
        in_channels=oup, out_channels=final_oup, kernel_size=1, bias=False)
    self._bn2 = nn.BatchNorm2d(
        num_features=final_oup, momentum=self._bn_mom, eps=self._bn_eps)
    self._swish = tw.nn.Swish()

  def forward(self, inputs, drop_connect_rate=None):
    """
    :param inputs: input tensor
    :param drop_connect_rate: drop connect rate (float, between 0 and 1)
    :return: output of block
    """

    # Expansion and Depthwise Convolution
    x = inputs
    if self._block_args.expand_ratio != 1:
      x = self._swish(self._bn0(self._expand_conv(inputs)))
    x = self._swish(self._bn1(self._depthwise_conv(x)))

    # Squeeze and Excitation
    if self.has_se:
      x_squeezed = F.adaptive_avg_pool2d(x, 1)
      x_squeezed = self._se_expand(self._swish(self._se_reduce(x_squeezed)))
      x = torch.sigmoid(x_squeezed) * x

    x = self._bn2(self._project_conv(x))

    # Skip connection and drop connect
    input_filters, output_filters = self._block_args.input_filters, self._block_args.output_filters
    if self.id_skip and self._block_args.stride == 1 and input_filters == output_filters:
      if drop_connect_rate:
        x = drop_connect(x, p=drop_connect_rate, training=self.training)
      x = x + inputs  # skip connection
    return x

  def set_swish(self, memory_efficient=True):
    """Sets swish function as memory efficient (for training) or standard (for export)"""
    self._swish = tw.nn.Swish()


class EfficientNet(nn.Module):
  """
  An EfficientNet model. Most easily loaded with the .from_name or .from_pretrained methods

  Args:
      blocks_args (list): A list of BlockArgs to construct blocks
      global_params (namedtuple): A set of GlobalParams shared between blocks

  Example:
      model = EfficientNet.from_pretrained('efficientnet-b0')

  """

  def __init__(self, blocks_args=None, global_params=None):
    super().__init__()
    assert isinstance(blocks_args, list), 'blocks_args should be a list'
    assert len(blocks_args) > 0, 'block args must be greater than 0'
    self._global_params = global_params
    self._blocks_args = blocks_args

    # Get static or dynamic convolution depending on image size
    Conv2d = get_same_padding_conv2d(image_size=global_params.image_size)

    # Batch norm parameters
    bn_mom = 1 - self._global_params.batch_norm_momentum
    bn_eps = self._global_params.batch_norm_epsilon

    # Stem
    in_channels = 3  # rgb
    # number of output channels
    out_channels = round_filters(32, self._global_params)
    self._conv_stem = Conv2d(in_channels, out_channels,
                             kernel_size=3, stride=2, bias=False)
    self._bn0 = nn.BatchNorm2d(
        num_features=out_channels, momentum=bn_mom, eps=bn_eps)

    # Build blocks
    self._blocks = nn.ModuleList([])
    for block_args in self._blocks_args:

      # Update block input and output filters based on depth multiplier.
      block_args = block_args._replace(
          input_filters=round_filters(
              block_args.input_filters, self._global_params),
          output_filters=round_filters(
              block_args.output_filters, self._global_params),
          num_repeat=round_repeats(block_args.num_repeat, self._global_params)
      )

      # The first block needs to take care of stride and filter size increase.
      self._blocks.append(MBConvBlock(block_args, self._global_params))
      if block_args.num_repeat > 1:
        block_args = block_args._replace(
            input_filters=block_args.output_filters, stride=1)
      for _ in range(block_args.num_repeat - 1):
        self._blocks.append(MBConvBlock(block_args, self._global_params))

    # Head
    in_channels = block_args.output_filters  # output of final block
    out_channels = round_filters(1280, self._global_params)
    self._conv_head = Conv2d(in_channels, out_channels,
                             kernel_size=1, bias=False)
    self._bn1 = nn.BatchNorm2d(
        num_features=out_channels, momentum=bn_mom, eps=bn_eps)

    # Final linear layer
    self._avg_pooling = nn.AdaptiveAvgPool2d(1)
    self._dropout = nn.Dropout(self._global_params.dropout_rate)
    self._fc = nn.Linear(out_channels, self._global_params.num_classes)
    self._swish = tw.nn.Swish()

  def set_swish(self, memory_efficient=True):
    """Sets swish function as memory efficient (for training) or standard (for export)"""
    self._swish = tw.nn.Swish()
    for block in self._blocks:
      block.set_swish(memory_efficient)

  def extract_features(self, inputs):
    """ Returns output of the final convolution layer """

    # Stem
    x = self._swish(self._bn0(self._conv_stem(inputs)))

    # Blocks
    for idx, block in enumerate(self._blocks):
      drop_connect_rate = self._global_params.drop_connect_rate
      if drop_connect_rate:
        drop_connect_rate *= float(idx) / len(self._blocks)
      x = block(x, drop_connect_rate=drop_connect_rate)

    # Head
    x = self._swish(self._bn1(self._conv_head(x)))

    return x

  def forward(self, inputs):
    """ Calls extract_features to extract features, applies final linear layer, and returns logits. """
    bs = inputs.size(0)
    # Convolution layers
    x = self.extract_features(inputs)

    # Pooling and final linear layer
    x = self._avg_pooling(x)
    x = x.view(bs, -1)
    x = self._dropout(x)
    x = self._fc(x)
    return x

  @classmethod
  def from_name(cls, model_name, override_params=None):
    cls._check_model_name_is_valid(model_name)
    blocks_args, global_params = get_model_params(model_name, override_params)
    return cls(blocks_args, global_params)

  @classmethod
  def from_pretrained(cls, model_name, num_classes=1000, in_channels=3):
    model = cls.from_name(model_name, override_params={
                          'num_classes': num_classes})
    load_pretrained_weights(model, model_name, load_fc=(num_classes == 1000))
    if in_channels != 3:
      Conv2d = get_same_padding_conv2d(
          image_size=model._global_params.image_size)
      out_channels = round_filters(32, model._global_params)
      model._conv_stem = Conv2d(
          in_channels, out_channels, kernel_size=3, stride=2, bias=False)
    return model

  # @classmethod
  # def from_pretrained(cls, model_name, num_classes=1000):
  #   model = cls.from_name(model_name, override_params={
  #                         'num_classes': num_classes})
  #   load_pretrained_weights(model, model_name, load_fc=(num_classes == 1000))

  #   return model

  @classmethod
  def get_image_size(cls, model_name):
    cls._check_model_name_is_valid(model_name)
    _, _, res, _ = efficientnet_params(model_name)
    return res

  @classmethod
  def _check_model_name_is_valid(cls, model_name, also_need_pretrained_weights=False):
    """ Validates model name. None that pretrained weights are only available for
    the first four models (efficientnet-b{i} for i in 0,1,2,3) at the moment. """
    num_models = 4 if also_need_pretrained_weights else 8
    valid_models = ['efficientnet-b'+str(i) for i in range(num_models)]
    if model_name not in valid_models:
      raise ValueError('model_name should be one of: ' +
                       ', '.join(valid_models))


def efficientnet(width_coefficient=None, depth_coefficient=None, dropout_rate=0.2,
                 drop_connect_rate=0.2, image_size=None, num_classes=1000):
  """ Creates a efficientnet model. """

  blocks_args = [
      'r1_k3_s11_e1_i32_o16_se0.25', 'r2_k3_s22_e6_i16_o24_se0.25',
      'r2_k5_s22_e6_i24_o40_se0.25', 'r3_k3_s22_e6_i40_o80_se0.25',
      'r3_k5_s11_e6_i80_o112_se0.25', 'r4_k5_s22_e6_i112_o192_se0.25',
      'r1_k3_s11_e6_i192_o320_se0.25',
  ]
  blocks_args = BlockDecoder.decode(blocks_args)

  global_params = GlobalParams(
      batch_norm_momentum=0.99,
      batch_norm_epsilon=1e-3,
      dropout_rate=dropout_rate,
      drop_connect_rate=drop_connect_rate,
      num_classes=num_classes,
      width_coefficient=width_coefficient,
      depth_coefficient=depth_coefficient,
      depth_divisor=8,
      min_depth=None,
      image_size=image_size)

  return blocks_args, global_params


def get_model_params(model_name, override_params):
  """ Get the block args and global params for a given model """
  if model_name.startswith('efficientnet'):
    w, d, s, p = efficientnet_params(model_name)
    # note: all models have drop connect rate = 0.2
    blocks_args, global_params = efficientnet(
        width_coefficient=w, depth_coefficient=d, dropout_rate=p, image_size=s)
  else:
    raise NotImplementedError('model name is not pre-defined: %s' % model_name)
  if override_params:
    # ValueError will be raised here if override_params has fields not included in global_params.
    global_params = global_params._replace(**override_params)
  return blocks_args, global_params


url_map = {
    'efficientnet-b0': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b0-355c32eb.pth',
    'efficientnet-b1': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b1-f1951068.pth',
    'efficientnet-b2': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b2-8bb594d6.pth',
    'efficientnet-b3': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b3-5fb5a3c3.pth',
    'efficientnet-b4': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b4-6ed6700e.pth',
    'efficientnet-b5': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b5-b6417697.pth',
    'efficientnet-b6': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b6-c76e70fd.pth',
    'efficientnet-b7': 'http://storage.googleapis.com/public-models/efficientnet/efficientnet-b7-dcc49843.pth',
}


def efficientnet_b0():
  return EfficientNet.from_name('efficientnet-b0')


def efficientnet_b1():
  return EfficientNet.from_name('efficientnet-b1')


def efficientnet_b2():
  return EfficientNet.from_name('efficientnet-b2')


def efficientnet_b3():
  return EfficientNet.from_name('efficientnet-b3')


def efficientnet_b4():
  return EfficientNet.from_name('efficientnet-b4')


def efficientnet_b5():
  return EfficientNet.from_name('efficientnet-b5')


def efficientnet_b6():
  return EfficientNet.from_name('efficientnet-b6')


def efficientnet_b7():
  return EfficientNet.from_name('efficientnet-b7')


def load_pretrained_weights(model, model_name, load_fc=True):
  """ Loads pretrained weights, and downloads if loading for the first time. """
  state_dict = model_zoo.load_url(url_map[model_name])
  if load_fc:
    model.load_state_dict(state_dict)
  else:
    state_dict.pop('_fc.weight')
    state_dict.pop('_fc.bias')
    res = model.load_state_dict(state_dict, strict=False)
    assert set(res.missing_keys) == set(
        ['_fc.weight', '_fc.bias']), 'issue loading pretrained weights'
  print('Loaded pretrained weights for {}'.format(model_name))
