.. _iact-point-edisp-format:

Energy dispersion format
========================

The format to store point-like energy dispersion is the following:

.. _point_edisp:

``edisp_2d``
------------

The energy dispersion information is saved as a
:ref:`fits-arrays-bintable-hdu` with the following required columns.

Columns:

* ``MATRIX`` type: float, dimensions: 3 
    * Matrix holding the probability for a given energy migration at a certain true energy and offset.
* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``RAD_MAX`` -- ndim: 1, unit: deg
    * Radial cut applied to each energy bin to calculate the IRF
* ``MIGRA_LO``, ``MIGRA_HI`` -- ndim: 1, unit: dimensionless
    * Energy migration axis (defined above)
* ``MATRIX`` -- ndim: 2, unit: dimensionless
    * Energy dispersion :math:`dP/d\mu`, see formula above.

Recommended axis order: ``ENERGY``, ``MIGRA``, ``THETA``

Header keywords: none
