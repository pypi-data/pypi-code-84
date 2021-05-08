import setuptools

setuptools.setup(
    install_requires=[
        'nvidia-pyindex==1.0.8',
        'hdbscan==0.8.27',
        'numpy>=1.20.1',
        'pandas>=1.2.3',
        'torch>=1.8.1',
        'tritonclient[all]>=2.8.0',
        'pyspark>=3.0.2',
        'schedule==1.1.0'
    ]
)