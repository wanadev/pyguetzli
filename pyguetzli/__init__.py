from .version import VERSION
from . import guetzli


def optimize_from_file(path, quality=guetzli.DEFAULT_JPEG_QUALITY):
    image = guetzli.read_file(path)
    image_opti = guetzli.image_optimize(image, quality)
    return image_opti


def optimize_from_image_bytes(data, quality=guetzli.DEFAULT_JPEG_QUALITY):
    image = guetzli.GuetzliImage(data, guetzli.GuetzliImage.TYPE_JPEG)  # TODO detect format from bytes
    image_opti = guetzli.image_optimize(image, quality)
    return image_opti


def optimize_from_rgb_bytes(data, width, height, quality=guetzli.DEFAULT_JPEG_QUALITY):
    rgb_array = guetzli.GuetzliRgbArray(data, width, height)
    image_opti = guetzli.rgbarray_optimize(rgb_array, quality)
    return image_opti

