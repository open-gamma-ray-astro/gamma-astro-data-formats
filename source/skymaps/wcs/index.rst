.. include:: ../../references.txt

.. _wcs_skymap:

WCS Formats
===========

This page describes data format conventions for images and cubes
pixelized with World Coordinate Systems (WCS).  WCS is a system for
describing transformations between pixel/world coordinates and sky
coordinates.  The conventions described here are extensions to the
`FITS WCS`_ standard which allow for serializing more complex data
structures such as sparse maps or maps with non-regular geometry
(e.g. a different pixel size in each image plane).

The format splits the specification of an image into two HDUs: an
:ref:`wcs_image_hdu` and a :ref:`bands_hdu`.  The image HDU contains
the image data while the BANDS HDU is an optional extension that
stores information about non-spatial dimensions.

There are two supported WCS formats:

* :ref:`wcs_image`: This is the standard FITS image format whereby
  data is stored in a FITS ImageHDU.  With the exception of handling
  of non-spatial dimensions images generated with this format follow
  standard FITS format conventions.

* :ref:`wcs_sparse`: This is a sparse data format for FITS images
  which uses a BinTableHDU to store pixel values.

By default multi-dimensional maps are assumed to have the same
projection in each image plane with the WCS projection specified in
the header keywords.
  
Both formats support the specification of non-regular
multi-dimensional geometries through the inclusion of ``CRPIX``,
``CEDLT``, and ``CRVAL`` columns in the :ref:`bands_hdu`.  A
non-regular geometry is one in which each image plane may have a
different pixelization (e.g. different pixel size or image extent).
The ``CRPIX``, ``CEDLT``, and ``CRVAL`` override the pixelization of
the base WCS projection (defined in the IMAGE HDU header) in each
image plane.

.. _wcs_sample_files:

Sample Files
------------


.. _wcs_image_hdu:
   
Image HDU
---------

The IMAGE HDU contains the map data and can be formatted according to
either the :ref:`wcs_image` or :ref:`wcs_sparse` scheme.  


WCS FITS Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

The keywords listed here are those required by the FITS WCS
specification.

* ``CRPIX{IDX}``, type : float
    * Pixel coordinate of reference point for axis ``{IDX}``.
* ``CDELT{IDX}``, type : float
    * Coordinate increment at reference point for axis ``{IDX}``.
* ``CTYPE{IDX}``, type : float
    * Coordinate system and projection code for axis ``{IDX}``.
* ``CRVAL{IDX}``, type : float
    * Coordinate value at reference point for axis ``{IDX}``.

Extra Header Keywords
~~~~~~~~~~~~~~~~~~~~~

These are extra keywords that are not part of the FITS WCS
specification but are required for some features of the GADF format.

* ``WCSSHAPE``, type: string, **optional**
    * Comma-separated list with the number of pixels in each dimension
      in row-major order, e.g. ``(4,5,3)`` would correspond to a 4x5
      image with three image planes.  For non-regular geometries the
      image dimension should be the maximum across all image planes.
      This keyword is optional for maps in the :ref:`wcs_image`
      format.
      
* ``BANDSHDU``, type: string, **optional**
    * Name of HDU containing the BANDS table.  If undefined the
      extension name should be ``EBOUNDS`` or ``ENERGIES``.  See
      :ref:`bands_hdu` for additional details.  

.. _wcs_image:

IMAGE Format
------------

The IMAGE format uses an ImageHDU to store map values.  Dimensions of
the image are directly inferred from the data member of the HDU.  This
is the standard format for WCS-based maps.


.. _wcs_sparse:

SPARSE Format
-------------

The SPARSE WCS format uses the same conventions as the :ref:`Sparse
HEALPix Format <hpx_sparse>`.  This format uses a BinTableHDU to store
map values with one row per pixel.

Columns
~~~~~~~
      
* ``PIX`` -- ndim: 1, unit: None, type: int
    * Dimension: nrows
    * Flattened pixel index in a given image plane (band).  Indices
      are flattened assuming a column-major ordering for the image.
      The row to band mapping is defined by the ``CHANNEL`` column.

* ``CHANNEL`` -- ndim: 1, unit: None, type: int
    * Dimension: nrows
    * Band index.  This column is optional for maps with a single
      band.  For efficiency it is recommended to represent this column
      with a 16-bit integer.
      
* ``VALUE`` -- ndim: 1, unit: None, type: float or int
    * Dimension: nrows
    * Amplitude in pixel indexed by ``PIX`` and ``CHANNEL``.  
