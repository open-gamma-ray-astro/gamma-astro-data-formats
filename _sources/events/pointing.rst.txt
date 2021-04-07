.. include:: ../references.txt

.. warning::
   This is a first draft proposal of a pointing table.
   It is not being used yet by data producers or science tools.
   Please note that the format is likely subject to change.
   
.. _iact-pnt:

POINTING
========

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
    * Pointing time (see :ref:`time`)
* ``RA_PNT`` type: float, unit: deg
    * Pointing Right Ascension (see :ref:`coords-radec`).
* ``DEC_PNT`` type: float, unit: deg
    * Pointing declination (see :ref:`coords-radec`).

Optional columns
----------------

* ``ALT_PNT`` type: float, unit: deg
    * Pointing altitude (see :ref:`coords-altaz`).
* ``AZ_PNT`` type: float, unit: deg
    * Pointing azimuth  (see :ref:`coords-altaz`).

Mandatory header keywords
-------------------------

The standard FITS reference time header keywords should be used (see :ref:`time-formats`).
An observatory Earth location should be given as well (see :ref:`coords-location`).

