.. _iact-gti:

GTI extension
-------------

Each event list file contains an extension to specify the good time intervals
('GTIs'). A general description of GTIs can be found in the `OGIP GTI`_
standard. This HDU contains two columns named START and STOP. At least one row
is containing the start and end time of the observation must be present. The
values are in units of seconds with respect to the reference time defined in the
associated header (keywords MJDREFI and MJDREFF). This extension allows for a
detailed handling of good time intervals (i.e. excluding periods with cloud
cover or lightning during one observation). Eventually, this extension could
disappear from the required extensions. High-level Science tools could add the
GTIs to the files according to user parameter. See e.g. `gtmktime`_ for an
application example from the Fermi Science Tools. The column names and FITS
header keywords are documented in the following, respectively.

GTI Column Names
----------------

* ``START`` tform: ``1D``, unit: s
    * Start time of good time interval (given in instrument specific time reference, see below)
* ``STOP`` tform: ``1D``, unit: s
    * End time of good time interval (given in instrument specific time reference, see below)
    
GTI Header Keywords
-------------------

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
