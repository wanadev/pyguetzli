from . import guetzli


def process_image_from_file(path, quality=guetzli.DEFAULT_JPEG_QUALITY):
    image = guetzli.guetzli_image_read_file(path)
    image_opti = guetzli.guetzli_image_process(image, quality)
    return image_opti


def process_image_from_bytes(data, quality=guetzli.DEFAULT_JPEG_QUALITY):
    image = guetzli.GuetzliImage(data, guetzli.GuetzliImage.TYPE_JPEG)  # TODO detect format from bytes
    image_opti = guetzli.guetzli_image_process(image, quality)
    return image_opti


def process_rgb_bytes(data, width, height, quality=guetzli.DEFAULT_JPEG_QUALITY):
    rgb_array = guetzli.GuetzliRgbArray(data, width, height)
    image_opti = guetzli.guetzli_rgb_array_process(rgb_array, quality)
    return image_opti

