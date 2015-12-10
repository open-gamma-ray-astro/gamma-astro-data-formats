.. include:: ../../references.txt

.. _bkg:

Background
==========

One method of background modeling for IACTs is to construct spatial and / or
spectral model templates of the irreducible cosmic ray background for a given
reconstruction and gamma-hadron separation from :ref:`glossary-obs-off`. These
templates can then be used as an ingredient to model the background in
observations that contain gamma-ray emission of interest, or to compute the
sensitivity for that set of cuts.

Here we specify two formats for such background template models:

* ``bkg_2d`` models depend on ``ENERGY`` and ``THETA``, i.e. are radially symmetric.
* ``bkg_3d`` models depend on ``ENERGY`` and field of view coordinates ``DETX`` and ``DETY``.

.. note::

    Generating background models requires the construction of several
    intermediate products (counts and livetime histograms, both filled by cutting
    out exclusion regions around sources like AGN) to arrive at the models
    containing an absolute rate described here. At this time we don't specify a
    format for those intermediate formats.

.. note::

    Background models are sometimes considered an instrument response function
    (IRF) and sometimes not (e.g. when the background is estimated from different
    parts of the field of view for the same observation).

    Here we have the background format specifications listed under IRFs,
    simply because the storage format is very similar to the other IRFs
    (e.g. effective area) and we didn't want to introduce a new top-level
    section besides IRFs.

.. _bkg-2d:

bkg_2d format
-------------

The ``bkg_2d`` format contains a 2-dimensional array of post-select background
rate, stored in the :ref:`fits-arrays-bintable-hdu` format.

Header keywords:

* ``HDU_CLASS = bkg_2d``
* ``HDU_DOC = ???`` (TODO: https://github.com/gammapy/gamma-astro-data-formats/issues/10)

Columns:

* ``bkg`` unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.
* ``THETA_LO``, ``THETA_HI`` (deg)
    * Field of view offset from the pointing position binning, see :ref:`sky-coordinates-fov`
* ``ENERG_LO``, ``ENERG_HI`` (TeV)
    * Energy binning, see TODO

TODO: explain a bit about the THETA axis, i.e. that bins are usually
chosen to have a constant solid angle per bin, i.e. with sqrt spacing.

Example data file: TODO

.. _bkg-3d:

bkg_3d format
-------------

The ``bkg_3d`` format contains a 3-dimensional array of post-select background
rate, stored in the :ref:`fits-arrays-bintable-hdu` format.

TODO: maybe we should we use TeV as units, since we use this for IACTs and also
store energy in TeV?

Columns:

* ``bkg`` unit: s^-1 MeV^-1 sr^-1
    * Absolute post-select background rate
      (expected background per time, energy and solid angle).
    * Note that this is not a "flux" or "surface brightness".
      This is already a count rate, it doesn't need to be multiplied with
      effective area to obtain predicted counts, like gamma-ray flux and
      surface brightness models do.
* ``DETX_LO``, ``DETX_HI``, ``DETY_LO``, ``DETY_HI`` (deg)
    * Field of view coordinates binning, see :ref:`sky-coordinates-fov`
* ``ENERG_LO``, ``ENERG_HI`` (TeV)
    * Energy binning, see TODO

Header keywords:

* ``HDU_CLASS = bkg_3d``
* ``HDU_DOC = ???`` (TODO: https://github.com/gammapy/gamma-astro-data-formats/issues/10)

Example data file: TODO
