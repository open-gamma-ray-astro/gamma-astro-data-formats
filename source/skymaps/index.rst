.. _skymaps:

Sky Maps
========

.. toctree::
   :maxdepth: 1
   :hidden:

   healpix/index
   wcs/index
   region/index

This page describes data formats for data structures representing
images in celestial coordinates.  A sky map may have one or more
non-spatial dimensions (e.g. energy or time) such that the data
consists of a sequence of image planes.  There are two primary
pixelization formats which are described in more detail in the
following sub-pages:

* :ref:`healpix_skymap`

* :ref:`wcs_skymap`

* :ref:`region_skymap`


Both pixelization formats store the data in a single IMAGE HDU which
can be either an ImageHDU or BinTableHDU depending on the image
format.  A :ref:`bands_hdu` is required for maps with non-spatial dimensions.

.. _bands_hdu:

BANDS HDU
---------

For maps with non-spatial dimensions, the BANDS table defines the
geometry in each band and the band to coordinate mapping for
non-spatial dimensions (e.g. energy).  The BANDS table is optional for
maps with a single band.

The extension name of the BANDS table associated to an image HDU is
given by the ``BANDSHDU`` header keyword of the image HDU.  If
``BANDSHDU`` is undefined the BANDS table should be read from the
``EBOUNDS`` or ``ENERGIES`` HDU.  The BANDS table extension names
``EBOUNDS`` and ``ENERGIES`` are reserved for maps with a third energy
dimension and are supported for backward compatibility with existing
file format conventions of the Fermi STs.  Although each map will
have its own IMAGE HDU, a single BANDS table can be associated to
multiple maps (if they share the same geometry).

The BANDS table contains 1 row per band with columns that define the
mapping of the band to the non-spatial dimensions of the map.  For
integral quantities (e.g. counts) this should be the lower and upper
edge values of the bin.  For differential quantities this should be
the coordinates at which the map value was evaluated.  Some examples
of quantities that can be used to define bands are as follows:

* Energy (Integral): ``E_MIN``, ``E_MAX``
* Energy (Differential): ``ENERGY``
* Event Type: ``EVENT_TYPE``
* Time: ``TIME_MIN``, ``TIME_MAX``
* FoV Angle: ``THETA_MIN``, ``THETA_MAX``

The mapping of column to non-spatial dimension is defined with the
``AXCOLS{IDX}`` header keyword.  For maps with multiple non-spatial
dimensions the mapping of channel number to band indices follows a
column-major ordering.  For instance for a map with a first energy
dimension with 3 bins indexed by *i* and a second time dimension with
2 bins indexed by *j* the band index mapping to channel number *k*
would be as follows::

  (i, j) = (0,0) : (k) = (0,)
  (i, j) = (1,0) : (k) = (1,)
  (i, j) = (2,0) : (k) = (2,)
  (i, j) = (0,1) : (k) = (3,)
  (i, j) = (1,1) : (k) = (4,)
  (i, j) = (2,1) : (k) = (5,)


Header Keywords
~~~~~~~~~~~~~~~

* ``AXCOLS{IDX}``, type: string, **optional**
    * Comma-separated list of columns in the BANDS table corresponding
      to non-spatial dimension with one-based index ``{IDX}``.  If
      there are two elements the columns should be interpreted as the
      lower and upper edges of each bin.  If there is a single element
      the column should be interpreted as the bin center.  For
      ``EBOUNDS`` or ``ENERGIES`` HDUs this keyword is optional.

* ``INTERP{IDX}``, type: string, **optional**
    * Specify how the non-spatial bins are spaced and recommended to be interpolated.
      Possible values are:
        * ``"lin"``: linear spacing e.g. used for time or offset axes
        * ``"log"``: logarithimic spacing e.g. used for energy axes
        * ``"sqrt"``: square root spacing e.g. used for radial axes

For time based axes the additional keywords described in :ref:`time-formats` are
required.


Columns
~~~~~~~

* ``CHANNEL``, ndim: 1
    * Dimension: nbands
    * Unique index of the band.  If this column is not defined then
      the band index should be inferred from the row number indexing
      from zero.  For maps with multiple non-spatial dimensions the
      index mapping to channel number follows a column-major ordering.
* ``E_MIN``, ndim: 1, unit: keV, **optional**
    * Dimension: nbands
    * Lower energy bound for integral quantities.
* ``E_MAX``, ndim: 1, unit: keV, **optional**
    * Dimension: nbands
    * Upper energy bound for integral quantities.
* ``ENERGY``, ndim: 1, unit: keV, **optional**
    * Dimension: nbands
    * Energy value for differential quantities.
* ``EVENT_TYPE``, ndim: 1, **optional**
    * Dimension: nbands
    * Integer key for a sequence of independent data subselections (e.g. FRONT/BACK-converting LAT events).

WCS Columns
~~~~~~~~~~~

This section lists BANDS table columns specific to the :ref:`WCS map
format <wcs_skymap>`.  These are optional columns to specify the
pixelization for non-regular geometries.

* ``NPIX``, ndim: 2, type: int, **optional**
    * Number of pixels in longitude and latitude in each image plane.

* ``CRPIX``, ndim: 2, type: float, **optional**
    * Reference pixel coordinate [deg] in longitude and latitude in each image plane.

* ``CDELT``, ndim: 2, type: float, **optional**
    * Pixel size [deg] in longitude and latitude in each image plane.


HPX Columns
~~~~~~~~~~~

This section lists BANDS table columns specific to the :ref:`HEALPix map format <healpix_skymap>`.

* ``NSIDE`` -- ndim: 1,
    * Dimension: nbands
    * NSIDE of the HEALPix pixelization in this band.  If not defined
      then ``NSIDE`` should be inferred from the FITS header.  Only
      required for formats that support energy-dependent pixelization
      (``SPARSE``).


Region Columns
~~~~~~~~~~~~~~

In the :ref:`Region map format <region_skymap>` the data is directly stored as an additional
column:

* ``DATA``, ndim: 1, type: float
