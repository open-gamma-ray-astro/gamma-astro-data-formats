.. include:: ../../references.txt

.. _full-enclosure-irfs:

Full-enclosure IRFs
===================

Full-enclosure IRF format has been used for calibration data and IRF of 
X-ray instruments, as well as for the IRFs that are distributed with the Fermi-LAT 
science tools. 

These IRFs are calculated for the whole field of view (FoV) of the instrument, with no 
prior assumption on the source position, allowing the analysis of any point-like 
or diffuse source within the instrument FoV. 

As discussed within the :ref:`iact-irf` section, IACTs have a couple of limitations to calculate
full-enclosure IRFs:

* As simulated gamma-ray events are distributed through the whole FoV, the IRFs may lack enough statistics 
  (for instance, to properly calculate the energy migration or the PSF tails for high energy bins) 
* Full-enclosure IRFs require a precise background model for the whole FoV, a rather complicated task for 
  IACTs (in highly populated areas or regions with diffuse signals larger than the instrument FoV).

Any full-enclosure IRF component should contain the header keyword: 

* ``HDU_CLAS3 = full-enclosure``

.. toctree::

   effective_area/index
   energy_dispersion/index
   psf/index
   background/index
