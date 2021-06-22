#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="uberfmt",
    version="0.1",
    url="https://github.com/magv/uberfmt",
    author="Vitaly Magerya",
    description="Format paragraphs of text, inside or outside of source code comments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["wcwidth>=0.1.8"],
    data_files=[("bin", ["uberfmt"])]
)
