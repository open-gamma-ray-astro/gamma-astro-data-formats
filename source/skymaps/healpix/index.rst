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

* Counts maps and cubes (generated with *gtbin*).
* Exposure cubes (generated with *gtexpcube2*).
* Source maps -- product of exposure with instrument response in
  spatial dimension (generated with *gtsrcmaps*).

The format uses a FITS BINTABLE for representing pixel amplitudes and
an EBOUNDS or ENERGIES table for representing bin edges/centers.
  
There are three different indexing conventions for mapping a row in
the BINTABLE to a HEALPix pixel number:

* **Implicit**: The row to pixel mapping is determined implicitly from
  the row number.  The row number corresponds to the HEALPix pixel
  number.
* **Explicit**: The row to pixel mapping is determined explicitly from
  the ``PIX`` column.  This can be used to define maps or cubes that
  only encompass a partial region of the sky.
* **Sparse**: The row to pixel mapping is determined explicitly from the
  ``IDX`` column.  This convention can be used to represent maps that
  have a different geometry in each energy plane.

All three conventions require the existence of two tables:

* ``SKYMAP`` : Table with amplitude in each pixel.
* ``EBOUNDS`` or ``ENERGIES``: Table with energy bin edges or bin centers.
  

Header Keyword
--------------
* ``INDXSCHM`` : String describing the indexing scheme.  Can be one of ``IMPLICIT``, ``EXPLICIT``, or ``SPARSE``.
* ``HPXREGION`` : Region string for the geometric selection that was used to construct a partial-sky map. 
* ``ORDERING`` : HEALPix ordering scheme.   Can be ``NESTED`` or ``RING``.
* ``COORDSYS`` : Map coordinate system.  Can be ``CEL`` (celestial coordinates) or ``GAL`` (galactic coordinates).
* ``ORDER`` : Healpix order.  ``NSIDE`` is 2 ** ``ORDER``.
* ``NSIDE`` : Number of healpix pixels per side. 

Implicit SKYMAP Table
---------------------

Columns
~~~~~~~

* ``CHANNEL{BIN_IDX}`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in energy plane ``{BIN_IDX}``.  


Explicit SKYMAP Table
---------------------

Columns
~~~~~~~

* ``PIX`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in energy plane ``{BIN_IDX}``.

* ``CHANNEL{BIN_IDX}`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in pixel ``PIX`` and energy plane ``{BIN_IDX}``.  


Sparse SKYMAP Table
-------------------

The sparse representation.

Columns
~~~~~~~
      
* ``KEY`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Unrolled index representing both the healpix pixel and energy
      plane such that ``KEY`` = ``{BIN_IDX}`` x ``NPIX`` + ``PIX``
      where ``NPIX`` and ``PIX`` are the total number of HEALPix
      pixels and healpix index respectively.

* ``VALUE`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in pixel .  
      

