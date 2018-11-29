# pyphfit2
Python wrapper for the Fortran routine `phfit2` from Verner et
al. 1996. `phfit2` fits ground state atomic cross sections for atomic numbers 1
through 30 for all shells occupied in these ground states.

This is mostly to be seen as an expirement in creating a Python package that
interfaces with Fortran code. It would likely have been a lot easier to just
re-implement the fitting routine in Python. However, my hope is that it might
nevertheless be useful for someone.

## Installation
### Building the shared library
First, you need to build a shared library from `phfit2.f` and
`phfit2_wrapper.f90` and copy it to `pyphfit2/lib/phfit2.so`. `phfit2/makefile`
gives an example of how to do this on Linux using either gfortran of ifort.

So if you're on Linux, choose your Fortran compiler in the makefile and then do:
```
cd phfit2
make
make install
```

### `setup.py`
With the shared library built, you can then run `python setup.py install`.

### Notes
I gave up on trying to get setuptools to do the building of the shared
library. This is almost certainly possible using `f2py` or `f2py3`, but the
goal here was to use Fortran-C interoperability to interface Python and Fortran
as directly as possible using the `ctypes` library. Maybe subclassing
`distutils.core.Extension`, or subclassing
`numpy.distutils.command.build_ext.build_ext` would work, but I have more
important things to do.

Right now I'm abusing the `data_files` argument to `setuptools.setup` to get it
to install the pre-built shared library.

## Contributing
I'm happy to accept pull requests.
