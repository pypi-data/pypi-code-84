# coding: utf8

# Dropbox 这类的云端，不是优选项，相当于把整个 bucket 的逻辑彻底交给第三方更新，与 FarBox Bucket 的基本结构有冲突，
# 在 Client 端**无法控制**同步的逻辑，并且是批量数据涌进来的，估计容易出问题。
# 如果不处理批量涌入的问题，只处理 delta 可能会好一些，但是使用者是无法接受没有 『初始化』 数据的。
# 再考虑到 FarBox 目前本身项目代码开放，自己跑一个脚本进行差量同步也是低成本的，而且**通用性**更高；
# 通过 Dropbox 在服务端进行 Hook 的更新，考虑副作用的前提下，必要性不大。@2021
