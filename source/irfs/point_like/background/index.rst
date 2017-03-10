.. include:: ../../../references.txt

.. _iact-point-background-format:

Background format
=================

In the case of point-like IRFs, background is calculated from... TODO

TODO: add figures of simultaneous background?

.. _point_bkg:

``point_bkg``
----------

The ``point_bkg`` format contains a 1-dimensional array of post-select background
rate, stored in the :ref:`fits-arrays-bintable-hdu` format.

Required columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``RAD_MAX`` -- ndim: 1, unit: deg
    * Radial cut applied to each energy bin to calculate the IRF
* ``BKG`` ndim: 1, unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.

Header keywords:

* ``HDU_CLASS = point_bkg``
* ``HDU_DOC = TODO``


Example data file: TODO
