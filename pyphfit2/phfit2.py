import ctypes as _ctypes
import numpy as _np
import astropy.units as _u
import os as _os

_phfit2_wrappers = _ctypes.CDLL(
    _os.path.join(
        _os.path.realpath(
            _os.path.dirname(__file__)), 'lib/phfit2.so'))


def phfit2(nz, ne, shell, wave):
    """
    Wrapper for the Verner et al. `phfit2` routine.

    Python wrapper for the Fortran routine `phfit2` from [1]_. `phfit2` fits
    ground state atomic cross sections for atomic numbers 1 through 30 for all
    shells occupied in these ground states.

    Parameters
    ----------
    nz : int
        Atomic number from 1 to 30.
    ne : int
        Number of electrons bound to the nucleus from 1 to `nz`.
    shell : int
        Shell number from 1 to 7 where:
            1 - 1s
            2 - 2s
            3 - 2p
            4 - 3s
            5 - 3p
            6 - 3d
            7 - 4s
    wave : Quantity or array_like
        Energy/ies [eV] at which to compute cross section. If this is a
        quantity, it can have any unit equivalent to eV as defined by the
        `astropy.spectral()` equivalencies.

    Returns
    -------
    res : Quantity or array_like
        Cross section [Mb]. The `type` of this will be equivalent to the one of
        `wave`. However, it might differ in precision, since `phfit2` works
        with single precision floats..

    Raises
    ------
    ValueError :
        If `nz`, `ne` and/or `shell` lie outside of the allowed range and if
        `wave` has wrong dimensions.

    References
    ----------
    .. [1] Verner et al. 1996, 1996ApJ...465..487V

    Examples
    --------
    >>> phfit2(1, 1, 1, 13.6)
    6.346298694610596
    >>> phfit2(1, 1, 1, _np.array([13.6, 200, 44]))
    array([6.3462987e+00, 2.2047125e-03, 2.3108763e-01], dtype=float32)
    >>> phfit2(1, 1, 1, 13.6*_u.eV)
    <Quantity 6.3462987 Mbarn>
    >>> phfit2(1, 1, 1, _np.array([13.6, 200, 44])*_u.eV)
    <Quantity [6.3462987e+00, 2.2047125e-03, 2.3108763e-01] Mbarn>
    >>> phfit2(1, 1, 1, 0.01*_u.micron)
    <Quantity 0.00995493 Mbarn>
    """
    if nz < 1 or nz > 30:
        raise ValueError("nz must be 1 <= nz <= 30.")
    if ne < 1 or ne > nz:
        raise ValueError("ne must be 1 <= ne <= nz.")
    if shell < 1 or shell > 7:
        raise ValueError("shell must be 1 <= shell <= 7.")

    # determine if we use units or not
    try:
        e = wave.to(_u.eV, equivalencies=_u.spectral()).value
        units = True
    except AttributeError:
        units = False
        e = wave

    # check dimensionality of input
    e = _np.asarray(e, dtype=_np.float32)
    if e.ndim > 1:
        raise ValueError("Energy array needs to have zero or one dimensions.")
    scalar_in = e.ndim == 0
    le = 1 if scalar_in else len(e)

    res = _np.zeros_like(e, dtype=_np.float32)

    _phfit2_wrappers.c_phfit2_arr(_ctypes.c_int(nz),
                                  _ctypes.c_int(ne),
                                  _ctypes.c_int(shell),
                                  e.ctypes.data_as(
                                      _ctypes.POINTER(_ctypes.c_float)),
                                  _ctypes.c_int(le),
                                  res.ctypes.data_as(
                                      _ctypes.POINTER(_ctypes.c_float)))
    if scalar_in:
        # scalar in means scalar out
        res = float(res)
    if units:
        # units in means units out
        return res*_u.Mbarn
    else:
        return res
