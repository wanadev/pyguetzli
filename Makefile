all: pyguetzli/_guetzli.so

guetzli/bin/Release/libguetzli_static.a: guetzli/Makefile
	cd guetzli && ${MAKE} guetzli_static

pyguetzli/_guetzli.so: guetzli/bin/Release/libguetzli_static.a pyguetzli/guetzli.cpp pyguetzli/guetzli.h
	CPPFLAGS="--std=c++11" python pyguetzli/guetzli_build.py

test/libguetzli.o: pyguetzli/guetzli.cpp pyguetzli/guetzli.h
	g++ -o $@ -c $< -Ipyguetzli -Iguetzli

test/test_guetzli.o: test/test_guetzli.c
	gcc -o $@ -c $< -Ipyguetzli

test/test_guetzli: test/test_guetzli.o test/libguetzli.o guetzli/bin/Release/libguetzli_static.a
	gcc -o $@ $^ -lstdc++ -lm

test: all test/test_guetzli

clean:
	rm -f pyguetzli/*.so
	rm -f pyguetzli/*.o
	rm -f pyguetzli/_*.cpp
	rm -f test/*.o
	rm -f test/test_guetzli
	cd guetzli && ${MAKE} clean
