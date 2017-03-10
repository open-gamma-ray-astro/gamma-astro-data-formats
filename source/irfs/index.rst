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

Unlike spaceborne instruments, IACT IRFs are affected by fast-changing parameters (weather, atmospheric 
density profile, night-sky background). The absence of these changing conditions in the MC is the main source of 
systematic uncertainty for the current generation of IACTs. In addition, IRF uncertainty is limited by the
statistics of generated MC events, requiring large computational resources. 

Given the large amount of parameters to be included within the simulations and the limited resources, two 
different approaches are generally used to calculate the IACTs response:

* Full-enclosure IRFs: contain the instrument response for the whole field of view (FoV) of the instrument.
  Storing such IRFs allow the scientific analysis of any source within the instrument FoV, with no prior 
  assumption on its position. Require simulation of gamma rays over the whole instrument field of view
 
* Point-like IRFs: contain the instrument response for a given point within the FoV, which restricts their
  use to that specific position. All simulated gamma rays come from a single point within the FoV, significantly
  reducing required resources to reach a given IRF uncertainty level


At the moment (November 2015), this format is used by H.E.S.S., MAGIC and
VERITAS and supported by Gammapy and Gammalib and is being proposed for
DL3 IRFs (i.e. the format distributed to end users and used by the science tools
for CTA).


.. toctree::
   :maxdepth: 1
   
   full_enclosure/index  
   point_like/index
  
  
   
