Trouble Shooting
================

Errors About Undeclared “nullptr” When Installing / Building PyGuetzli
----------------------------------------------------------------------

Guetzli is written in C++ 11, so you can encounter errors when trying to
compile PyGuetzli with GCC < 6.0::

   ...

   build/temp.linux-x86_64-2.7/pyguetzli._guetzli.cpp: In function ‘int guetzli_process_rgb_bytes(char*, int, int, char**, int)’:

   build/temp.linux-x86_64-2.7/pyguetzli._guetzli.cpp:474:21: error: ‘nullptr’ was not declared in this scope

        Process(params, nullptr, inData, width, height, &outData);

                        ^

   error: command 'gcc' failed with exit status 1

To compile PyGuetzli using older GCC version, you can set the following
environment variable::

   CPPFLAGS="--std=c++11"

See `issue #1 <https://github.com/wanadev/pyguetzli/issues/1>`__ for
more information.
