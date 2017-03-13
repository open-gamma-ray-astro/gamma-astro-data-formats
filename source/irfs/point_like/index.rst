.. include:: ../../references.txt

.. _point-irfs:

Point-like IRFs
===============

Point-like IRFs has been classically used within the IACT community. Each IRF component is calculated from the
events surviving an energy dependent directional cut around the assumed source position. 

Any point-like IRF component should contain the header keyword: 

* ``HDU_CLAS2 = point-like``

From here on, the specific format of each IRF component: 

.. toctree::

   effective_area/index
   energy_dispersion/index
   background/index
