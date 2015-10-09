#!/usr/bin/python

from distutils.core import setup

setup(
    name = "gistimporter",
    version = "1.0.0",
    description = "An importer for Python 3.x to allow import modules from gists.",
    author = "Salvador de la Puente González",
    author_email = "salva@unoyunodiez.com",
    url = "https://github.com/lodr/gistimporter",
    download_url = "https://github.com/lodr/gistimporter/archive/master.zip",
    keywords = ["gist", "import", "importer", "github"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
        ],
    long_description = open('./README.txt').read(),
    license = open('./LICENSE').read()
)
