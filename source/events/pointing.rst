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
(for example for divergent pointing mode). The main purpose of the ``POINTING``
extension is to provide time dependent information on how to transform
between celestial and terrestial coordinates.

See also `HFWG Recommendation R3`_ for the OGIP standard.

Mandatory columns
-----------------

* ``TIME`` type: float64, unit: s
    * Time stamp of pointing.
* ``RA_PNT`` type: float, unit: deg
    * Pointing Right Ascension (see :ref:`coords-radec`).
* ``DEC_PNT`` type: float, unit: deg
    * Pointing declination (see :ref:`coords-radec`).
* ``ALT_PNT`` type: float, unit: deg
    * Pointing altitude (see :ref:`coords-altaz`).
* ``AZ_PNT`` type: float, unit: deg
    * Pointing azimuth  (see :ref:`coords-altaz`).


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
    * Geographic longitude of array centre
* ``GEOLAT`` type: float, unit: deg
    * Geographic latitude of array centre
* ``GEOALT`` type: float, unit: m
    * Altitude of array center above sea level
