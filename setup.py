from Cython.Build import cythonize
from setuptools import setup

setup(
    # ext_modules=cythonize("helloworld.pyx")
    # ext_modules=cythonize("fibonacci_cython.pyx")
    # ext_modules=cythonize("primes_cython.pyx", annotate=True)
    ext_modules=cythonize("calc_pi.pyx", annotate=True)
)
