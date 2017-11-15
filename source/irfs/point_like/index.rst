.. include:: ../../references.txt

.. _point-irfs:

Point-like IRFs
===============

Point-like IRFs has been classically used within the IACT community. Each IRF component is calculated from the
events surviving an energy dependent directional cut around the assumed source position. 

The format of each point-like IRF component is analog to the ones already described within the full enclosure 
IRF specifications (see :ref:`full-enclosure-irfs`), with certain differences listed in this section.

Any point-like IRF component should contain the header keyword: 

* ``HDU_CLAS3 = POINT-LIKE``

``RAD_MAX``
-----------

In addition to the IRFs, the actual directional cut applied to the data needs to be stored. This cut is allowed 
to be constant and variable along several axes, with a slightly different format.

In case the angular cut is constant along the energy and FoV, an additional header keyword may be added to the 
IRF HDU:

Header keyword:

* ``RAD_MAX`` type: float, unit: deg
    * Radius of the directional cut applied to calculate the IRF, in degrees.

If this keyword is present, the point-like IRF will assume the directional cut is constant over all axes. In case 
the angular cut is variable along any axis (reconstructed energy or FoV), an additional HDU is required to store 
these values. Note any DL3 file with a point-like IRF (with ``HDU_CLAS3`` = POINT-LIKE) that has no ``RAD_MAX`` 
keyword within the HDU should have this additional HDU.
 
In case the directional cut is variable with energy or the FoV, point-like IRFs require this additional binary 
table. It stores the values of ``RAD_MAX`` as a function of the reconstructed energy and camera offset following 
:ref:`fits-arrays-bintable-hdu` format.

Depending on the FoV coordinates employed, the binary table is allowed to have two different formats.

``rad_max_2d``
--------------

The ``rad_max_2d`` format contains a 2-dimensional array of directional cut values, stored in the 
:ref:`fits-arrays-bintable-hdu` format.

Required columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Reconstructed energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
    * Binning is often chosen with a square root scale,
      so that each ``THETA`` bin has equal solid angle,
      which means bins at the center of the field of view
      have smaller width ``THETA_HI - THETA_LO``.
* ``RAD_MAX`` -- ndim: 2, unit: deg
    * Radius of the directional cut applied to calculate the IRF, in degrees.

Recommended axis order: ``ENERGY``, ``THETA``, ``RAD_MAX``

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'RAD_MAX'
* ``HDUCLAS3`` = 'POINT-LIKE'
* ``HDUCLAS4`` = 'RAD_MAX_2D'


``rad_max_3d``
--------------

The ``rad_max_3d`` format contains a 3-dimensional array of directional cut values, stored in the 
:ref:`fits-arrays-bintable-hdu` format.

Required columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Reconstructed energy axis
* ``DETX_LO``, ``DETX_HI``, ``DETY_LO``, ``DETY_HI`` -- ndim: 1, unit: deg
    * Field of view coordinates binning, see :ref:`coords-fov`
* ``RAD_MAX`` -- ndim: 2, unit: deg
    * Radius of the directional cut applied to calculate the IRF, in degrees.

Recommended axis order: ``ENERGY``, ``DETX``, ``DETY``, ``RAD_MAX``

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'RAD_MAX'
* ``HDUCLAS3`` = 'POINT-LIKE'
* ``HDUCLAS4`` = 'RAD_MAX_3D'
