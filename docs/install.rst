Installation
============

Installing From PyPI
--------------------

To install PyGuetzli from the PYPI package, just run the following command::

    pip install pyguetzli

.. NOTE::

    We provide prebuilt package for PyGuetzli. To be able to use them, you will need **pip >= 19.0**. If you want to install this library with an older pip version, you will have to install additional build dependencies (see :ref:`source-install` bellow).

.. NOTE::

    If you are using Linux distributions that are not based on ``libc6``, like Alpine, you will also have to install the additional build dependencies  (see :ref:`source-install` bellow).


.. _source-install:

Installing From Source
----------------------

As PyGuetzli is a binding to a C++ library, you will need a recent GCC and GNU
Make version to install it. On Debian / Ubuntu, this can be installed with the
following command::

    sudo apt-get install build-essential

Then you can install PyGuetzli::

    git clone https://github.com/wanadev/pyguetzli.git
    cd pyguetzli
    pip install .
