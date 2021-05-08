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
"""VGG form torchvision.model """
import torch
import torch.nn as nn


class VGG(nn.Module):

  def __init__(self, features, num_classes=1000, init_weights=True):
    super(VGG, self).__init__()
    self.features = features
    self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
    self.classifier = nn.Sequential(
        nn.Linear(512 * 7 * 7, 4096),
        nn.ReLU(),
        nn.Dropout(),
        nn.Linear(4096, 4096),
        nn.ReLU(),
        nn.Dropout(),
        nn.Linear(4096, num_classes),
    )
    if init_weights:
      self._initialize_weights()

  def forward(self, x):
    x = self.features(x)
    x = self.avgpool(x)
    x = torch.flatten(x, 1)
    x = self.classifier(x)
    return x

  def _initialize_weights(self):
    for m in self.modules():
      if isinstance(m, nn.Conv2d):
        nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
        if m.bias is not None:
          nn.init.constant_(m.bias, 0)
      elif isinstance(m, nn.BatchNorm2d):
        nn.init.constant_(m.weight, 1)
        nn.init.constant_(m.bias, 0)
      elif isinstance(m, nn.Linear):
        nn.init.normal_(m.weight, 0, 0.01)
        nn.init.constant_(m.bias, 0)


def make_layers(cfg, batch_norm=False, **kwargs):
  layers = []
  if 'input_channels' in kwargs:
    in_channels = kwargs['input_channels']
  else:
    in_channels = 3
  for v in cfg:
    if v == 'M':
      layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
    else:
      conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
      if batch_norm:
        layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
      else:
        layers += [conv2d, nn.ReLU(inplace=True)]
      in_channels = v
  return nn.Sequential(*layers)


cfgs = {
    'A': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'B': [64, 64, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'D': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],
    'E': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M'],
}


def _vgg(arch, cfg, batch_norm, **kwargs):
  return VGG(make_layers(cfgs[cfg], batch_norm=batch_norm, **kwargs), **kwargs)


def vgg11(**kwargs):
  r"""VGG 11-layer model (configuration "A") from
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg11', 'A', False, **kwargs)


def vgg11_bn(**kwargs):
  r"""VGG 11-layer model (configuration "A") with batch normalization
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg11_bn', 'A', True, **kwargs)


def vgg13(**kwargs):
  r"""VGG 13-layer model (configuration "B")
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg13', 'B', False, **kwargs)


def vgg13_bn(**kwargs):
  r"""VGG 13-layer model (configuration "B") with batch normalization
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg13_bn', 'B', True, **kwargs)


def vgg16(**kwargs):
  r"""VGG 16-layer model (configuration "D")
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg16', 'D', False, **kwargs)


def vgg16_bn(**kwargs):
  r"""VGG 16-layer model (configuration "D") with batch normalization
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg16_bn', 'D', True, **kwargs)


def vgg19(**kwargs):
  r"""VGG 19-layer model (configuration "E")
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg19', 'E', False, **kwargs)


def vgg19_bn(**kwargs):
  r"""VGG 19-layer model (configuration 'E') with batch normalization
  `"Very Deep Convolutional Networks For Large-Scale Image Recognition" <https://arxiv.org/pdf/1409.1556.pdf>`_

  Args:
      pretrained (bool): If True, returns a model pre-trained on ImageNet
      progress (bool): If True, displays a progress bar of the download to stderr
  """
  return _vgg('vgg19_bn', 'E', True, **kwargs)
