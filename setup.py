# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

# setup.py py2exe

setup(
    name="ipconfig",
    version="1.0",
    description="Config ip address ipv4 easily an faster.",
    author="Jose Luis Pinto Hernandez",
    author_email="josep8686@gmail.com",
    url="joseluispinto.net",
    license="Compleatly Free License",
    scripts=["ipconfig.py"],
    console=["ipconfig.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)