.. include:: ../../references.txt

.. _healpix:

This page describes data format conventions for FITS binned data and model
representations pixelized with the `HEALPix algorithm`_.  

ST HEALPix Formats
==================

This section describes HEALPix format conventions currently used
within the Fermi Science Tools (STs).  The ST HEALPix format is used
for representing maps and cubes of both integral and differential
quantities including:

* Photon count maps and cubes (generated with *gtbin*).
* Exposure cubes (generated with *gtexpcube2*).
* Source maps -- product of exposure cube with instrument response in
  spatial dimension (generated with *gtsrcmaps*).

The format uses a ``SKYMAP`` BINTABLE for storing pixel amplitudes.
For cubes an additional BINTABLE is used to store bin edges
(``EBOUNDS``) for integral quantities or bin centers (``ENERGIES``)
for differential quantities.  Note that 2D maps are treated as cubes
with a single energy plane and can be accomodated by all of the
formats described here.
  
There are five different indexing conventions for mapping table
entries in the BINTABLE to a HEALPix pixel number.  The convention
used in a given HDU is designated by the ``INDXSCHM`` header keyword:

* **IMPLICIT**: The row to pixel mapping is determined implicitly from
  the row number.  The row number corresponds to the HEALPix pixel
  number.
* **EXPLICIT**: The row to pixel mapping is determined explicitly from
  the ``PIX`` column.  This can be used to define maps or cubes that
  only encompass a partial region of the sky.
* **EXPLICIT_EDEP**: Same as **EXPLICIT** convention but with a
  variable number of pixels in each energy plane.  
* **SPARSE**: The row to pixel mapping is determined explicitly from the
  ``IDX`` column.  This convention can be used to represent maps that
  have a different geometry in each energy plane.
* **SPARSE_EDEP**: Same as **SPARSE** convention but the number of
  pixels in each energy plane can be variable.


Header Keyword
--------------

* ``INDXSCHM`` : Indexing scheme.  Can be one of
  ``IMPLICIT``, ``EXPLICIT``, ``EXPLICIT_EDEP``, ``SPARSE``,
  ``SPARSE_EDEP``.
* ``HPXREGION``, **optional**
  * Region string for the geometric selection that was used to
  construct a partial-sky map.  See :ref:`hpxregion` for additional
  details.
* ``ORDERING``
  * HEALPix ordering scheme.   Can be ``NESTED`` or ``RING``.
* ``COORDSYS`` : Map coordinate system.  Can be ``CEL`` (celestial coordinates) or ``GAL`` (galactic coordinates).
* ``ORDER`` : Healpix order.  ``NSIDE`` is 2 ** ``ORDER``.
* ``NSIDE`` : Number of healpix pixels per side. 

.. _hpxregion:
  
HEALPix Region String
---------------------

For partial-sky maps that correspond to a particular geometric
selection one can optionally specify the selection that was used in
constructing the map with the ``HPXREGION`` header keyword.  The
following region strings are supported:

* DISC(LON,LAT,RADIUS): A circular selection centered on the
  coordinates (LON,LAT) with radius RADIUS with all quantities given
  in degrees.  A pixel is included in the selection if its center is
  encompassed by the circle.

* DISCINC(LON,LAT,RADIUS): A circular selection centered on the
  coordinates (LON,LAT) with radius RADIUS with all quantities given
  in degrees.  A pixel is included in the selection if any part of it
  is encompassed by the circle.

* HPXPIXEL(ORDER,PIX): A selection encompassing all pixels contained
  in the HEALPix pixel of order ORDER and index PIX.
  
.. _ebounds_table:
   
EBOUNDS Table
-------------

The EBOUNDS HDU is a BINTABLE with 1 row per energy bin and the
following columns.  

Columns
~~~~~~~

* ``CHANNEL``, ndim: 1
* ``E_MIN``, ndim: 1, unit: keV,
    * Dimension: nebins
* ``E_MAX``, ndim: 1, unit: keV,
    * Dimension: nebins
* ``ORDER`` -- ndim: 1,
    * Dimension: nebins
    * Order of the HEALPix pixelization in each energy plane.
      Onlyrequired for energy-dependent pixelization formats
      (``EXPLICIT_EDEP`` and ``SPARSE_EDEP``).
    
IMPLICIT SKYMAP Table
---------------------

HDUS
~~~~

* ``SKYMAP``
* ``EBOUNDS``

SKYMAP Columns
~~~~~~~~~~~~~~

* ``CHANNEL{BIN_IDX}`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in energy plane ``{BIN_IDX}``.  

EXPLICIT SKYMAP Table
---------------------

HDUS
~~~~

* ``SKYMAP``
* ``EBOUNDS``

SKYMAP Columns
~~~~~~~~~~~~~~

* ``PIX`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in energy plane ``{BIN_IDX}``.

* ``CHANNEL{BIN_IDX}`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in pixel ``PIX`` and energy plane ``{BIN_IDX}``.  
      
SPARSE and SPARSE_EDEP Format
-----------------------------

The SPARSE and SPARSE_EDEP representations use a single index to
represent both pixel index and energy plane.  This allows one to
define energy-dependent partial-sky selections.  

HDUS
~~~~

* ``SKYMAP``
* ``EBOUNDS``

SKYMAP Columns
~~~~~~~~~~~~~~
      
* ``KEY`` -- ndim: 1, unit: None
    * Dimension: 1
    * Unrolled index representing both the healpix pixel and energy
      plane such that ``KEY`` = ``{BIN_IDX}`` x ``NPIX`` + ``PIX``
      where ``NPIX`` and ``PIX`` are the total number of HEALPix
      pixels and healpix index respectively.  For the SPARSE_EDEP
      representation ``NPIX`` is the sum of the number of pixels in
      each energy plane up to ``{BIN_IDX}``.

* ``VALUE`` -- ndim: 1, unit: None
    * Dimension: 1
    * Amplitude in pixel .  
      

