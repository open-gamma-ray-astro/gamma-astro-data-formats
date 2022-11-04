.. include:: ../../../../references.txt

.. _psf_table:

PSF_TABLE
=========

This is a PSF FITS format we agree on for IACTs.
This file contains the offset- and energy-dependent table distribution of the PSF.

This format is almost identical to the `OGIP radial PSF`_ format. The
differences are that we don't have the dependency on azimuthal field of view
position, the units are different and the recommended axis order is different
(to have uniformity across axis order in the IACT DL3 IRFs).

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis (see :ref:`coords-fov`)
* ``RAD_LO``, ``RAD_HI`` -- ndim: 1, unit: deg
    * Offset angle from source position
* ``RPSF`` -- ndim: 3, unit: sr^-1
    * Point spread function value :math:`dP/d\Omega`, see :ref:`psf-pdf`.

Recommended axis order: ``ENERGY``, ``THETA``, ``RAD``.

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.3'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'PSF'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'PSF_TABLE'

Example data file: TODO
