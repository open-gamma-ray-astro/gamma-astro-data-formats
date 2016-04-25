.. include:: ../references.txt

.. _iact-events:

IACT event lists
================

This document describes IACT DL3 event lists.

Event lists are stored in FITS files with two required and one optional
extensions (HDUs).

* Suggested filename: ``events_OBS_ID.fits.gz``
* Suggested HDU name events: ``EVENTS``
* Suggested HDU name good time intervals: ``GTI``
* Suggested optional HDU name telescope array: ``TELARRAY``

EVENTS extension
----------------

The first extension is a binary FITS table that contains an event list.
Each row of the table provides information that characterises one event.
The mandatory and optional columns of the table are listed below. In
addition, a list of header keywords providing metadata is specified.
Also here there are mandatory and optional keywords.
The suggested extension name of the binary table is ``EVENTS``.

Mandatory columns
-----------------

* ``EVENT_ID`` tform: ``1J``, unit: N.A.
    * Event identification number at the DL3 level
      (lower data levels could be different, see note below).
* ``TIME`` tform: ``1D``, unit: s
    * Time stamp of event in MET
* ``RA`` tform: ``1E``, unit: deg
    * Reconstructed event Right Ascension (see :ref:`sky-coordinates-radec`)
* ``DEC`` tform: ``1E``, unit: deg
    * Reconstructed event Declination (see :ref:`sky-coordinates-radec`)
* ``ENERGY`` tform: ``1E``, unit: TeV
    * Reconstructed event energy
* ``DETX`` tform: ``1E``, unit: deg
    * Reconstructed event X-coordinate in detector system (nominal system, see :ref:`sky-coordinates-fov`) 
* ``DETY`` tform: ``1E``, unit: deg
    * Reconstructed event Y-coordinate in detector system (nominal system, see :ref:`sky-coordinates-fov`)

Optional Column Names
---------------------

None of the following columns is required to be part of an IACT DL3 FITS file.
Any software using these columns should first check whether the columns exist,
and warn in case of their absence.

* ``ALT`` tform: ``1E``, unit: deg
    * Reconstructed altitude coordinate of event (horizon system, see :ref:`sky-coordinates-altaz`)  
* ``AZ`` tform: ``1E``, unit: deg
    * Reconstructed azimuth coordinate of event (horizon system, see :ref:`sky-coordinates-altaz`)  
* ``THETA`` tform: ``1E``, unit: deg
    * Reconstructed offset from the observation pointing position
* ``PHI`` tform: ``1E``, unit: deg
    * Reconstructed position angle from the observation pointing position (position angles are counted counterclockwise from celestial North)
* ``MULTIP`` tform: ``1I``
    * Telescope multiplicity. Number of telescopes that have seen the event
* ``OBS_ID`` tform: ``1I``
    * Unique observation identifier (Run number)
* ``DIR_ERR`` tform: ``1E``, unit: deg
    * Direction error of reconstruction 
* ``ENERGY_ERR`` tform: ``1E``, unit: TeV
    * Error on reconstructed event energy
* ``COREX`` tform: ``1E``, unit: m
    * Core position X of shower
* ``COREY`` tform: ``1E``, unit: m
    * Core position Y of shower
* ``CORE_ERR`` tform: ``1E``, unit: m
    * Error on core position of shower    
* ``XMAX`` tform: ``1E``, unit: radiation lengths
    * First interaction depth 
* ``XMAX_ERR`` tform: ``1E``, unit: radiation lengths
    * Error on first interaction depth 
* ``HIL_MSW`` tform: ``1E``
    * Hillas mean scaled width
* ``HIL_MSW_ERR`` tform: ``1E``
    * Hillas mean scaled width error
* ``HIL_MSL`` tform: ``1E``
    * Hillas mean scaled length
* ``HIL_MSL_ERR`` tform: ``1E``
    * Hillas mean scaled length error

Mandatory Header keywords:
--------------------------

