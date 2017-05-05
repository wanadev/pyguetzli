all: pyguetzli/_guetzli.so

./guetzli/bin/Release/libguetzli_static.a: ./guetzli/Makefile
	cd ./guetzli && ${MAKE}

pyguetzli/_guetzli.so: ./guetzli/bin/Release/libguetzli_static.a
	CPPFLAGS="--std=c++11" python pyguetzli/guetzli_build.py

clean:
	rm -f pyguetzli/*.so
	rm -f pyguetzli/*.o
	rm -f pyguetzli/_*.cpp
	cd ./guetzli && ${MAKE} clean
