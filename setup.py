from setuptools import setup, find_packages
from sys import platform

setup(
    name='DidimoLS',
    version='0.6',
    license='MIT',
    author="Bramwel Ochieng",
    author_email='bramwelochieng@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    url='https://github.com/ochi96/DLS',
    keywords='lips segmentation inferencing ',
    install_requires=[
        'wheel',
        'numpy',
        'torch',
        'opencv_python',
        'torchvision',
        'Pillow'
      ]
)