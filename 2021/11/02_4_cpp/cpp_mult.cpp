#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <iostream>

namespace py = pybind11;

void mult(py::array_t<double>& _c, py::array_t<double>& _a, py::array_t<double>& _b) {

    py::buffer_info buf_a = _a.request();
    py::buffer_info buf_b = _b.request();
    py::buffer_info buf_c = _c.request();

    double* a = (double*)buf_a.ptr;
    double* b = (double*)buf_b.ptr;
    double* c = (double*)buf_c.ptr;

    unsigned long size = buf_a.shape[0];
    unsigned long i, j, k;

    std::cout << "Matrix size: " << size << std::endl;

    for (i = 0; i < size; ++i) {
        for (j = 0; j < size; ++j) {
            c[i*size + j] = 0;
            for (k = 0; k < size; ++k) {
                c[i*size + j] += a[i*size + k] * b[k*size + j];
            }
        }
    }
};


PYBIND11_MODULE(cpp_mult, m) {
    m.def("mult", &mult, "A function that multiplies two matrices");
}
