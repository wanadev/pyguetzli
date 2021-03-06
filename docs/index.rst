Welcome to pyguetzli's documentation!
=====================================

|Github| |Discord| |PYPI Version| |Build Status| |License|

**PyGuetzli** is a Python binding for Google's Guetzli_ library.

Description of **Guetzli** from official's repo:

    Guetzli is a JPEG encoder that aims for excellent compression density at
    high visual quality. Guetzli-generated images are typically 20-30% smaller
    than images of equivalent quality generated by libjpeg. Guetzli generates
    only sequential (nonprogressive) JPEGs due to faster decompression speeds
    they offer.


Example Usage
-------------

.. code-block:: python

   import pyguetzli

   input_jpeg = open("./test/image.jpg", "rb").read()
   optimized_jpeg = pyguetzli.process_jpeg_bytes(input_jpeg)

   output = open("./optimized.jpg", "wb")
   output.write(optimized_jpeg)

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    install
    guetzli
    pil_image
    differences
    trouble-shooting
    contributing
    license

* :ref:`genindex`
* :ref:`modindex`

.. _guetzli: https://github.com/google/guetzli


.. |Github| image:: https://img.shields.io/github/stars/wanadev/pyguetzli?label=Github&logo=github
   :target: https://github.com/wanadev/pyguetzli
.. |Discord| image:: https://img.shields.io/badge/chat-Discord-8c9eff?logo=discord&logoColor=ffffff
   :target: https://discord.gg/BmUkEdMuFp
.. |PYPI Version| image:: https://img.shields.io/pypi/v/pyguetzli.svg
   :target: https://pypi.python.org/pypi/pyguetzli
.. |Build Status| image:: https://github.com/wanadev/pyguetzli/actions/workflows/python-ci.yml/badge.svg
   :target: https://github.com/wanadev/pyguetzli/actions
.. |License| image:: https://img.shields.io/pypi/l/pyguetzli.svg
   :target: https://github.com/wanadev/pyguetzli/blob/master/LICENSE
