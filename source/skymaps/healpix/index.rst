.. include:: ../../references.txt

.. _healpix:

This page describes data format conventions for FITS binned data and model
representations pixelized with the `HEALPix algorithm`_.  

HEALPix Formats
===============

This section describes a proposal for HEALPix format conventions which
is based on the format currently used within the Fermi Science Tools
(STs).  This format is intended for representing maps and cubes
of both integral and differential quantities including:

* Photon count maps and cubes (e.g. as generated with with *gtbin*).
* Exposure cubes (e.g. as generated with *gtexpcube2*).
* Source maps -- product of exposure cube with instrument response in
  spatial dimension (e.g. as generated with *gtsrcmaps*).
* Model maps and cubes (the IEM and other diffuse components).

The format uses a ``SKYMAP`` BINTABLE for storing pixel amplitudes and
a separate BINTABLE to store energy bin edges for integral quantities
(``EBOUNDS``) or bin centers for differential quantities
(``ENERGIES``).  Note that 2D maps are treated as cubes with a single
energy plane and can be accomodated by all of the formats described
here.
  
There are four primary HEALPix map formats which use different table
structures for mapping table entries to HEALPix pixel and energy plane:

* :ref:`hpx_implicit`: The row to pixel mapping is determined implicitly from
  the row number.  The row number corresponds to the HEALPix pixel
  number.
* :ref:`hpx_explicit`: The row to pixel mapping is determined explicitly from
  the ``PIX`` column.  This can be used to define maps or cubes that
  only encompass a partial region of the sky.
* :ref:`hpx_explicit_edep`: Same as :ref:`hpx_explicit` convention but
  with a different pixel size (HEALPix order) in each energy plane.
* :ref:`hpx_sparse`: The row to pixel mapping is determined explicitly
  from the ``IDX`` column which is an unrolled index for both pixel
  and energy plane.  This format can be used to represent maps that
  have a different spatial geometry in each energy plane and also
  supports energy-dependent pixel size.

Note that there are variations of these primary formats which use
different conventions for column, HDU, and header keywords names.  The
``HPX_CONV`` keyword defines a specific mapping between the names used
here and in these other formats:

* ``FGST_CCUBE``
* ``FGST_LTCUBE``
* ``FGST_BEXPCUBE``
* ``FGST_SRCMAP``
* ``FGST_TEMPLATE``
* ``FGST_SRCMAP_SPARSE``
* ``GALPROP``
* ``GALPROP2``
  
Header Keywords
---------------

This section lists the keywords that should be written to the
``SKYMAP`` BINTABLE HDU header.  These keywords define the pixel size
and ordering scheme that was used to construct the HEALPix map.

* ``PIXTYPE``, type: string
    * Should be set to ``HEALPIX``.
* ``INDXSCHM``, type: string
    * Indexing scheme.  Can be one of ``IMPLICIT``, ``EXPLICIT``,
      ``EXPLICIT_EDEP``, ``SPARSE``, ``SPARSE_EDEP``.  If this keyword
      is not provided then the ``IMPLICIT`` indexing scheme will be
      assumed.
* ``ORDERING``, type: string
    * HEALPix ordering scheme.   Can be ``NESTED`` or ``RING``.
* ``COORDSYS``, type: string
    * Map coordinate system.  Can be ``CEL`` (celestial coordinates) or ``GAL`` (galactic coordinates).
* ``ORDER``, type: int
    * Healpix order.  ``NSIDE`` is 2 ** ``ORDER``.  For
      ``EXPLICIT_EDEP`` and ``SPARSE_EDEP`` this keyword is superseded
      by the ``ORDER`` column in the ``EBOUNDS`` table.
* ``NSIDE``, type: int
    * Number of healpix pixels per side.
* ``FIRSTPIX``, type: int
* ``LASTPIX``, type: int
* ``HPX_REG``, type: string, **optional**
    * Region string for the geometric selection that was used to
      construct a partial-sky map.  See :ref:`hpx_region_string` for
      additional details.
* ``HPX_CONV``, type: string, **optional**
    * Convention for HEALPix format.

.. _hpx_region_string:
  
HEALPix Region String
---------------------

For partial-sky maps that correspond to a particular geometric
selection one can optionally specify the selection that was used in
constructing the map with the ``HPX_REG`` header keyword.  The
following region strings are supported:

* ``DISK({LON},{LAT},{RADIUS})``: A circular selection centered on the
  coordinates (``{LON}``, ``{LAT}``) with radius ``{RADIUS}`` with all
  quantities given in degrees.  A pixel is included in the selection
  if its center is within ``{RADIUS}`` deg of coordinates (``{LON}``,
  ``{LAT}``).

