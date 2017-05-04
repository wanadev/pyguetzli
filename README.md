# PyGuetzli

**PyGuetzli** is a Python bindings for Google's **Guetzli**.

Description of Guetzli from official's repo:

> Guetzli is a JPEG encoder that aims for excellent compression density at high
> visual quality. Guetzli-generated images are typically 20-30% smaller than
> images of equivalent quality generated by libjpeg. Guetzli generates only
> sequential (nonprogressive) JPEGs due to faster decompression speeds they
> offer.


## Building PyGuetzli

In order to build Guetzli, GCC, GNU Make and libpng are required. On Debian
/ Ubuntu, this can be installed with the following command:

    sudo apt-get install build-essential libpng-dev

then, to build and install PyGuetzli, run the following command from the
project's root directory:

    pip install .


## Testing

    pip install cffi pytest
    python setup.py develop
    pytest