* ``ORIGIN`` type: string
    * Organisation that created the FITS file.
* ``CREATOR`` type: string
    * Software that created the file.
      When appropriate, the value of the CREATOR keyword should also reference the specific
      version of the program that created the FITS file.
      It is intented that this keyword should refer to the program that originally defined the
      FITS file structure and wrote the contents. If a FITS file is subsequently copied largely
      intact into a new FITS by another program, then the value of the CREATOR keyword should
      still refer to the original program. ``HISTORY`` keywords should be used instead to document
      any further processing that is performed on the file after it is created.
* ``TELESCOP`` type: string
    * Telescope (e.g. 'CTA', 'HESS', 'VERITAS', 'MAGIC')
* ``INSTRUME`` type: string
    * Instrument used to aquire the data contained in the file (e.g. 'North', 'South')
* ``OBSERVER`` type: string
    * Name of observer (e.g. 'Joe Public'). This could be the PI of a proposal later on.
* ``OBJECT`` type: string
    * Observed object (e.g. 'Crab')
* ``OBS_MODE`` type: string
    * Observation mode (e.g. 'Wobble', 'Scan', 'Slew', or any mode that is supported by ``TELESCOP``) 
* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``DATE_OBS`` type: string
    * Start date of observation in UTC string format: "YYYY-MM-DD"
* ``TIME_OBS`` type: string
    * Start time of observation in UTC string format: "HH:MM:SS"
* ``DATE_END`` type: string
    * End date of observation in UTC string format: "YYYY-MM-DD"
* ``TIME_END`` type: string
    * End time of observation in UTC string format: "HH:MM:SS"
* ``TSTART`` type: float, unit: s
    * Start time of observation (given in instrument specific time reference, see below)
* ``TSTOP`` type: float, unit: s
    * End time of observation (given in instrument specific time reference, see below)
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
* ``TELAPSE`` type: float, unit: s
    * Time interval between start and stop time (``TELAPSE=TSTOP-TSTART``).
      Any gaps due to bad weather, or high background counts and/or other anomalies, are included.
* ``ONTIME`` type: float, unit: s
    * Total *good time* (sum of length of all Good Time Intervals).
      If a Good Time Interval (GTI) table is provided, ``ONTIME`` should be calculated as the sum of those intervals.
      Corrections for instrumental *dead time* effects are **NOT** included.
* ``LIVETIME`` type: float, unit: s
    * Total time (in seconds) on source, corrected for the *total* instrumental dead time effect.
* ``DEADC`` type: float
    * Dead time correction, defined by ``LIVETIME/ONTIME``.
      Is comprised in [0,1]. Defined to be 0 if ``ONTIME=0``.
* ``RA_PNT`` type: float, unit: deg
    * Observation pointing right ascension (see :ref:`sky-coordinates-radec`)
         Note: this keyword can be removed in a pointing table is added
* ``DEC_PNT`` type: float, unit: deg
    * Observation pointing declination (see :ref:`sky-coordinates-radec`)
         Note: this keyword can be removed in a pointing table is added

Optional header keywords
------------------------

Note: This section needs review. It contains for the moment a long list of things that
may appear in an IACT DL3 file. This list could be separate into keywords actually needed
by H.E.S.S. and other keywords.

* ``RA_OBJ`` type: float, unit: deg
    * Right ascension of ``OBJECT``
* ``DEC_OBJ`` type: float, unit: deg
    * Declination of ``OBJECT``                
* ``ALT_PNT`` float, deg
    * Observation pointing altitude at observation mid-time ``TMID`` (see :ref:`sky-coordinates-altaz`)
* ``AZ_PNT`` type: float, unit: deg
    * Observation pointing azimuth at observation mid-time ``TMID`` (see :ref:`sky-coordinates-altaz`)    
* ``GEOLON`` type: float, unit: deg
    * Geographic longitude of array centre (e.g. -23.27 for HESS)     
