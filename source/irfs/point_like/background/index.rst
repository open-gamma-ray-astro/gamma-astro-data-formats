.. include:: ../../../references.txt

.. _iact-point-background-format:

Background format
=================

Here we specify the format for the background of a point-like IRF:

.. _bkg_2d_point:

``bkg_2d_point``
----------------

The ``point_bkg`` format contains a 1-dimensional array of post-select background
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
    * Radial cut applied to each energy bin to calculate the IRF component
* ``BKG`` ndim: 2, unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.

Header keywords:

* ``HDUCLAS3`` type: string
    * Secondary extension class (option: 'BKG_2D_POINT').
* ``HDU_DOC = TODO``


Example data file: TODO
