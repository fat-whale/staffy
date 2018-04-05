import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "staffy",
    version = "0.0.1",
    author = "Urbano Gutierrez",
    author_email = "urbano@fatwhale.io",
    description = ("A simple wrapper for our internal staff API."),
    license = "BSD",
    keywords = "api wrapper",
    url = "https://github.com/fat-whale/staffy",
    packages=['staffy'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)