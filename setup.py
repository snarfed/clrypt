import os

from clrypt import __version__

try:
  from setuptools import setup
except:
  from distutils.core import setup


setup(name = "clrypt",
      version = __version__,
      description = "A tool to encrypt/decrypt files.",
      author = "Color Genomics",
      author_email = "dev@getcolor.com",
      url = "https://github.com/ColorGenomics/clrypt",
      packages = ["clrypt"],
      install_requires=['M2Crypto>=0.22.3'],
      license = "MIT",
      )
