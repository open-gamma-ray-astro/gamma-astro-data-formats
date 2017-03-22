.. _iact-edisp-full-format:

Energy dispersion format
========================

The format to store full-enclosure energy dispersion is the following:

.. _edisp_2d_full:

``edisp_2d_full``
-----------------

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

Header keywords:

* ``HDUCLAS1`` type: string
    * First extension class (option: 'RESPONSE').
* ``HDUCLAS2`` type: string
    * Second extension class (option: 'EDISP').
* ``HDUCLAS3`` type: string
    * Third extension class (option: 'FULL-ENCLOSURE').
* ``HDUCLAS4`` type: string
    * Fourth extension class (option: 'edisp_2d').
* ``HDU_DOC = TODO``

Example data file: TODO