* ``DISK_INC({LON},{LAT},{RADIUS})``: A circular selection centered
  on the coordinates (``{LON}``, ``{LAT}``) with radius ``{RADIUS}``
  with all quantities given in degrees.  A pixel is included in the
  selection if any part of it is encompassed by the circle.

* ``HPX_PIXEL({ORDERING},{ORDER},{PIX})``: A selection encompassing
  all pixels contained in the HEALPix pixel of the given pixelization
  where ordering is ``{ORDERING}`` (i.e. ``NESTED`` or ``RING``),
  order is ``{ORDER}``, and pixel index is ``{PIX}``.


.. _hpx_sample_files:
  
Sample Files
------------

* Spatial-sky Counts Cube (EXPLICIT Format): :download:`FITS <hpx_ccube_explicit.fits>`
* Spatial-sky Counts Map (EXPLICIT Format)::download:`FITS <hpx_cmap_explicit.fits>`
  
.. _hpx_ebounds_table:
   
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
      Only required for energy-dependent pixelization formats
      (``EXPLICIT_EDEP`` and ``SPARSE_EDEP``).

.. _hpx_implicit:
      
IMPLICIT Format
---------------

The IMPLICIT format defines a one-to-one mapping between table row and
HEALPix pixel index.  Each energy plane is represented by a separate
column (``CHANNEL0``, ``CHANNEL1``, etc.).  This format can only be
used for all-sky maps.

HDUS
~~~~

* ``SKYMAP``
* ``EBOUNDS``

HEADER
~~~~~~

* ``INDXSCHM`` : ``IMPLICIT``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``CHANNEL{BIN_IDX}`` -- ndim: 1
    * Dimension: nrows
    * Amplitude in energy plane ``{BIN_IDX}``.  The HEALPix pixel
      index is determined from the table row.

.. _hpx_explicit:
      
EXPLICIT Format
---------------

The EXPLICIT format uses an additional ``PIX`` column to explicitly
define the pixel number corresponding to each table row.  Each energy
plane is represented by a separate column (``CHANNEL0``, ``CHANNEL1``,
etc.).  This format can be used for both all-sky and partial-sky maps.

HDUS
~~~~

* ``SKYMAP``
* ``EBOUNDS``

HEADER
~~~~~~

* ``INDXSCHM`` : ``EXPLICIT``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``PIX`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Spatial pixel index.  This index is common to all energy planes.

* ``CHANNEL{BIN_IDX}`` -- ndim: 1
    * Dimension: nrows
    * Amplitude in HEALPix pixel ``PIX`` and energy plane
      ``{BIN_IDX}``.

.. _hpx_explicit_edep:
      
EXPLICIT_EDEP Format
--------------------

HDUS
~~~~

* ``SKYMAP``
* ``EBOUNDS``

HEADER
~~~~~~

* ``INDXSCHM`` : ``EXPLICIT_EDEP``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``PIX{BIN_IDX}`` -- ndim: 2, unit: None
    * Dimension: 1 x npix
    * Spatial pixel index in energy plane ``{BIN_IDX}``.

* ``CHANNEL{BIN_IDX}`` -- ndim: 2, unit: None
    * Dimension: 1 x npix
    * Amplitude in pixel ``PIX{BIN_IDX}`` and energy plane ``{BIN_IDX}``.  
      
.. _hpx_sparse:
      
SPARSE Format
-------------

The SPARSE format uses a single index to represent indices for pixel
and energy plane.  This allows one to define energy-dependent
partial-sky selections.  This format also supports energy-dependent
pixel size by including an ``ORDER`` column in the ``EBOUNDS`` table
and setting ``INDXSCHM`` to ``SPARSE_EDEP``.

HDUS
~~~~

* ``SKYMAP``
* ``EBOUNDS``

HEADER
~~~~~~

* ``INDXSCHM`` : ``SPARSE`` or ``SPARSE_EDEP``
  
SKYMAP Columns
~~~~~~~~~~~~~~
      
* ``KEY`` -- ndim: 2, unit: None
    * Dimension: 1 x npix
    * Unrolled index representing both the healpix pixel and energy
      plane such that ``KEY`` = ``{BIN_IDX}`` x ``NPIX`` + ``PIX``
      where ``NPIX`` and ``PIX`` are the total number of HEALPix
      pixels and healpix index respectively.  For maps with
      energy-dependent pixel size ``NPIX`` is the sum of the number of
      pixels in each energy plane up to ``{BIN_IDX}``.

* ``VALUE`` -- ndim: 2, unit: None
    * Dimension: 1 x npix
    * Amplitude in pixel indexed by ``KEY``.  
      

