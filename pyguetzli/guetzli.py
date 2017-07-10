from ._guetzli import lib, ffi


DEFAULT_JPEG_QUALITY = 95


def process_jpeg_bytes(bytes_in, quality=DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from JPEG-encoded bytes.

    Arguments:
    bytes_in -- the input image's bytes

    Keyword Arguments:
    quality -- the output JPEG quality (default 95)
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
        raise ValueError("Invalid JPEG: Guetzli was not able to decode the image")

    bytes_out = ffi.cast("char*", bytes_out_p_gc[0])
    return ffi.unpack(bytes_out, length)


def process_rgb_bytes(bytes_in, width, height, quality=DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from RGB bytes.

    Arguments:
    bytes_in -- the input image's bytes
    width -- the width of the input image
    height -- the height of the input image

    Keyword Arguments:
    quality -- the output JPEG quality (default 95)
    """
    if len(bytes_in) != width * height * 3:
        raise ValueError("bytes_in length is not coherent with given width and height")

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

