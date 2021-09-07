all:
	g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` -I . cpp_mult.cpp -o cpp_mult`python3-config --extension-suffix`

clean:
	rm *.so
