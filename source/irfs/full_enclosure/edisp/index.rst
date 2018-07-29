.. _iact-edisp-format:

Energy dispersion format
========================

The format to store full-enclosure energy dispersion (see :ref:`iact-edisp`) is the following:

.. _edisp_2d:

EDISP_2D
--------

The energy dispersion information is saved as a
:ref:`fits-arrays-bintable-hdu` with the following required columns.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``MIGRA_LO``, ``MIGRA_HI`` -- ndim: 1, unit: dimensionless
    * Energy migration axis (defined above)
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis (see :ref:`coords-fov`)
* ``MATRIX`` -- ndim: 3, unit: dimensionless
    * Energy dispersion :math:`dP/d\mu`, see :ref:`iact-edisp`.

Recommended axis order: ``ENERGY``, ``MIGRA``, ``THETA``

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EDISP'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'EDISP_2D'  

Example data file: TODO
