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
import torch
import torch.nn as nn
import torch.nn.functional as F
from .utils import _ResnetBackbone


class DANet(nn.Module):
  r"""Pyramid Scene Parsing Network

  Reference:
      Jun Fu, Jing Liu, Haijie Tian, Yong Li, Yongjun Bao, Zhiwei Fang,and Hanqing Lu.
      "Dual Attention Network for Scene Segmentation." *CVPR*, 2019
  """

  def __init__(self, num_classes, arch='resnet50', **kwargs):
    super(DANet, self).__init__()
    self.backbone = _ResnetBackbone(arch, **kwargs)
    self.head = _DAHead(2048, num_classes, **kwargs)

    self.__setattr__('exclusive', ['head'])

  def forward(self, x):
    size = x.size()[2:]
    _, _, c3, c4 = self.backbone.forward(x)
    outputs = []
    x = self.head(c4)
    x0 = F.interpolate(x[0], size, mode='bilinear', align_corners=True)
    outputs.append(x0)
    return outputs


class _PositionAttentionModule(nn.Module):
  """ Position attention module"""

  def __init__(self, in_channels, **kwargs):
    super(_PositionAttentionModule, self).__init__()
    self.conv_b = nn.Conv2d(in_channels, in_channels // 8, 1)
    self.conv_c = nn.Conv2d(in_channels, in_channels // 8, 1)
    self.conv_d = nn.Conv2d(in_channels, in_channels, 1)
    self.alpha = nn.Parameter(torch.zeros(1))
    self.softmax = nn.Softmax(dim=-1)

  def forward(self, x):
    batch_size, _, height, width = x.size()
    feat_b = self.conv_b(x).view(
        batch_size, -1, height * width).permute(0, 2, 1)
    feat_c = self.conv_c(x).view(batch_size, -1, height * width)
    attention_s = self.softmax(torch.bmm(feat_b, feat_c))
    feat_d = self.conv_d(x).view(batch_size, -1, height * width)
    feat_e = torch.bmm(feat_d, attention_s.permute(
        0, 2, 1)).view(batch_size, -1, height, width)
    out = self.alpha * feat_e + x

    return out


class _ChannelAttentionModule(nn.Module):
  """Channel attention module"""

  def __init__(self, **kwargs):
    super(_ChannelAttentionModule, self).__init__()
    self.beta = nn.Parameter(torch.zeros(1))
    self.softmax = nn.Softmax(dim=-1)

  def forward(self, x):
    batch_size, _, height, width = x.size()
    feat_a = x.view(batch_size, -1, height * width)
    feat_a_transpose = x.view(batch_size, -1, height * width).permute(0, 2, 1)
    attention = torch.bmm(feat_a, feat_a_transpose)
    attention_new = torch.max(
        attention, dim=-1, keepdim=True)[0].expand_as(attention) - attention
    attention = self.softmax(attention_new)

    feat_e = torch.bmm(attention, feat_a).view(batch_size, -1, height, width)
    out = self.beta * feat_e + x

    return out


class _DAHead(nn.Module):
  def __init__(self, in_channels, num_classes, aux=True, norm_layer=nn.BatchNorm2d, norm_kwargs=None, **kwargs):
    super(_DAHead, self).__init__()
    self.aux = aux
    inter_channels = in_channels // 4
    self.conv_p1 = nn.Sequential(
        nn.Conv2d(in_channels, inter_channels, 3, padding=1, bias=False),
        norm_layer(inter_channels, **
                   ({} if norm_kwargs is None else norm_kwargs)),
        nn.ReLU(True)
    )
    self.conv_c1 = nn.Sequential(
        nn.Conv2d(in_channels, inter_channels, 3, padding=1, bias=False),
        norm_layer(inter_channels, **
                   ({} if norm_kwargs is None else norm_kwargs)),
        nn.ReLU(True)
    )
    self.pam = _PositionAttentionModule(inter_channels, **kwargs)
    self.cam = _ChannelAttentionModule(**kwargs)
    self.conv_p2 = nn.Sequential(
        nn.Conv2d(inter_channels, inter_channels, 3, padding=1, bias=False),
        norm_layer(inter_channels, **
                   ({} if norm_kwargs is None else norm_kwargs)),
        nn.ReLU(True)
    )
    self.conv_c2 = nn.Sequential(
        nn.Conv2d(inter_channels, inter_channels, 3, padding=1, bias=False),
        norm_layer(inter_channels, **
                   ({} if norm_kwargs is None else norm_kwargs)),
        nn.ReLU(True)
    )
    self.out = nn.Sequential(
        nn.Dropout(0.1),
        nn.Conv2d(inter_channels, num_classes, 1)
    )
    if aux:
      self.conv_p3 = nn.Sequential(
          nn.Dropout(0.1),
          nn.Conv2d(inter_channels, num_classes, 1)
      )
      self.conv_c3 = nn.Sequential(
          nn.Dropout(0.1),
          nn.Conv2d(inter_channels, num_classes, 1)
      )

  def forward(self, x):
    feat_p = self.conv_p1(x)
    feat_p = self.pam(feat_p)
    feat_p = self.conv_p2(feat_p)

    feat_c = self.conv_c1(x)
    feat_c = self.cam(feat_c)
    feat_c = self.conv_c2(feat_c)

    feat_fusion = feat_p + feat_c

    outputs = []
    fusion_out = self.out(feat_fusion)
    outputs.append(fusion_out)
    if self.aux:
      p_out = self.conv_p3(feat_p)
      c_out = self.conv_c3(feat_c)
      outputs.append(p_out)
      outputs.append(c_out)

    return tuple(outputs)
