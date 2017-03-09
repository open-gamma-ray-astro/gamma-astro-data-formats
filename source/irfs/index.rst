.. include:: ../references.txt

.. _iact-irfs:

IACT IRFs
=========

The instrument response function (IRF) formats currently in use
for imaging atmospheric Cherenkov telescopes (IACTs) are stored in FITS
binary tables using the "multidimensional array" convention (binary tables with a
single row and array columns) described at :ref:`fits-arrays-bintable-hdu`.

This format has been used for calibration data and IRF of X-ray instruments,
as well as for the IRFs that are distributed with the Fermi-LAT science tools.

BLAH BLAH BLAH why we need 2 types of IRFs: full-enclosure IRFs and point-like IRFs.

* Full-enclosure IRFs: contain the instrument response for the whole field of view (FoV) of the instrument.
  Storing such IRFs allow the scientific analysis of any source within the instrument FoV, with no prior 
  assumption on its position. Given the limitation in computational resources, these IRFs generally lack sufficient
  MC event statistics to provide the best instrument response estimation possible for a given FoV position.
 
* Point-like IRFs: contain the instrument response for a given point within the FoV, which restricts their
  use to that specific position. Allow excellent MC statistics for the generation of IRFs. They also allow
  to extract simultaneous background from reflected regions, significantly reducing the systematic uncertainty 
  of the background.


At the moment (November 2015), this format is used by H.E.S.S., MAGIC and
VERITAS and supported by Gammapy and Gammalib and is being proposed for
DL3 IRFs (i.e. the format distributed to end users and used by the science tools
for CTA).


.. toctree::
   :maxdepth: 1
   
   full_enclosure/index  
   point_like/index
  
  
   
