.. include:: ../../../../references.txt

.. _psf-table_full:

``psf_table_full``
==================

This is a PSF FITS format we agree on for IACTs.
This file contains the offset- and energy-dependent table distribution of the PSF.

This format is almost identical to the `OGIP radial PSF`_ format. The
differences are that we don't have the dependency on azimuthal field of view
position, the units are different and the recommended axis order is different
(to have uniformity across axis order in the IACT DL3 IRFs).

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``RAD_LO``, ``RAD_HI`` -- ndim: 1, unit: deg
    * Offset angle from source position
* ``RPSF`` -- ndim: 3, unit: sr^-1
    * Point spread function value :math:`dP/d\Omega`, see :ref:`psf-pdf`.

Recommended axis order: ``ENERGY``, ``THETA``, ``RAD``.

Header keywords:

* ``HDUCLAS1`` type: string
    * First extension class (option: 'RESPONSE').
* ``HDUCLAS2`` type: string
    * Second extension class (option: 'RPSF').
* ``HDUCLAS3`` type: string
    * Third extension class (option: 'FULL-ENCLOSURE').
* ``HDUCLAS4`` type: string
    * Fourth extension class (option: 'psf_table').
* ``HDU_DOC = TODO``

Example data file: TODO