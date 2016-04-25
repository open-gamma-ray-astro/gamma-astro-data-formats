.. include:: ../references.txt

.. _iact-pnt:

.. warning::
   This is a first draft proposal of a pointing table. Please note that
   the format is likely subject to change.


``POINTING`` extension
======================

The ``POINTING`` extension is a binary FITS table that contains for a number
of time stamps the pointing direction of the telescopes. A *pointing* is here
defined as the centre of the field of view (or centre of the camera
coordinates). In reality, all telescopes may point to different positions
(for example for divergent pointing mode).


Mandatory columns
-----------------

* ``TIME`` tform: ``1D``, unit: s
    * Time stamp of pointing.
* ``RA_PNT`` type: float, unit: deg
    * Pointing Right Ascension (see :ref:`sky-coordinates-radec`).
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``DEC_PNT`` type: float, unit: deg
    * Pointing declination (see :ref:`sky-coordinates-radec`).
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``ALT_PNT`` float, deg
    * Pointing altitude.
* ``AZ_PNT`` type: float, unit: deg
    * Pointing azimuth.


Mandatory header keywords
-------------------------

* ``MJDREFI`` type: int, unit: days
    * Integer part of instrument specific MJD time reference
* ``MJDREFF`` type: float, unit: days
    * Float part of instrument specific MJD time reference       
* ``TIMEUNIT`` type: string
    * Time unit (e.g. 's')
* ``TIMESYS`` type: string
    * Time system (e.g. 'TT', 'MJD', 'JD', 'TJD')
* ``TIMEREF`` type: string
    * Time reference frame, used for example for barycentric corrections
      (options: 'LOCAL', 'SOLARSYSTEM', 'HELIOCENTRIC', 'GEOCENTRIC')
* ``GEOLON`` type: float, unit: deg
    * Geographic longitude of array centre (e.g. -23.27 for HESS)     
* ``GEOLAT`` type: float, unit: deg
    * Geographic latitude of array centre (e.g. -16.5 for HESS)
* ``GEOALT`` type: float, unit: m
    * Altitude of array center above sea level (1835 for HESS)
