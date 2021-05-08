# Copyright 2020 The KaiJIN Authors. All Rights Reserved.
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
# =============================================================================
r"""From https://github.com/Tramac/awesome-semantic-segmentation-pytorch.git
  2080ti: 15.24 ms, 65.58 fps
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class ENet(nn.Module):
  """Efficient Neural Network"""

  def __init__(self, num_classes, norm_layer=nn.BatchNorm2d, **kwargs):
    super(ENet, self).__init__()
    self.initial = InitialBlock(13, **kwargs)

    self.bottleneck1_0 = Bottleneck(16, 16, 64, downsampling=True, **kwargs)
    self.bottleneck1_1 = Bottleneck(64, 16, 64, **kwargs)
    self.bottleneck1_2 = Bottleneck(64, 16, 64, **kwargs)
    self.bottleneck1_3 = Bottleneck(64, 16, 64, **kwargs)
    self.bottleneck1_4 = Bottleneck(64, 16, 64, **kwargs)

    self.bottleneck2_0 = Bottleneck(64, 32, 128, downsampling=True, **kwargs)
    self.bottleneck2_1 = Bottleneck(128, 32, 128, **kwargs)
    self.bottleneck2_2 = Bottleneck(128, 32, 128, dilation=2, **kwargs)
    self.bottleneck2_3 = Bottleneck(128, 32, 128, asymmetric=True, **kwargs)
    self.bottleneck2_4 = Bottleneck(128, 32, 128, dilation=4, **kwargs)
    self.bottleneck2_5 = Bottleneck(128, 32, 128, **kwargs)
    self.bottleneck2_6 = Bottleneck(128, 32, 128, dilation=8, **kwargs)
    self.bottleneck2_7 = Bottleneck(128, 32, 128, asymmetric=True, **kwargs)
    self.bottleneck2_8 = Bottleneck(128, 32, 128, dilation=16, **kwargs)

    self.bottleneck3_1 = Bottleneck(128, 32, 128, **kwargs)
    self.bottleneck3_2 = Bottleneck(128, 32, 128, dilation=2, **kwargs)
    self.bottleneck3_3 = Bottleneck(128, 32, 128, asymmetric=True, **kwargs)
    self.bottleneck3_4 = Bottleneck(128, 32, 128, dilation=4, **kwargs)
    self.bottleneck3_5 = Bottleneck(128, 32, 128, **kwargs)
    self.bottleneck3_6 = Bottleneck(128, 32, 128, dilation=8, **kwargs)
    self.bottleneck3_7 = Bottleneck(128, 32, 128, asymmetric=True, **kwargs)
    self.bottleneck3_8 = Bottleneck(128, 32, 128, dilation=16, **kwargs)

    self.bottleneck4_0 = UpsamplingBottleneck(128, 16, 64, **kwargs)
    self.bottleneck4_1 = Bottleneck(64, 16, 64, **kwargs)
    self.bottleneck4_2 = Bottleneck(64, 16, 64, **kwargs)

    self.bottleneck5_0 = UpsamplingBottleneck(64, 4, 16, **kwargs)
    self.bottleneck5_1 = Bottleneck(16, 4, 16, **kwargs)

    self.fullconv = nn.ConvTranspose2d(16, num_classes, 2, 2, bias=False)

  def forward(self, x):
    # init
    x = self.initial(x)

    # stage 1
    x, max_indices1 = self.bottleneck1_0(x)
    x = self.bottleneck1_1(x)
    x = self.bottleneck1_2(x)
    x = self.bottleneck1_3(x)
    x = self.bottleneck1_4(x)

    # stage 2
    x, max_indices2 = self.bottleneck2_0(x)
    x = self.bottleneck2_1(x)
    x = self.bottleneck2_2(x)
    x = self.bottleneck2_3(x)
    x = self.bottleneck2_4(x)
    x = self.bottleneck2_5(x)
    x = self.bottleneck2_6(x)
    x = self.bottleneck2_7(x)
    x = self.bottleneck2_8(x)

    # stage 3
    x = self.bottleneck3_1(x)
    x = self.bottleneck3_2(x)
    x = self.bottleneck3_3(x)
    x = self.bottleneck3_4(x)
    x = self.bottleneck3_6(x)
    x = self.bottleneck3_7(x)
    x = self.bottleneck3_8(x)

    # stage 4
    x = self.bottleneck4_0(x, max_indices2)
    x = self.bottleneck4_1(x)
    x = self.bottleneck4_2(x)

    # stage 5
    x = self.bottleneck5_0(x, max_indices1)
    x = self.bottleneck5_1(x)

    # out
    x = self.fullconv(x)
    return x


class InitialBlock(nn.Module):
  """ENet initial block"""

  def __init__(self, out_channels, norm_layer=nn.BatchNorm2d, **kwargs):
    super(InitialBlock, self).__init__()
    self.conv = nn.Conv2d(3, out_channels, 3, 2, 1, bias=False)
    self.maxpool = nn.MaxPool2d(2, 2)
    self.bn = norm_layer(out_channels + 3)
    self.act = nn.PReLU()

  def forward(self, x):
    x_conv = self.conv(x)
    x_pool = self.maxpool(x)
    x = torch.cat([x_conv, x_pool], dim=1)
    x = self.bn(x)
    x = self.act(x)
    return x


class Bottleneck(nn.Module):
  """Bottlenecks include regular, asymmetric, downsampling, dilated"""

  def __init__(self, in_channels, inter_channels, out_channels, dilation=1, asymmetric=False,
               downsampling=False, norm_layer=nn.BatchNorm2d, **kwargs):
    super(Bottleneck, self).__init__()
    self.downsamping = downsampling
    if downsampling:
      self.maxpool = nn.MaxPool2d(2, 2, return_indices=True)
      self.conv_down = nn.Sequential(
          nn.Conv2d(in_channels, out_channels, 1, bias=False),
          norm_layer(out_channels)
      )

    self.conv1 = nn.Sequential(
        nn.Conv2d(in_channels, inter_channels, 1, bias=False),
        norm_layer(inter_channels),
        nn.PReLU()
    )

    if downsampling:
      self.conv2 = nn.Sequential(
          nn.Conv2d(inter_channels, inter_channels, 2, stride=2, bias=False),
          norm_layer(inter_channels),
          nn.PReLU()
      )
    else:
      if asymmetric:
        self.conv2 = nn.Sequential(
            nn.Conv2d(inter_channels, inter_channels,
                      (5, 1), padding=(2, 0), bias=False),
            nn.Conv2d(inter_channels, inter_channels,
                      (1, 5), padding=(0, 2), bias=False),
            norm_layer(inter_channels),
            nn.PReLU()
        )
      else:
        self.conv2 = nn.Sequential(
            nn.Conv2d(inter_channels, inter_channels, 3,
                      dilation=dilation, padding=dilation, bias=False),
            norm_layer(inter_channels),
            nn.PReLU()
        )
    self.conv3 = nn.Sequential(
        nn.Conv2d(inter_channels, out_channels, 1, bias=False),
        norm_layer(out_channels),
        nn.Dropout2d(0.1)
    )
    self.act = nn.PReLU()

  def forward(self, x):
    identity = x
    if self.downsamping:
      identity, max_indices = self.maxpool(identity)
      identity = self.conv_down(identity)

    out = self.conv1(x)
    out = self.conv2(out)
    out = self.conv3(out)
    out = self.act(out + identity)

    if self.downsamping:
      return out, max_indices
    else:
      return out


class UpsamplingBottleneck(nn.Module):
  """upsampling Block"""

  def __init__(self, in_channels, inter_channels, out_channels, norm_layer=nn.BatchNorm2d, **kwargs):
    super(UpsamplingBottleneck, self).__init__()
    self.conv = nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 1, bias=False),
        norm_layer(out_channels)
    )
    self.upsampling = nn.MaxUnpool2d(2)

    self.block = nn.Sequential(
        nn.Conv2d(in_channels, inter_channels, 1, bias=False),
        norm_layer(inter_channels),
        nn.PReLU(),
        nn.ConvTranspose2d(inter_channels, inter_channels, 2, 2, bias=False),
        norm_layer(inter_channels),
        nn.PReLU(),
        nn.Conv2d(inter_channels, out_channels, 1, bias=False),
        norm_layer(out_channels),
        nn.Dropout2d(0.1)
    )
    self.act = nn.PReLU()

  def forward(self, x, max_indices):
    out_up = self.conv(x)
    out_up = self.upsampling(out_up, max_indices)

    out_ext = self.block(x)
    out = self.act(out_up + out_ext)
    return out
