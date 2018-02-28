import os
from distutils import ccompiler

from cffi import FFI


_ROOT = os.path.abspath(os.path.dirname(__file__))
_GUETZLI_CPP = os.path.join(_ROOT, "guetzli.cpp")
_GUETZLI_H = os.path.join(_ROOT, "guetzli.h")
_GUETZLI_STATIC_LIB = ccompiler.new_compiler() \
    .library_filename("guetzli", output_dir="guetzli")

ffibuilder = FFI()
ffibuilder.set_source(
        "pyguetzli._guetzli",
        open(_GUETZLI_CPP, "r").read(),
        extra_objects=[_GUETZLI_STATIC_LIB],
        include_dirs=[_ROOT, os.path.join(_ROOT, "..", "guetzli")],
        source_extension=".cpp"
        )
ffibuilder.cdef(open(_GUETZLI_H, "r").read())


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
