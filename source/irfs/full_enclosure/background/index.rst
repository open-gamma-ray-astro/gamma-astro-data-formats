.. include:: ../../../references.txt

.. _iact-background-format:

Background format
=================

Here we specify two formats for the background template models (see :ref:`bkg`) of a full-enclosure IRF:

* ``bkg_2d`` models depend on ``ENERGY`` and ``THETA``, i.e. are radially symmetric.
* ``bkg_3d`` models depend on ``ENERGY`` and field of view coordinates ``DETX`` and ``DETY``.

.. _bkg_2d:

``bkg_2d``
----------

The ``bkg_2d`` format contains a 2-dimensional array of post-select background
rate, stored in the :ref:`fits-arrays-bintable-hdu` format.

Required columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Reconstructed energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
    * Binning is often chosen with a square root scale,
      so that each ``THETA`` bin has equal solid angle,
      which means bins at the center of the field of view
      have smaller width ``THETA_HI - THETA_LO``.
* ``BKG`` -- ndim: 2, unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.

Recommended axis order: ``ENERGY``, ``THETA``

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'BKG'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'BKG_2D'

Example data file: TODO

.. _bkg_3d:

``bkg_3d``
----------

The ``bkg_3d`` format contains a 3-dimensional array of post-select background
rate, stored in the :ref:`fits-arrays-bintable-hdu` format.

Required columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Reconstructed energy axis
* ``DETX_LO``, ``DETX_HI``, ``DETY_LO``, ``DETY_HI`` -- ndim: 1, unit: deg
    * Field of view coordinates binning, see :ref:`coords-fov`
* ``BKG`` -- ndim: 3, unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.

Recommended axis order: ``ENERGY``, ``DETX``, ``DETY``

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'BKG'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'BKG_3D'

Example data file: TODO
