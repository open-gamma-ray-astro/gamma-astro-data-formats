.. include:: ../../references.txt



This page describes data format conventions for FITS binned data and model
representations pixelized with the `HEALPix algorithm`_.  

.. _healpix_skymap:

HEALPix Formats
===============

This section describes a proposal for HEALPix format conventions which
is based on formats currently used within the Fermi Science Tools
(STs) and pointlike.  This format is intended for representing maps
and cubes of both integral and differential quantities including:

* Photon count maps and cubes (e.g. as generated with with *gtbin*).
* Exposure cubes (e.g. as generated with *gtexpcube2*).
* Source maps -- product of exposure with instrument response in
  spatial dimension (e.g. as generated with *gtsrcmaps*).
* Model maps and cubes (the Fermi IEM and other diffuse emission
  components).

The format defines a :ref:`hpx_skymap_table` for storing a sequence of
image slices (*bands*) and a :ref:`bands_hdu` to store the
geometry and coordinate mapping for each band.  A band can represent
any selection on non-spatial coordinates such as energy, time, or FoV
angle.  The most common use-case is a sequence of bands
representing energy bins (for counts maps) or energy nodes (for source
or model maps).

There are three primary HEALPix map formats which use different table
structures for mapping table entries to HEALPix pixel and band:

* :ref:`hpx_implicit`: The row to pixel mapping is determined implicitly from
  the row number.  The row number corresponds to the HEALPix pixel
  number.
* :ref:`hpx_explicit`: The row to pixel mapping is determined explicitly from
  the ``PIX`` column.  This can be used to define maps or cubes that
  only encompass a partial region of the sky.
* :ref:`hpx_local`: The row to pixel mapping is determined explicitly
  from the ``PIX`` column but with a local indexing scheme.  This can
  be used to define maps or cubes that only encompass a partial region
  of the sky.
* :ref:`hpx_sparse`: The row to pixel mapping is determined explicitly
  from the ``PIX`` column but with a variable number of pixels in each
  band.  This format can be used to represent maps that have a
  different spatial geometry in each band and also supports
  band-dependent pixel size.

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

.. _hpx_conventions:

Non-Standard HEALPix Conventions
--------------------------------
  
.. _hpx_sample_files:
  
Sample Files
------------

* All-sky Counts Cube (IMPLICIT Format): :download:`FITS <hpx_ccube_implicit.fits>`
* Partial-sky Counts Cube (EXPLICIT Format): :download:`FITS <hpx_ccube_explicit.fits>`
* Partial-sky Counts Map (EXPLICIT Format): :download:`FITS <hpx_cmap_explicit.fits>`
* Partial-sky Counts Cube (SPARSE Format w/ fixed NSIDE)::download:`FITS <hpx_ccube_sparse0.fits>`
* Partial-sky Counts Cube (SPARSE Format w/ variable NSIDE)::download:`FITS <hpx_ccube_sparse1.fits>`
  
.. _hpx_skymap_table:
   
SKYMAP HDU
----------

The SKYMAP table contains the map data and row-to-pixel mapping
formatted according to one of three indexing schemes specified by the
``INDXSCHM`` header keyword: :ref:`hpx_implicit`, :ref:`hpx_explicit`,
or :ref:`hpx_sparse`.  By convention if a file contains a single map
it is recommended to name the extension ``SKYMAP``.  For maps with
non-spatial dimensions an accompanying BANDS table must also be
defined (see :ref:`bands_hdu`).

Header Keywords
~~~~~~~~~~~~~~~

This section lists the keywords that should be written to the
SKYMAP BINTABLE header.  These keywords define the pixel size
and ordering scheme that was used to construct the HEALPix map.

* ``PIXTYPE``, type: string
    * Should be set to ``HEALPIX``.
* ``INDXSCHM``, type: string
    * Indexing scheme.  Can be one of ``IMPLICIT``, ``EXPLICIT``,
      ``SPARSE``.  If this keyword is not provided then the
      ``IMPLICIT`` indexing scheme will be assumed.
* ``ORDERING``, type: string
    * HEALPix ordering scheme.   Can be ``NESTED`` or ``RING``.
* ``COORDSYS``, type: string
    * Map coordinate system.  Can be ``CEL`` (celestial coordinates)
      or ``GAL`` (galactic coordinates).
* ``ORDER``, type: int
    * Healpix order.  ``ORDER`` = log2(``NSIDE``) if ``NSIDE`` is a
      power of 2 and -1 otherwise.  If the ``BANDS`` table is defined
      this keyword is superseded by the ``NSIDE`` column.
* ``NSIDE``, type: int
    * Number of healpix pixels per side.  If the ``BANDS`` table is defined
      this keyword is superseded by the ``NSIDE`` column.
* ``FIRSTPIX``, type: int
    * Index of first pixel in the map.
