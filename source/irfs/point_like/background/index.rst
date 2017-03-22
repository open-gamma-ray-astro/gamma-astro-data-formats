.. include:: ../../../references.txt

.. _iact-point-background-format:

Background format
=================

Here we specify two formats for the background of a point-like IRF:

* ``bkg_2d_point`` models depend on ``ENERGY`` and ``THETA``, i.e. are radially symmetric.
* ``bkg_3d_point`` models depend on ``ENERGY`` and field of view coordinates ``DETX`` and ``DETY``.

.. _bkg_2d_point:

``bkg_2d_point``
----------------

The ``bkg_2d_point`` format contains a 1-dimensional array of post-select background
rate, stored in the :ref:`fits-arrays-bintable-hdu` format.

Required columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
    * Binning is often chosen with a square root scale,
      so that each ``THETA`` bin has equal solid angle,
      which means bins at the center of the field of view
      have smaller width ``THETA_HI - THETA_LO``.
* ``RAD_MAX`` -- ndim: 2, unit: deg
    * Radial cut applied to calculate the IRF component
* ``BKG`` -- ndim: 2, unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.

Recommended axis order: ``ENERGY``, ``THETA``, ``RAD_MAX`` 

Header keywords:

* ``HDUCLAS1`` type: string
    * First extension class (option: 'RESPONSE').
* ``HDUCLAS2`` type: string
    * Second extension class (option: 'BKG').
* ``HDUCLAS3`` type: string
    * Third extension class (option: 'POINT-LIKE').
* ``HDUCLAS4`` type: string
    * Fourth extension class (option: 'bkg_2d').  
* ``HDU_DOC = TODO``

Example data file: TODO


.. _bkg_3d_point:

``bkg_3d_point``
----------------

The ``bkg_3d_point`` format contains a 3-dimensional array of post-select background
rate, stored in the :ref:`fits-arrays-bintable-hdu` format.

Required columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``DETX_LO``, ``DETX_HI``, ``DETY_LO``, ``DETY_HI`` -- ndim: 1, unit: deg
    * Field of view coordinates binning, see :ref:`coords-fov`
* ``RAD_MAX`` -- ndim: 3, unit: deg
    * Radial cut applied to calculate the IRF component
* ``BKG`` -- ndim: 3, unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.

Recommended axis order: ``ENERGY``, ``DETX``, ``DETY``, ``RAD_MAX`` 

Header keywords:

* ``HDUCLAS1`` type: string
    * First extension class (option: 'RESPONSE').
* ``HDUCLAS2`` type: string
    * Second extension class (option: 'BKG').
* ``HDUCLAS3`` type: string
    * Third extension class (option: 'POINT-LIKE').
* ``HDUCLAS4`` type: string
    * Fourth extension class (option: 'bkg_3d').  
* ``HDU_DOC = TODO``

Example data file: TODO

