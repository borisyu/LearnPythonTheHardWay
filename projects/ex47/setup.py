try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Boris",
    "url": "https://github.com/borisyu/LearnPythonTheHardWay",
    "download_urll": "https://github.com/borisyu/LearnPythonTheHardWay",
    "author_email": "boris@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["ex47"],
    "scripts": [],
    "name": "ex47"
}

setup(**config)