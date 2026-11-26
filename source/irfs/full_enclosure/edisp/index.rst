.. _iact-edisp-format:

Energy dispersion format
========================

The formats to store full-enclosure energy dispersion (see :ref:`iact-edisp`) are detailed below.
Two formats are specified:

* ``EDISP_2D`` depends on the true energy ``ENERG`` and the field of view offset ``THETA``,
  i.e. it is radially symmetric w.r.t. the field-of-view center.
* ``EDISP_3D`` depends on the true energy ``ENERG`` and the field of view coordinates ``DETX``, ``DETY``,
  which can capture non-radially symmetric energy dispersion in the field-of-view.

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
* ``HDUVERS``  = '0.3'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EDISP'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'EDISP_2D'

Example data file: :download:`here <./edisp_2d_full_example.fits>`.

.. _edisp_3d:

EDISP_3D
--------

The energy dispersion information is saved as a
:ref:`fits-arrays-bintable-hdu` with the following required columns.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``MIGRA_LO``, ``MIGRA_HI`` -- ndim: 1, unit: dimensionless
    * Energy migration axis (defined above)
* ``DETX_LO``, ``DETX_HI``, ``DETX_LO``, ``DETY_HI`` -- ndim: 1, unit: deg
    * Field of view coordinate axes (see :ref:`coords-fov`)
* ``MATRIX`` -- ndim: 4, unit: dimensionless
    * Energy dispersion :math:`dP/d\mu`, see :ref:`iact-edisp`.

Recommended axis order: ``ENERGY``, ``DETX``, ``DETY``, ``MIGRA``

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.4'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EDISP'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'EDISP_3D'

Further header keywords:

* ``FOVALIGN`` = 'ALTAZ' / 'RADEC'
    * Alignment of the field-of-view coordinate system (see :ref:`coords-fov`). It is recommended to always fill this keyword explicitly.

Example data file: :download:`here <./edisp_3d_full_example.fits>`.
