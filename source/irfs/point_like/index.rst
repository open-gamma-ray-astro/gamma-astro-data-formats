.. include:: ../../references.txt

.. _point-irfs:

Point-like IRFs
===============

Point-like IRFs has been classically used within the IACT community. Each IRF component is calculated from the
events surviving an energy dependent directional cut around the assumed source position. 

The format of each point-like IRF component is analog to the ones already described within the full enclosure 
IRF specifications (see :ref:`full-enclosure-irfs`:), with certain differences listed in this section.

Any point-like IRF component should contain the header keyword: 

* ``HDU_CLAS3 = POINT-LIKE``

``RAD_MAX`` column
------------------

In addition, binary tables should contain the ``RAD_MAX`` column, containing the radial cut applied
to calculate the IRF component (unit: deg). As this value is allowed to change as a function of the energy and field 
of view (FoV) coordinates, the dimension of this column is equal to: 

* -- ndim: 2 in case that the FoV coordinate is ``THETA``

* -- ndim: 3 in case that the FoV coordinates are ``DETX`` and ``DETY`` 

As an example, the format of a point-like effective area (as a function of the true energy) is shown below. 

Example: point-like effective Area vs true energy
-------------------------------------------------

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1
    * Field of view offset axis
* ``RAD_MAX`` -- ndim: 2, unit: deg
    * Radial cut applied to calculate the IRF component
* ``EFFAREA`` -- ndim: 2
    * Effective area value as a function of true energy

Recommended axis order: ``ENERGY``, ``THETA``, ``RAD_MAX``

Header keywords:

* ``OBS_ID`` type: int
    * Observation ID, run number
* ``LO_THRES`` type: float, unit: TeV
    * Low energy threshold
* ``HI_THRES`` type: float, unit: TeV
    * High energy threshold
    
And as described in :ref:`hduclass`:
    
* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EFF_AREA'
* ``HDUCLAS3`` = 'POINT-LIKE'
* ``HDUCLAS4`` = 'AEFF_2D'
