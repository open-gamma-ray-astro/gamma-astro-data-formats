.. _iact-edisp-format:

Energy dispersion format
========================

The format to store full-enclosure energy dispersion is the following:

.. _edisp_2d:

``edisp_2d``
------------

The energy dispersion information is saved as a
:ref:`fits-arrays-bintable-hdu` with the following required columns.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``MIGRA_LO``, ``MIGRA_HI`` -- ndim: 1, unit: dimensionless
    * Energy migration axis (defined above)
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``MATRIX`` -- ndim: 3, unit: dimensionless
    * Energy dispersion :math:`dP/d\mu`, see :ref:`iact-edisp`.

Recommended axis order: ``ENERGY``, ``MIGRA``, ``THETA``

Header keywords: none
