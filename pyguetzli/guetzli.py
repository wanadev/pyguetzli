"""
This module contains functions binded from the Guetzli C++ API.
"""


from ._guetzli import lib, ffi


#: Default quality for outputted JPEGs
DEFAULT_JPEG_QUALITY = 95


def process_jpeg_bytes(bytes_in, quality=DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from JPEG-encoded bytes.

    :param bytes_in: the input image's bytes
    :param quality: the output JPEG quality (default 95)

    :returns: Optimized JPEG bytes
    :rtype: bytes

    :raises ValueError: Guetzli was not able to decode the image (the image is
                        probably corrupted or is not a JPEG)

    .. code:: python

        import pyguetzli

        input_jpeg_bytes = open("./test/image.jpg", "rb").read()
        optimized_jpeg = pyguetzli.process_jpeg_bytes(input_jpeg_bytes)
    """
    bytes_out_p = ffi.new("char**")
    bytes_out_p_gc = ffi.gc(bytes_out_p, lib.guetzli_free_bytes)

    length = lib.guetzli_process_jpeg_bytes(
            bytes_in,
            len(bytes_in),
            bytes_out_p_gc,
            quality
            )

    if length == 0:
        raise ValueError("Invalid JPEG: Guetzli was not able to decode the image")  # noqa

    bytes_out = ffi.cast("char*", bytes_out_p_gc[0])
    return ffi.unpack(bytes_out, length)


def process_rgb_bytes(bytes_in, width, height, quality=DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from RGB bytes.

    :param bytes bytes_in: the input image's bytes
    :param int width: the width of the input image
    :param int height: the height of the input image
    :param int quality: the output JPEG quality (default 95)

    :returns: Optimized JPEG bytes
    :rtype: bytes

    :raises ValueError: the given width and height is not coherent with the
                        ``bytes_in`` length.

    .. code:: python

        import pyguetzli

        # 2x2px RGB image
        #                |    red    |   green   |
        image_pixels  = b"\\xFF\\x00\\x00\\x00\\xFF\\x00"
        image_pixels += b"\\x00\\x00\\xFF\\xFF\\xFF\\xFF"
        #                |   blue    |   white   |

        optimized_jpeg = pyguetzli.process_rgb_bytes(image_pixels, 2, 2)
    """
    if len(bytes_in) != width * height * 3:
        raise ValueError("bytes_in length is not coherent with given width and height")  # noqa

    bytes_out_p = ffi.new("char**")
    bytes_out_p_gc = ffi.gc(bytes_out_p, lib.guetzli_free_bytes)

    length = lib.guetzli_process_rgb_bytes(
            bytes_in,
            width,
            height,
            bytes_out_p_gc,
            quality
            )

    bytes_out = ffi.cast("char*", bytes_out_p_gc[0])
    return ffi.unpack(bytes_out, length)
