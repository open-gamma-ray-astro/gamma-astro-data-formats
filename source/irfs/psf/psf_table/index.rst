.. include:: ../../../references.txt

.. _psf-table:

``psf_table`` format
====================

This is a PSF FITS format we agree on for IACTs.
This file contains the offset- and energy-dependent table distribution of the PSF.

This format is almost identical to the `OGIP format for radial point spred function datasets
<http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_020/cal_gen_92_020.html>`__
The differences are that we don't have the dependency on azimuthal field of view position and the
units are different.

Columns:

* ``RAD_LO``, ``RAD_HI`` -- 1D, unit: deg
    * Offset angle from source position
* ``THETA_LO``, ``THETA_HI`` -- 1D, unit: deg
    * Field of view offset axis
* ``ENERG_LO``, ``ENERG_HI`` -- 1D, unit: TeV
    * Energy axis
* ``RPSF`` -- 3D (deg^-2), shape = (len(RAD), len(THETA), len(ENERGY))
    * Point spread function value :math:`dP/d\Omega`, see :ref:`psf-pdf`.
    * Axis order: RAD, THETA, ENERGY

Header keywords: none
