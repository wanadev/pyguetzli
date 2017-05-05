from _guetzli import lib, ffi


DEFAULT_JPEG_QUALITY = 95


class GuetzliImage(object):

    TYPE_JPEG = lib.GUETZLI_IMAGE_TYPE_JPEG
    TYPE_PNG = lib.GUETZLI_IMAGE_TYPE_PNG
    TYPE_UNKNOWN = lib.GUETZLI_IMAGE_TYPE_UNKNOWN

    _cdata = None

    def __init__(self, bytes_, type_):
        guetzli_image_p = lib.guetzliImageNew(type_, len(bytes_))
        ffi.memmove(guetzli_image_p.data, bytes_, len(bytes_))
        guetzli_image_p_gc = ffi.gc(guetzli_image_p, lib.guetzliImageFree)
        self._cdata = guetzli_image_p_gc

    @classmethod
    def from_guetzli_image_p(cls, guetzli_image_p):
        if ffi.typeof(guetzli_image_p).cname != "GuetzliImage *":
            raise ValueError("Expected guetzli_image_p to be a 'GuetzliImage *'")
        image = cls.__new__(cls)
        image._cdata = guetzli_image_p
        return image

    @property
    def length(self):
        return self._cdata.length

    @property
    def type(self):
        return self._cdata.type

    def to_bytes(self):
        return ffi.unpack(self._cdata.data, self._cdata.length)

    def save(self, path):
        lib.guetzliImageWriteFile(path, self._cdata)


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
    guetzli_image_p = lib.guetzliImageReadFile(path,
            GuetzliImage.TYPE_JPEG)  # FIXME

    if not guetzli_image_p.length:
        raise IOError("Could not open the file")

    guetzli_image_p_gc = ffi.gc(guetzli_image_p, lib.guetzliImageFree)

    return GuetzliImage.from_guetzli_image_p(guetzli_image_p_gc)


def image_optimize(image, quality=DEFAULT_JPEG_QUALITY):
    opti_guetzli_imge_p = lib.guetzliImageOptimize(image._cdata, quality)
    opti_guetzli_imge_p_gc = ffi.gc(opti_guetzli_imge_p, lib.guetzliImageFree)
    return GuetzliImage.from_guetzli_image_p(opti_guetzli_imge_p_gc)


def rgbarray_optimize(rgbarray, quality=DEFAULT_JPEG_QUALITY):
    pass

