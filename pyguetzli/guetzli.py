from ._guetzli import lib, ffi


DEFAULT_JPEG_QUALITY = 95


def process_jpeg_bytes(bytes_in, quality=DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from JPEG-encoded bytes.

    Arguments:
    bytes_in -- the input image's bytes

    Keyword Arguments:
    quality -- the output JPEG quality (default 95)
    """
    pass


def process_rgb_bytes(bytes_in, width, height, quality=DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from RGB bytes.

    Arguments:
    bytes_in -- the input image's bytes
    width -- the width of the input image
    height -- the height of the input image

    Keyword Arguments:
    quality -- the output JPEG quality (default 95)
    """
    pass

