import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="caselockerapi",
    version="0.0.6",
    author="Litigation Locker",
    author_email="trennon@litigationlocker.com",
    description="Python API to interact with CaseLocker installation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://litigationlocker.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
