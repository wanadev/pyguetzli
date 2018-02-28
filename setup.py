#!/usr/bin/env python
# encoding: UTF-8

import os
from distutils import ccompiler

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py


class CustomBuildPy(build_py):

    def run(self):
        extra_cc_args = []

        if ccompiler.get_default_compiler() == "unix":
            os.environ["CPPFLAGS"] = "--std=c++11"
            extra_cc_args = ["-fPIC", "--std=c++11"]

        compiler = ccompiler.new_compiler()
        compiler.set_include_dirs([
            "guetzli/",
            "guetzli/third_party/butteraugli/",
            ])
        objects = compiler.compile([
            "guetzli/guetzli/butteraugli_comparator.cc",
            "guetzli/guetzli/dct_double.cc",
            "guetzli/guetzli/debug_print.cc",
            "guetzli/guetzli/entropy_encode.cc",
            "guetzli/guetzli/fdct.cc",
            "guetzli/guetzli/gamma_correct.cc",
            "guetzli/guetzli/idct.cc",
            "guetzli/guetzli/jpeg_data.cc",
            "guetzli/guetzli/jpeg_data_decoder.cc",
            "guetzli/guetzli/jpeg_data_encoder.cc",
            "guetzli/guetzli/jpeg_data_reader.cc",
            "guetzli/guetzli/jpeg_data_writer.cc",
            "guetzli/guetzli/jpeg_huffman_decode.cc",
            "guetzli/guetzli/output_image.cc",
            "guetzli/guetzli/preprocess_downsample.cc",
            "guetzli/guetzli/processor.cc",
            "guetzli/guetzli/quality.cc",
            "guetzli/guetzli/quantize.cc",
            "guetzli/guetzli/score.cc",
            "guetzli/third_party/butteraugli/butteraugli/butteraugli.cc",
            ],
            extra_preargs=extra_cc_args)
        compiler.create_static_lib(objects, "guetzli", output_dir="guetzli")

        build_py.run(self)


long_description = ""
if os.path.isfile("README.rst"):
    long_description = open("README.rst", "r").read()
elif os.path.isfile("README.md"):
    long_description = open("README.md", "r").read()


setup(
    name="pyguetzli",
    version="1.0.4",
    description="Python bindings for Google's Guetzli, a JPEG encoder that optimises JPEG compression",
    url="https://github.com/wanadev/pyguetzli",
    license="Apache-2.0",

    long_description=long_description,
    keywords="image jpeg optimize guetzli",

    author="Wanadev",
    author_email="contact@wanadev.fr",
    maintainer="Fabien LOISON, Alexis BREUST",

    packages=find_packages(),

    setup_requires=["cffi>=1.0.0"],
    install_requires=["cffi>=1.0.0"],
    extra_require={
        "PIL": ["pillow"]
    },

    cffi_modules=["pyguetzli/guetzli_build.py:ffibuilder"],

    cmdclass={
        "build_py": CustomBuildPy,
    },
)
