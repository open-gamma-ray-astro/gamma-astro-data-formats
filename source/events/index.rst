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
* Suggested HDU name telescope array: ``TELARRAY``

EVENTS extension
----------------

The first extension contains characteristic information about each event.
Suggested extension name ``EVENTS``. These information are stored in a FITS
binary table. The columns are listed below. In addition, a list of header
keywords to be contained in each FITS event list is also documented. Many of the
keywords are not necessarily required for an analysis. The information is,
however, included as meta data in the event lists to enable instrument-dependent
studies and selections of particular observations.

Required columns
----------------

* ``EVENT_ID`` type: int
    * Event identification number at the DL3 level
      (lower data levels could be different, see note below).
    * Required: The pair (``OBS_ID``, ```EVENT_ID``) must be globally unique
      for all events from a given instrument.
      (to be discussed ... it's not clear if CTA will have "runs" ``OBS_ID``)
    * Required: ``EVENT_ID`` should increase monotonically with ``TIME``.
      (to be discussed if this should be changed to a recommendation only)
    * Required: event lists should be sorted by ``EVENT_ID`` and ``TIME``.
      (to be discussed if this should be changed to a recommendation only)
* ``TIME`` type: double, unit: s
    * Time stamp of event in MET
* ``RA`` type: float, unit: deg
    * Event right ascension (see :ref:`sky-coordinates-radec`)
* ``DEC`` type: float, unit: deg
    * Event declination (see :ref:`sky-coordinates-radec`)
* ``ENERGY`` type: float, unit: TeV
    * Reconstructed event energy

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
and to store ``EVENT_ID = (BUNCH_ID_HESS << 32) & (EVENT_ID_HESS)``, i.e.
use the upper bits to contain the low-level bunch ID and the lower bits
to contains the low-level event ID.
This encoding is unique and reversible, i.e. it's easy to go back to
``BUNCH_ID_HESS`` and ``EVENT_ID_HESS`` for a given ``EVENT_ID``,
and to low-level checks (e.g. look at the shower images for a given event
that behaves strangely in reconstructed high-level parameters).

Optional Column Names
---------------------

* ``MULTIP`` type: int
    * Telescope multiplicity. Number of telescopes that have seen the event
* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``DIR_ERR`` type: float, unit: deg
    * Direction error of reconstruction 
* ``ENERGY_ERR`` type: float, unit: TeV
    * Error on reconstructed event energy
* ``ALT`` type: float, unit: deg
    * Altitude coordinate of event (horizon system, see :ref:`sky-coordinates-altaz`)  
* ``AZ`` type: float, unit: deg
    * Azmuth coordinate of event (horizon system, see :ref:`sky-coordinates-altaz`)  
* ``DETX`` type: float, unit: deg
    * X-coordinate in detector system (nominal system, see :ref:`sky-coordinates-fov`)   
* ``DETY`` type: float, unit: deg
    * Y-coordinate in detector system (nominal system, see :ref:`sky-coordinates-fov`)     
* ``THETA`` type: float, unit: deg
    * Offset from the observation pointing position
* ``COREX`` type: float, unit: m
    * Core position X of shower
* ``COREY`` type: float, unit: m
    * Core position Y of shower
* ``CORE_ERR`` type: float, unit: m
    * Error on core position of shower    
* ``XMAX`` type: float, unit: radiation lengths
    * First interaction depth 
* ``XMAX_ERR`` type: float, unit: radiation lengths
    * Error on first interaction depth 
* ``HIL_MSW`` type: float
    * Hillas mean scaled width
* ``HIL_MSW_ERR`` type: float
    * Hillas mean scaled width error
* ``HIL_MSL`` type: float
    * Hillas mean scaled length
* ``HIL_MSL_ERR`` type: float
    * Hillas mean scaled length error

Required Header keywords:
-------------------------

* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``TELESCOP`` type: int
    * Telescope (e.g. 'HESS')
* ``TSTART`` type: float, unit: s
    * Start time of observation  [MET]
* ``TSTOP`` type: float, unit: s
    * End time of observation  [MET]
* ``TSTART_STR`` type: string
    * Start of observation in UTC string format: "YYYY-MM-DD HH:MM:SS"
* ``TSTOP_STR`` type: string
    * End of observation in UTC string format: "YYYY-MM-DD HH:MM:SS"
* ``MJDREFI`` type: int, unit: days
    * Integer part of MJD time reference
* ``MJDREFF`` type: float, unit: days
    * Float part of MJD time reference       
* ``ONTIME`` type: float, unit: s
    * Total observation time (including dead time).
    * Equals ``TSTOP`` - ``TSTART``
* ``LIVETIME`` type: float, unit: s
    * Total livetime (observation minus dead time)
* ``DEADC`` type: float
    * Dead time correction.
    * It is defined such that ``LIVETIME`` = ``DEADC`` * ``ONTIME``
      i.e. the fraction of time the telescope was actually able to take data.
* ``OBJECT`` type: string
    * Observed object     
* ``RA_PNT`` type: float, unit: deg
    * Obsevation pointing right ascension (see :ref:`sky-coordinates-radec`)
* ``DEC_PNT`` type: float, unit: deg
    * Observation pointing declination (see :ref:`sky-coordinates-radec`)
* ``ALT_PNT`` float, deg
    * Observation pointing altitude at observation mid-time ``TMID`` (see :ref:`sky-coordinates-altaz`)
* ``AZ_PNT`` type: float, unit: deg
    * Observation pointing azimuth at observation mid-time ``TMID`` (see :ref:`sky-coordinates-altaz`)    
* ``RA_OBJ`` type: float, unit: deg
    * Right ascension of ``OBJECT``
* ``DEC_OBJ`` type: float, unit: deg
    * Declination of ``OBJECT``                
* ``TELLIST`` type: string
    * Telescope IDs in observation (e.g. '1,2,3,4')   
* ``N_TELS`` type: int
    * Number of observing telescopes       
* ``EUNIT`` type: string
    * Unit of energies in event list (e.g. 'TeV')
* ``GEOLON`` type: float, unit: deg
    * Geographic longitude of array centre (e.g. -23.27 for HESS)     
* ``GEOLAT`` type: float, unit: deg
    * Geographic latitude of array centre (e.g. -16.5 for HESS)
* ``ALTITUDE`` type: float, unit: km
    * Altitude of array center above sea level (1.835 for HESS)

Optional header keywords
------------------------

* ``OBSERVER`` type: string
    * Name of observer (e.g. 'HESS'). This could be the PI of a proposal later on.
* ``CREATOR`` type: string
    * Software that created the file
* ``CREATED`` type: string
    * Time when file was created (UTC): "YYYY-MM-DD HH:MM:SS"
* ``RADECSYS`` type: string
    * Equatorial system type (e.g. 'FK5')
* ``EQUINOX`` type: float
    * Base equinox (e.g. 2000.) 
* ``TIMESYS`` type: string
    * Time system (currently 'TT')
* ``TIMEREF`` type: string
    * Time reference ('LOCAL')
* ``TASSIGN`` type: string
    * Place of time reference ('Namibia')
* ``OBS_MODE`` type: string
    * Observation mode (e.g. wobble, survey, or any mode that is supported by ``TELESCOP``) 
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

* ``START`` type: double, unit: s
    * Start time of good time interval (observation)  [MET]
* ``STOP`` type: double, unit: s
    * End time of good time interval (observation) [MET]
    
GTI Header Keywords
-------------------

* ``MJDREFI`` type: int, unit: days
    * Integer part of MJD time reference
* ``MJDREFF`` type: float, unit: days
    * Float part of MJD time reference   

TELARRAY extension
------------------

To be defined
