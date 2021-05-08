# setup.py 是一个 setuptools 的构建脚本，其中包含了项目和代码文件的信息
# 如果没有需要先安装，pip install setuptools
import setuptools

setuptools.setup(
    # 项目的名称
    name="verify-valid",
    # 项目的版本
    version="0.0.2",
    # 项目的作者
    author="gao",
    # 作者的邮箱
    author_email="513370497@qq.com",
    # 项目描述
    description="校验时间的有效性",
    # 项目的长描述
    long_description="校验时间的有效性",
    # 以哪种文本格式显示长描述
    long_description_content_type="text/markdown",  # 所需要的依赖
    install_requires=[],  # 比如["flask>=0.10"]
    # 项目主页
    url="https://www.baidu.com",
    # 项目中包含的子包，find_packages() 是自动发现根目录中的所有的子包。
    packages=setuptools.find_packages(),
    # 其他信息，这里写了使用 Python3，MIT License许可证，不依赖操作系统。
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
