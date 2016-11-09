.. _notes:

Notes
=====

Here we collect miscellaneous notes that are helpful when reading or working with the specs.

FITS BINTABLE TFORM data type codes
-----------------------------------

The valid FITS BINTABLE TFORM data type codes are given in this table in the FITS standard paper in
`table 18 <http://www.aanda.org/articles/aa/full_html/2010/16/aa15362-10/T18.html>`__

Information on how to use it correctly via CFITSIO is
`here <https://heasarc.gsfc.nasa.gov/docs/software/fitsio/c/c_user/node20.html>`__

For `astropy.io.fits <http://docs.astropy.org/en/stable/io/fits/index.html>`__, there's these
dicts to translate FITS BINTABLE TFORM codes to Numpy dtype codes::


    >>> from astropy.io.fits.column import FITS2NUMPY, NUMPY2FITS
    >>> FITS2NUMPY
    {'J': 'i4', 'I': 'i2', 'L': 'i1', 'E': 'f4', 'M': 'c16', 'B': 'u1', 'K': 'i8', 'C': 'c8', 'D': 'f8', 'A': 'a'}
    >>> NUMPY2FITS
    {'i1': 'L', 'c16': 'M', 'i4': 'J', 'f2': 'E', 'i2': 'I', 'b1': 'L', 'i8': 'K', 'u8': 'K', 'u1': 'B', 'u4': 'J', 'u2': 'I', 'c8': 'C', 'f8': 'D', 'f4': 'E', 'a': 'A'}

But normally you never should have to manually handle these dtypes from Python.
``astropy.io.fits`` or ``astropy.table.Table`` will read and write the
TFORM FITS header keys correctly for you.
