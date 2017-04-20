.. _iact-edisp-point-format:

Energy dispersion format
========================

The format to store point-like energy dispersion is the following:

.. _edisp_2d_point:

``edisp_2d_point``
------------------

The energy dispersion information is saved as a
:ref:`fits-arrays-bintable-hdu` with the following required columns.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``MIGRA_LO``, ``MIGRA_HI`` -- ndim: 1, unit: dimensionless
    * Energy migration axis (defined above)
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``RAD_MAX`` -- ndim: 2, unit: deg
    * Radial cut applied to calculate the IRF component. This cut will 
      change as a function of energy and theta.
* ``MATRIX`` -- ndim: 3, unit: dimensionless
    * Energy dispersion :math:`dP/d\mu`, see :ref:`iact-edisp`.

Recommended axis order: ``ENERGY``, ``MIGRA``, ``THETA``, ``RAD_MAX``

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EDISP'
* ``HDUCLAS3`` = 'POINT-LIKE'
* ``HDUCLAS4`` = 'EDISP_2D'

Example data file: TODO