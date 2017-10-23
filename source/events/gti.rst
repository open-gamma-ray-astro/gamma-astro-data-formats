.. include:: ../references.txt

.. _iact-gti:

``GTI`` extension
=================

The ``GTI`` extension is a binary FITS table that contains the Good Time
Intervals ('GTIs') for the event list. A general description of GTIs can
be found in the `OGIP GTI`_ standard.

This HDU contains two mandatory columns named ``START`` and ``STOP``. At
least one row is containing the start and end time of the observation must
be present. The values are in units of seconds with respect to the reference
time defined in the header (keywords MJDREFI and MJDREFF). This extension
allows for a detailed handling of good time intervals (i.e. excluding periods
with cloud cover or lightning during one observation).

High-level Science tools could modify the GTIs according to user parameter.
See e.g. `gtmktime`_ for an application example from the Fermi Science Tools.


Mandatory columns
-----------------

* ``START`` tform: ``1D``, unit: s
    * Start time of good time interval (given in instrument specific time
      reference, see below)
* ``STOP`` tform: ``1D``, unit: s
    * End time of good time interval (given in instrument specific time
      reference, see below)


Mandatory header keywords
-------------------------

* ``MJDREFI`` type: int, unit: days
    * Integer part of instrument specific MJD time reference
* ``MJDREFF`` type: float, unit: days
    * Float part of instrument specific MJD time reference       
* ``TIMEUNIT`` type: string
    * Time unit (e.g. 's')
* ``TIMESYS`` type: string
    * Time system, also referred as time scale (e.g. 'UT', 'UTC', 'TT', 'TAI') 
* ``TIMEREF`` type: string
    * Time reference frame, used for example for barycentric corrections
      (options: 'LOCAL', 'SOLARSYSTEM', 'HELIOCENTRIC', 'GEOCENTRIC')
