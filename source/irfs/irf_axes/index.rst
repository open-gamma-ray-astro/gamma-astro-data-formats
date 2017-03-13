.. include:: ../../references.txt

.. _irf-axes:

IRF axes
========

Most IRFs are dependent on parameters, and the 1-dimensional parameter arrays are
stored in columns. The following names are recommended:

* For energy grids, see `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_003/cal_gen_92_003.html#tth_sEc7>`__
  for basic recommendations. Column names should be ``ENERGY`` or ``ENERG_LO``, ``ENERG_HI``
  because that is used (consistently I think) for OGIP and Fermi-LAT.
  For separate HDUs, the extension names should be ``ENERGIES`` or ``EBOUNDS`` (used by Fermi-LAT consistently).
* Sky coordinates should be called ``RA``, ``DEC``, ``GLON``, ``GLAT``, ``ALT``, ``AZ``.
* Field of view coordinates ``DETX``, ``DETY`` or ``THETA``, ``PHI`` for offset and azimuth angle in the field of view.
* Offset wrt. the source position should be called ``RAD`` (this is what the OGIP PSF formats use).

In the specific case of point-like IRFs:

* The energy-dependent radius of the selected region of interest should be ``RAD_MAX``
   
The IRF format specifications mention a recommended axis format and axis units.
But tools should not depend on this and instead:

* Use the axis order specified by the ``CREF`` header keyword (see :ref:`fits-arrays-bintable-hdu`)
* Use the axis unit specified by the ``CUNIT`` header keywords (see :ref:`fits-arrays-bintable-hdu`)

 
