from _guetzli import lib, ffi

from _guetzli.lib import (
        GUETZLI_IMAGE_TYPE_JPEG,
        GUETZLI_IMAGE_TYPE_PNG,
        GUETZLI_IMAGE_TYPE_UNKNOWN)


DEFAULT_JPEG_QUALITY = 95


class GuetzliImage:

    def __init__(self, bytes_, type):
        pass

    @property
    def length(self):
        pass

    @property
    def type(self):
        pass

    def to_bytes(self):
        pass

    def save(self, path):
        pass


class GuetzliRgbArray:

    def __init__(self, data, width, height):
        pass

    @property
    def width(self):
        pass

    @property
    def height(self):
        pass

    def to_bytes(self):
        pass


def read_file(path):
    pass


def image_optimize(image, quality=DEFAULT_JPEG_QUALITY):
    pass


def rgbarray_optimize(rgbarray, quality=DEFAULT_JPEG_QUALITY):
    pass

