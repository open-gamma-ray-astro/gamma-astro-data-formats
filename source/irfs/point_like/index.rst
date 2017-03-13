.. include:: ../../references.txt

.. _point-irfs:

Point-like IRFs
===============

Point-like IRFs has been classically used within the IACT community. These IRFs are calculated for 
a given position within the field of view (FoV) of the instrument, with a directional cut already applied
to calculate each IRF component. 

As discussed within the :ref:`iact-irf` section, although the point-like IRF format has the obvious limitation 
of only describing the instrument response to a given point-like source within the FoV, it also provides certain 
benefits:

* Lower IRF uncertainty due to higher MC statistics
* Simultaneous background determination extracted from a given number of reflected regions within the
  FoV. This method allows lower systematic uncertainty on the background estimation 

Any point-like IRF component should contain the header keyword: 

* ``HDU_CLAS3 = point-like``

From here on, the specific format of each IRF component: 

.. toctree::

   effective_area/index
   energy_dispersion/index
   background/index