* ``LASTPIX``, type: int
    * Index of last pixel in the map.  
* ``HPX_REG``, type: string, **optional**
    * Region string for the geometric selection that was used to
      construct a partial-sky map.  See :ref:`hpx_region_string` for
      additional details.
* ``HPX_CONV``, type: string, **optional**
    * Convention for HEALPix format.  See :ref:`hpx_conventions` for
      additional details.
* ``AXCOLS{IDX}``, type: string
    * Comma-separated list of columns in the BANDS table corresponding
      to non-spatial dimension with zero-based index ``{IDX}``.  If
      there are two elements the columns should be interpreted as the
      lower and upper edges of each bin.  If there is a single element
      the column should be interpreted as the bin center.
* ``BANDSHDU``, type: string, **optional**  
    * Name of HDU containing the BANDS table.  If undefined the
      extension name should be ``EBOUNDS`` or ``ENERGIES``.  See
      :ref:`bands_hdu` for additional details.

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

  
.. _hpx_implicit:

IMPLICIT Format
---------------

The IMPLICIT format defines a one-to-one mapping between table row and
HEALPix pixel index.  Each energy plane is represented by a separate
column (``CHANNEL0``, ``CHANNEL1``, etc.).  This format can only be
used for all-sky maps.

HEADER
~~~~~~

* ``INDXSCHM`` : ``IMPLICIT``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``CHANNEL{BAND_IDX}`` -- ndim: 1, type: float or int
    * Dimension: nrows
    * Amplitude in image plane ``{BAND_IDX}``.  The HEALPix pixel
      index is determined from the table row.

.. _hpx_explicit:
      
EXPLICIT Format
---------------

The EXPLICIT format uses an additional ``PIX`` column to explicitly
define the pixel number corresponding to each table row.  Pixel values
for each band are represented by a separate column (``CHANNEL0``,
``CHANNEL1``, etc.).  This format can be used for both all-sky and
partial-sky maps but requires the same pixel size for all bands.

  
HEADER
~~~~~~

* ``INDXSCHM`` : ``EXPLICIT``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``PIX`` -- ndim: 1, unit: None, type: int
    * Dimension: nrows
    * HEALPix pixel index.  This index is common to all bands.

* ``CHANNEL{BAND_IDX}`` -- ndim: 1, type: float or int
    * Dimension: nrows
    * Amplitude in HEALPix pixel ``PIX`` and band
      ``{BAND_IDX}``.

.. _hpx_local:
      
LOCAL Format
------------

The LOCAL format is identical to the :ref:`hpx_explicit` with the
exception that the ``PIX`` column contains a local rather than global
HEALPix index.  The local HEALPix index is a mapping of global indices
in a partial-sky geometry to 0, ..., N-1 where N is the total number of
pixels in the geometry.  For an all-sky geometry the local index is
equal to the global index.  This format can be used for both all-sky
and partial-sky maps as well as maps with a different pixel-size in
each band.

  
HEADER
~~~~~~

* ``INDXSCHM`` : ``LOCAL``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``PIX`` -- ndim: 1, unit: None, type: int
    * Dimension: nrows
    * Local HEALPix pixel index.  The mapping to global HEALPix index
      is derived by finding the index of the ith pixel in the geometry
      where pixels are ordered by their global index values.

* ``CHANNEL{BAND_IDX}`` -- ndim: 1, type: float or int
    * Dimension: nrows
    * Amplitude in HEALPix pixel ``PIX`` and band
      ``{BAND_IDX}``.
      
.. _hpx_sparse:
      
SPARSE Format
-------------

The SPARSE format allows for an arbitrary set of pixels to be defined
in each band.  The SKYMAP table contains three columns with the
pixel index, band index, and amplitude.  Pixel values for each band
are continguous and arranged in order of band index.  This format
supports an different HEALPix pixel size in each band defined by the
``NSIDE`` column in the ``BANDS`` table.

Pixels that are undefined but contained within the geometric selection
are assumed to be zero while pixels outside the geometric selection
are undefined.  For counts data this allows for maps that only contain
pixels with at least one count.


HEADER
~~~~~~

* ``INDXSCHM`` : ``SPARSE``
  
SKYMAP Columns
~~~~~~~~~~~~~~
      
* ``PIX`` -- ndim: 1, unit: None, type: int
    * Dimension: nrows
    * HEALPix pixel index.  Pixels are ordered by band number.  The
      row to band mapping is defined by the ``CHANNEL`` column.  

* ``CHANNEL`` -- ndim: 1, unit: None, type: int
    * Dimension: nrows
    * Band index.  This column is optional for maps with a single
      band.  For efficiency it is recommended to represent this column
      with a 16-bit integer.
      
* ``VALUE`` -- ndim: 1, unit: None, type: float or int
    * Dimension: nrows
    * Amplitude in pixel indexed by ``PIX`` and ``CHANNEL``.  
      

