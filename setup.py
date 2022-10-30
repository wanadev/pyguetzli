#!/usr/bin/env python
# encoding: UTF-8

import io
import os

from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext


class CustomBuildExt(build_ext):
    def build_extensions(self):
        extra_cc_args = []

        if self.compiler.compiler_type == "unix":
            os.environ["CPPFLAGS"] = "--std=c++11"
            extra_cc_args = ["-fPIC", "--std=c++11", "-O3"]

        if self.compiler.compiler_type == "msvc":
            extra_cc_args = ["/O2"]

        self.compiler.set_include_dirs(
            self.include_dirs
            + [
                "guetzli/",
                "guetzli/third_party/butteraugli/",
            ]
        )
        objects = self.compiler.compile(
            [
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
            extra_preargs=extra_cc_args,
        )
        self.compiler.create_static_lib(objects, "guetzli", output_dir="guetzli")

        build_ext.build_extensions(self)


long_description = ""
if os.path.isfile("README.rst"):
    with io.open("README.rst", "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="pyguetzli",
    version="1.0.14",
    description="Python bindings for Google's Guetzli, a JPEG encoder that optimises JPEG compression",  # noqa
    url="https://github.com/wanadev/pyguetzli",
    project_urls={
        "Source Code": "https://github.com/wanadev/pyguetzli",
        "Documentation": "https://wanadev.github.io/pyguetzli/",
        "Changelog": "https://github.com/wanadev/pyguetzli#changelog",
        "Issues": "https://github.com/wanadev/pyguetzli/issues",
        "Chat": "https://discord.gg/BmUkEdMuFp",
    },
    license="Apache-2.0",
    long_description=long_description,
    keywords="image jpeg optimize guetzli",
    author="Wanadev",
    author_email="contact@wanadev.fr",
    maintainer="Fabien LOISON, Alexis BREUST",
    packages=find_packages(),
    setup_requires=["cffi>=1.0.0"],
    install_requires=["cffi>=1.0.0"],
    extras_require={
        "PIL": ["pillow"],
        "dev": [
            "nox",
            "flake8",
            "Sphinx",
            "sphinx-rtd-theme",
            "pytest",
        ],
    },
    cffi_modules=["pyguetzli/guetzli_build.py:ffibuilder"],
    cmdclass={
        "build_ext": CustomBuildExt,
    },
)
