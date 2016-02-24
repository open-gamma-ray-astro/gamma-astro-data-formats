.. include:: ../../../references.txt

.. _psf-table:

``psf_table`` format
====================

This is a PSF FITS format we agree on for IACTs.
This file contains the offset- and energy-dependent table distribution of the PSF.

This format is almost identical to the `OGIP radial PSF`_ format.
The differences are that we don't have the dependency on azimuthal field of
view position and the units are different.

Columns:

* ``RAD_LO``, ``RAD_HI`` -- ndim: 1, unit: deg
    * Offset angle from source position
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``RPSF`` -- ndim: 3, unit: deg^-2
    * Point spread function value :math:`dP/d\Omega`, see :ref:`psf-pdf`.

The ``RPSF`` array is three-dimensional:
* Axis order: RAD, THETA, ENERGY
* Shape: (len(RAD), len(THETA), len(ENERGY))

Header keywords: none
