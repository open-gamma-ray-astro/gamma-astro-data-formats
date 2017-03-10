.. include:: ../../references.txt

.. _point-irfs:

Point-like IRFs
===============


Allow excellent MC statistics for the generation of IRFs. They also allow
  to extract simultaneous background from reflected regions, significantly reducing the systematic uncertainty 
  of the background.

The instrument response function (IRF) formats currently in use
for imaging atmospheric Cherenkov telescopes (IACTs) are stored in FITS
binary tables using the "multidimensional array" convention (binary tables with a
single row and array columns) described at :ref:`fits-arrays-bintable-hdu`.

This format has been used for calibration data and IRF of X-ray instruments,
as well as for the IRFs that are distributed with the Fermi-LAT science tools.
In order to support point-like IRFs, describing instrument response for a given 
region of interest, this format has been extended closely following 
previous conventions.

At the moment (November 2015), this format is used by H.E.S.S., MAGIC and
VERITAS and supported by Gammapy and Gammalib and is being proposed for
DL3 IRFs (i.e. the format distributed to end users and used by the science tools
for CTA).

Here we specify the IRFs in use for IACT data.

.. _point-irf-axes:

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

In the case of fully enclosed IRFs:

* The energy-dependent radius of the selected region of interest should be ``RAD_MAX``  
   
The IRF format specifications mention a recommended axis format and axis units.
But tools should not depend on this and instead:

* Use the axis order specified by the ``CREF`` header keyword (see :ref:`fits-arrays-bintable-hdu`)
* Use the axis unit specified by the ``CUNIT`` header keywords (see :ref:`fits-arrays-bintable-hdu`)

.. _point-specific-irfs:

Specific IRFs
-------------

.. toctree::

   effective_area/index
   energy_dispersion/index
   background/index
