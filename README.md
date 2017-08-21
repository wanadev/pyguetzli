# PyGuetzli

[![Build Status](https://travis-ci.org/wanadev/pyguetzli.svg?branch=master)](https://travis-ci.org/wanadev/pyguetzli)
[![PYPI Version](https://img.shields.io/pypi/v/pyguetzli.svg)](https://pypi.python.org/pypi/pyguetzli)
[![License](https://img.shields.io/pypi/l/pyguetzli.svg)](https://github.com/wanadev/pyguetzli/blob/master/LICENSE)


**PyGuetzli** is a Python binding for Google's [Guetzli][guetzli] library.

Description of **Guetzli** from official's repo:

> Guetzli is a JPEG encoder that aims for excellent compression density at high
> visual quality. Guetzli-generated images are typically 20-30% smaller than
> images of equivalent quality generated by libjpeg. Guetzli generates only
> sequential (nonprogressive) JPEGs due to faster decompression speeds they
> offer.

[guetzli]: https://github.com/google/guetzli


## Building and Installing PyGuetzli

In order to build Guetzli, GCC and GNU Make are required. On Debian / Ubuntu,
this can be installed with the following command:

    sudo apt-get install build-essential


### Installing from PYPI

To install PyGuetzli from the PYPI package, just run the following command:

    pip install pyguetzli

### Installing from source

To build and install PyGuetzli from source, clone the repository, and run the
`pip install` command from the project's root directory:

    git clone https://github.com/wanadev/pyguetzli.git
    cd pyguetzli
    pip install .


## Using PyGuetzli

Example:

```python
import pyguetzli

input_jpeg = open("./test/image.jpg", "rb").read()
optimized_jpeg = pyguetzli.process_jpeg_bytes(input_jpeg)

output = open("./optimized.jpg", "wb")
output.write(optimized_jpeg)
```

For more information, please visit the project's documentation:

* http://wanadev.github.io/pyguetzli/


## Trouble Shooting

### Errors About Undeclared "nullptr" When Installing / Building PyGuetzli

Guetzli is written in C++ 11, so you can encounter errors when trying to
compile PyGuetzli with GCC < 6.0:

    ...

    build/temp.linux-x86_64-2.7/pyguetzli._guetzli.cpp: In function ‘int guetzli_process_rgb_bytes(char*, int, int, char**, int)’:

    build/temp.linux-x86_64-2.7/pyguetzli._guetzli.cpp:474:21: error: ‘nullptr’ was not declared in this scope

         Process(params, nullptr, inData, width, height, &outData);

                         ^

    error: command 'gcc' failed with exit status 1

To compile PyGuetzli using older GCC version, you can set the following
environment variable:

    CPPFLAGS="--std=c++11"

See [issue #1](https://github.com/wanadev/pyguetzli/issues/1) for more
information.


## Hacking

### Running Tests

    pip install tox
    tox

By default test will run in Python 2.7, 3.5 and 3.6. To run only on a specific
Python version run the following commands:

    tox -e py27
    tox -e py35
    tox -e py36

### Generating Documentation

From a virtualenv:

    pip install -r requirements.txt
    python setup.py build_sphinx


## Changelog

* **1.0.0**:
    * New and simpler API
    * Built-in function to deal with PIL / Pillow Images
    * Documentation (Sphinx)
    * Guetzli update
* **0.9.0**: Initial release
