.. _iact-point-edisp-format:

Energy dispersion format
========================

The format to store point-like energy dispersion is the following:

.. _point_edisp:

``point_edisp``
---------------

The energy dispersion information is saved as a
:ref:`fits-arrays-bintable-hdu` with the following required columns.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``MIGRA_LO``, ``MIGRA_HI`` -- ndim: 1, unit: dimensionless
    * Energy migration axis (defined above)
* ``RAD_MAX`` -- ndim: 1, unit: deg
    * Radial cut applied to each energy bin to calculate the IRF
* ``MATRIX`` -- ndim: 2, unit: dimensionless
    * Energy dispersion :math:`dP/d\mu`, see :ref:`iact-edisp`.

Recommended axis order: ``ENERGY``, ``MIGRA``, ``RAD_MAX``

Header keywords: none
