from .version import VERSION
from . import guetzli


def optimize_from_file(path, quality=guetzli.DEFAULT_JPEG_QUALITY):
    pass


def optimize_from_image_bytes(data, quality=guetzli.DEFAULT_JPEG_QUALITY):
    pass


def optimize_from_rgb_bytes(data, width, height, quality=guetzli.DEFAULT_JPEG_QUALITY):
    pass

