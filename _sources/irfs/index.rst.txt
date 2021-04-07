.. include:: ../references.txt

.. _iact-irf:

IACT IRFs
=========

The instrument response function (IRF) format currently in use
for imaging atmospheric Cherenkov telescopes (IACTs) are stored in FITS
binary tables using the "multidimensional array" convention (binary tables with a
single row and array columns) described at :ref:`fits-arrays-bintable-hdu`. 
This format has been used for calibration data and IRF of X-ray instruments,
as well as for the IRFs that are distributed with the Fermi-LAT science tools.

Two different approaches are used to store the IRF of IACTs:

* Full-enclosure IRF: all IRF components are stored as a function of the offset with respect to the source 
  position.
 
* Point-like IRF: IRF components are calculated after applying a cut in direction offset. This format has been 
  used by the current generation of IACTs to perform spectral analysis and light curves.

At the moment (November 2015), this format is used by H.E.S.S., MAGIC and
VERITAS and supported by Gammapy and Gammalib and is being proposed for
DL3 IRF (i.e. the format distributed to end users and used by the science tools
for CTA).

.. toctree::
   :maxdepth: 1
   
   irf_components/index   
   irf_axes/index
   full_enclosure/index  
   point_like/index
  
  
   
