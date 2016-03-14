.. include:: ../references.txt

.. _iact-irfs:

IACT IRFs
=========

The instrument response function (IRF) formats currently in use
for imaging atmospheric Cherenkov telescopes (IACTs) are stored in FITS
binary tables using the "multidimentional array" convention (binary tables with a
single row and array columns) described at :ref:`fits-arrays-bintable-hdu`.

This format has been used for calibration data and IRF of X-ray instruments,
as well as for the IRFs that are distributed with the Fermi-LAT science tools.

At the moment (November 2015), this format is used by H.E.S.S. and
VERITAS and supported by Gammapy and Gammalib and is being proposed for
DL3 IRFs (i.e. the format distributed to end users and used by the science tools
for CTA).
Note that a different format has been proposed for CTA to serialise multidimensional
arrays and axis information: http://adsabs.harvard.edu/abs/2015arXiv150807437W
As far as we know, this format is currently not supported by any analysis package.

Here we specify the IRFs in use for IACT data.

IRF axes
--------

Most IRFs are dependent on parameters, and the 1-dim. parameter arrays are
stored in columns. The following names are recommended:

* For energy grids, see `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_003/cal_gen_92_003.html#tth_sEc7>`__
  for basic recommendations. Column names should be ``ENERGY`` or ``ENERG_LO``, ``ENERG_HI``
  because that is used (consistently I think) for OGIP and Fermi-LAT.
  For separate HDUs, the extension names should be ``ENERGIES`` or ``EBOUNDS`` (used by Fermi-LAT consistently).
* Sky coordinates should be called ``RA``, ``DEC``, ``GLON``, ``GLAT``, ``ALT``, ``AZ``.
* Field of view coordinates ``DETX``, ``DETY`` or ``THETA``, ``PHI`` for offset and azimuth angle in the field of view.
* Offset wrt. the source position should be called ``RAD`` (this is what the OGIP PSF formats use).

The IRF format specs mention a recommended axis format and axis units.
But tools should not depend on this and instead:

* Use the axis order specified by the ``CREF`` header keyword (see :ref:`fits-arrays-bintable-hdu`)
* Use the axis unit specifiec by the ``CUNIT`` header keywords (see :ref:`fits-arrays-bintable-hdu`)

Specific IRFs
-------------

.. toctree::

   effective_area/index
   energy_dispersion/index
   psf/index
   background/index
