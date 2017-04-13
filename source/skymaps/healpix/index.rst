.. include:: ../../references.txt

.. _healpix:

This page describes data format conventions for FITS binned data and model
representations pixelized with the `HEALPix algorithm`_.  

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

The format defines a ``SKYMAP`` BINTABLE for storing a sequence of
image slices (*bands*) and a :ref:`hpx_bands_table` to store the
geometry and selection parameters for each band.  A band can represent
any selection on non-spatial coordinates such as energy, time, or FoV
angle.  The most common use-case is to have a sequence of bands
representing energy bins (for counts maps) or energy nodes (for source
or model maps).  To allow for backwards compatibility with existing
HEALPix format conventions the specification defines optional
:ref:`hpx_ebounds_table` and :ref:`hpx_energies_table` to store bin
edges or nodes for integral or differential cubes in energy.
  
There are three primary HEALPix map formats which use different table
structures for mapping table entries to HEALPix pixel and band:

* :ref:`hpx_implicit`: The row to pixel mapping is determined implicitly from
  the row number.  The row number corresponds to the HEALPix pixel
  number.
* :ref:`hpx_explicit`: The row to pixel mapping is determined explicitly from
  the ``PIX`` column.  This can be used to define maps or cubes that
  only encompass a partial region of the sky.
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
  
Header Keywords
---------------

This section lists the keywords that should be written to the
``SKYMAP`` BINTABLE HDU header.  These keywords define the pixel size
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
* ``LASTPIX``, type: int
* ``HPX_REG``, type: string, **optional**
    * Region string for the geometric selection that was used to
      construct a partial-sky map.  See :ref:`hpx_region_string` for
      additional details.
* ``HPX_CONV``, type: string, **optional**
    * Convention for HEALPix format.
* ``BANDSHDU``, type: string, **optional**
    * Name of HDU containing the BANDS table.  If undefined the
      extension name should be assumed to be ``BANDS``.
* ``EBNDSHDU``, type: string, **optional**
    * Name of HDU containing the EBOUNDS table.  If undefined the
      extension name should be assumed to be ``EBOUNDS``.
* ``ENERGHDU``, type: string, **optional**
    * Name of HDU containing the ENERGIES table.  If undefined the
      extension name should be assumed to be ``ENERGIES``.

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

In the case of ``SPARSE`` maps pixels that are undefined but contained
within the geometric selection are assumed to be zero while pixels
outside the geometric selection are undefined.
  
.. _hpx_sample_files:
  
Sample Files
------------

* All-sky Counts Cube (IMPLICIT Format): :download:`FITS <hpx_ccube_implicit.fits>`
* Partial-sky Counts Cube (EXPLICIT Format): :download:`FITS <hpx_ccube_explicit.fits>`
* Partial-sky Counts Map (EXPLICIT Format): :download:`FITS <hpx_cmap_explicit.fits>`
* Partial-sky Counts Cube (SPARSE Format)::download:`FITS <hpx_ccube_sparse.fits>`

.. _hpx_bands_table:
   
BANDS Table
-----------

The BANDS HDU contains a BINTABLE with 1 row per band.  A band is a sequence
of HEALPix pixels that contain events for selections on any of the
following:

* Energy: ``E_MIN``, ``E_REF``, ``E_MAX``
* Event Type: ``EVENT_TYPE``
* Time: ``T_MIN``, ``T_MAX``
* FoV Angle: ``THETA_MIN``, ``THETA_MAX``

Where a band is defined by multiple selections (e.g. energy and event
type) columns for all selections should be included in the table.
  
Columns
~~~~~~~

* ``BAND``, ndim: 1
    * Dimension: nbands
* ``NPIX``, ndim: 1
    * Dimension: nbands
    * Number of pixels in each band.
* ``NSIDE`` -- ndim: 1,
    * Dimension: nbands
    * NSIDE of the HEALPix pixelization in this band.  Only required
      for formats that support energy-dependent pixelization
      (``SPARSE``).
* ``E_MIN``, ndim: 1, unit: keV,
    * Dimension: nbands
    * Lower energy bound for integral quantities.
* ``E_MAX``, ndim: 1, unit: keV,
    * Dimension: nbands
    * Upper energy bound for integral quantities.      
* ``E_REF``, ndim: 1, unit: keV,
    * Dimension: nbands
    * Energy value for differential quantities.

  
.. _hpx_ebounds_table:
   
EBOUNDS Table
-------------

The EBOUNDS HDU is a BINTABLE with 1 row per energy bin.  For cubes
that only contain energy bands this table contains the same
information as the BANDS table.

Columns
~~~~~~~

* ``CHANNEL``, ndim: 1
* ``E_MIN``, ndim: 1, unit: keV,
    * Dimension: nebins
* ``E_MAX``, ndim: 1, unit: keV,
    * Dimension: nebins


.. _hpx_energies_table:
   
ENERGIES Table
--------------
      
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
* ``BANDS``
* ``EBOUNDS``, *optional*
* ``ENERGIES``, *optional*

HEADER
~~~~~~

* ``INDXSCHM`` : ``IMPLICIT``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``CHANNEL{BAND_IDX}`` -- ndim: 1
    * Dimension: nrows
    * Amplitude in energy plane ``{BAND_IDX}``.  The HEALPix pixel
      index is determined from the table row.

.. _hpx_explicit:
      
EXPLICIT Format
---------------

The EXPLICIT format uses an additional ``PIX`` column to explicitly
define the pixel number corresponding to each table row.  Pixel values
for each band are represented by a separate column (``CHANNEL0``,
``CHANNEL1``, etc.).  This format can be used for both all-sky and
partial-sky maps but requires the same pixel size for all bands.

HDUS
~~~~

* ``SKYMAP``
* ``BANDS``
* ``EBOUNDS``, *optional*
* ``ENERGIES``, *optional*
  
HEADER
~~~~~~

* ``INDXSCHM`` : ``EXPLICIT``
  
SKYMAP Columns
~~~~~~~~~~~~~~

* ``PIX`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Spatial pixel index.  This index is common to all bands.

* ``CHANNEL{BAND_IDX}`` -- ndim: 1
    * Dimension: nrows
    * Amplitude in HEALPix pixel ``PIX`` and band
      ``{BAND_IDX}``.
      
.. _hpx_sparse:
      
SPARSE Format
-------------

The SPARSE format allows for an arbitrary list of pixels to be defined
in each band.  The ``SKYMAP`` table contains two columns with the
pixel index and amplitude for all bands.  Pixel values for each band
are continguous and arranged in order of band index.  The mapping
between row and band number can be derived from the ``NPIX`` column of
the ``BANDS`` table which contains the number of pixels defined in
each band.  This format supports an independent pixel size in each
band defined by the ``NSIDE`` column in the ``BANDS`` table.

HDUS
~~~~

* ``SKYMAP``
* ``BANDS``

HEADER
~~~~~~

* ``INDXSCHM`` : ``SPARSE``
  
SKYMAP Columns
~~~~~~~~~~~~~~
      
* ``PIX`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Spatial pixel index.  Pixels are ordered by band number.  The
      row to band mapping is defined by the ``NPIX`` column of the
      ``BANDS`` table.

* ``VALUE`` -- ndim: 1, unit: None
    * Dimension: nrows
    * Amplitude in pixel indexed by ``PIX``.  
      