* ``GEOLAT`` type: float, unit: deg
    * Geographic latitude of array centre (e.g. -16.5 for HESS)
* ``ALTITUDE`` type: float, unit: m
    * Altitude of array center above sea level (1835 for HESS)
* ``TELLIST`` type: string
    * Telescope IDs in observation (e.g. '1,2,3,4')   
* ``N_TELS`` type: int
    * Number of observing telescopes       
* ``CREATED`` type: string
    * Time when file was created (UTC): "YYYY-MM-DD HH:MM:SS"
* ``RADECSYS`` type: string
    * Equatorial system type (e.g. 'FK5')
* ``EQUINOX`` type: float
    * Base equinox (e.g. 2000.) 
* ``TASSIGN`` type: string
    * Place of time reference ('Namibia')
* ``DST_VER`` type: string
    * Version of DST/Data production 
* ``ANA_VER`` type: string
    * Reconstruction software version   
* ``CAL_VER`` type: string
    * Calibration software version 
* ``CONV_DEP`` type: float
    * convergence depth (0 for parallel pointing)  
* ``CONV_RA`` type: float, unit: deg
    * Convergence Right Ascension    
* ``CONV_DEC`` type: float, unit: deg
    * Convergence Declination
* ``TRGRATE`` type: float, unit: Hz
    * Mean system trigger rate
* ``ZTRGRATE`` type: float, unit: Hz
    * Zenith equivalent mean system trigger rate    
* ``MUONEFF`` type: float
    * Mean muon efficiency
    * TODO: define how muon efficiency is defined (it's very tricky to get a comparable number in HESS from HD and PA calibration)
* ``BROKPIX`` type: float
    * Fraction of broken pixels (0.15 means 15% broken pixels)
* ``AIRTEMP`` type: float, unit: deg C
   * Mean air temperature at ground during the observation.
* ``PRESSURE`` type: float, unit: hPa
   * Mean air pressure at ground during the observation.
* ``NSBLEVEL`` type: float, unit: a.u.
   * Measure for NSB level
   * TODO: how is this defined? at least leave a comment if it doesn't have a clear definition and can only be used in one chain.
* ``RELHUM`` type: float
   * Relative humidity
   * TODO: link to definition ... wikipedia?


Notes on EVENT_ID
-----------------

This paragraph contains some explanatory notes concerning the requirements
and recommendations on ``EVENT_ID``.

Most analyses with high-level science tools don't need ``EVENT_ID`` information.
But being able to uniquely identify every event is important, e.g. when
comparing the high-level reconstructed event parameters (``RA``, ``DEC``,
``ENERGY``) for different calibrations, reconstructions or gamma-hadron
separations.

Assigning a unique ``EVENT_ID`` during data taking can be difficult or
impossible. E.g. in H.E.S.S. we have two numbers ``BUNCH_ID_HESS`` and
``EVENT_ID_HESS`` that only together uniquely identify an event within a given
run (i.e. ``OBS_ID``). Probably the scheme to uniquely identify events at the
DL0 level for CTA will be even more complicated, because of the much larger
number of telescopes and events.

So given that data taking and event identification is different for every IACT
at low data levels and is already fixed for existing IACTs, we propose here
to have an ``EVENT_ID`` that is simpler and works the same for all IACTs at
the DL3 level.

As an example: for H.E.S.S. we achive this by using an INT64 for ``EVENT_ID``
and to store ``EVENT_ID = (BUNCH_ID_HESS << 32) || (EVENT_ID_HESS)``, i.e.
use the upper bits to contain the low-level bunch ID and the lower bits
to contains the low-level event ID.
This encoding is unique and reversible, i.e. it's easy to go back to
``BUNCH_ID_HESS`` and ``EVENT_ID_HESS`` for a given ``EVENT_ID``,
and to low-level checks (e.g. look at the shower images for a given event
that behaves strangely in reconstructed high-level parameters).


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

TELARRAY extension
------------------

To be defined
