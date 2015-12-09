.. include:: ../references.txt

.. _iact-events:

IACT event lists
================

Event lists are stored in FITS files with two required and one optional extensions (HDUs).

* Suggested filename: ``events_OBS_ID.fits.gz``
* Suggested HDU name events: ``EVENTS``
* Suggested HDU name good time intervals: ``GTI``
* Suggested HDU name telescope array: ``TELARRAY``



EVENTS extension
----------------

The first extension contains characteristic information about each event. Suggested extension name ``EVENTS``.
These information are stored in a FITS binary table. The columns are listed below.
In addition, a list of header keywords to be contained in each FITS event list is also documented.
Many of the keywords are not necessarily required for an analysis.
The information is, however, included as meta data in the event lists to enable
instrument-dependent studies and selections of particular observations.

Column Names
------------
* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``BUNCH_ID`` type: int
    * Number of bunch that contained the event
* ``EVENT_ID`` type: int
    * Number of event inside bunch (using ``OBS_ID``, ``BUNCH_ID`` and ``EVENT_ID`` one can build unique event identifiers across an experiment)
* ``TIME`` type: double, unit: s
    * Time stamp of event in MET
* ``MULTIP`` type: int
    * Telescope multiplicity. Number of telescopes that have seen the event
* ``RA`` type: float, unit: deg
    * Event right ascension (see :ref:`sky-coordinates-radec`)
* ``DEC`` type: float, unit: deg
    * Event declination (see :ref:`sky-coordinates-radec`)
* ``DIR_ERR`` type: float, unit: deg
    * Direction error of reconstruction 
* ``DETX`` type: float, unit: deg
    * X-coordinate in detector system (nominal system, see :ref:`sky-coordinates-radec`)   
* ``DETY`` type: float, unit: deg
    * Y-coordinate in detector system (nominal system, see :ref:`sky-coordinates-radec`)     
* ``ALT`` type: float, unit: deg
    * Altitude coordinate of event (horizon system, see :ref:`sky-coordinates-radec`)  
* ``AZ`` type: float, unit: deg
    * Azmuth coordinate of event (horizon system, see :ref:`sky-coordinates-radec`)  
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
* ``ENERGY`` type: float, unit: TeV
    * Reconstructed event energy
* ``ENERGY_ERR`` type: float, unit: TeV
    * Error on reconstructed event energy
* ``HIL_MSW`` type: float
    * Hillas mean scaled width
* ``HIL_MSW_ERR`` type: float
    * Hillas mean scaled width error
* ``HIL_MSL`` type: float
    * Hillas mean scaled length
* ``HIL_MSL_ERR`` type: float
    * Hillas mean scaled length error      


Required Header keywords:
------------------------

* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``TELESCOP`` type: int
    * Telescope (e.g. 'HESS')
* ``CREATOR`` type: string
    * Software that created the file
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
* ``TIMESYS`` type: string
    * Time system (currently 'TT')
* ``TIMEREF`` type: string
    * Time reference ('LOCAL')
* ``TASSIGN`` type: string
    * Place of time reference ('Namibia')
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
* ``ZEN_PNT`` type: float, unit: deg
    * Observation pointing zenith angle at observation mid-time ``TMID`` (see :ref:`sky-coordinates-altaz`)
* ``ALT_PNT`` float, deg
    * Observation pointing altitude at observation mid-time ``TMID`` (see :ref:`sky-coordinates-altaz`)
* ``AZ_PNT`` type: float, unit: deg
    * Observation pointing azimuth at observation mid-time ``TMID`` (see :ref:`sky-coordinates-altaz`)    
* ``RA_OBJ`` type: float, unit: deg
    * Right ascension of ``OBJECT``
* ``DEC_OBJ`` type: float, unit: deg
    * Declination of ``OBJECT``
* ``RADECSYS`` type: string
    * Equatorial system type (e.g. 'FK5')
* ``EQUINOX`` type: float
    * Base equinox (e.g. 2000.)   
* ``CONV_DEP`` type: float
    * convergence depth (0 for parallel pointing)  
* ``CONV_RA`` type: float, unit: deg
    * Convergence Right Ascension    
* ``CONV_DEC`` type: float, unit: deg
    * Convergence Declination
* ``OBS_MODE`` type: string
    * Observation mode (e.g. wobble, survey, or any mode that is supported by ``TELESCOP``)    
* ``OBSERVER`` type: string
    * Name of observer (e.g. 'HESS'). This could be the PI of a proposal later on.              
* ``TELLIST`` type: string
    * Telescope IDs in observation (e.g. '1,2,3,4')   
* ``N_TELS`` type: int
    * Number of observing telescopes    
* ``OBS_MODE`` type: string
    * Observation mode (e.g. wobble, survey, or any mode that is supported by ``TELESCOP``)    
* ``EUNIT`` type: string
    * Unit of energies in event list (e.g. 'TeV')
* ``GEOLON`` type: float, unit: deg
    * Geographic longitude of array centre (e.g. -23.27 for HESS)     
* ``GEOLAT`` type: float, unit: deg
    * Geographic latitude of array centre (e.g. -16.5 for HESS)
* ``ALTITUDE`` type: float, unit: km
    * Altitude of array center above sea level (1.835 for HESS)
* ``DST_VER`` type: string
    * Version of DST/Data production 
* ``ANA_VER`` type: string
    * Reconstruction software version   
* ``CAL_VER`` type: string
    * Calibration software version 
* ``CREATED`` type: string
    * Time when file was created: "YYYY-MM-DD HH:MM:SS"


Optional header keywords
------------------------

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



GTI extension
-------------

Each event list file contains an extension to specify the good time intervals ('GTIs').
A general description of GTIs can be found in the
`OGIP standard <http://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/rates/ogip_93_003/ogip_93_003.html#tth_sEc6.3>`__.
This HDU contains two columns named START and STOP.
At least one row is containing the start and end time of the observation must be present.
The values are in units of seconds with respect to the reference time defined in the
associated header (keywords MJDREFI and MJDREFF).
This extension allows for a detailed handling of good time intervals
(i.e. excluding periods with cloud cover or lightning during one observation).
The column names and FITS header keywords are documented in Table  :ref:`tab_3` and  :ref:`tab_4`, respectively.

TELARRAY extension
------------------

To be defined

Reference Tables
----------------


.. _tab_1:

.. table:: GIT extension columns

    =============  ============================== ============    =============
    Column Name    Description                     Unit            FITS Type
    =============  ============================== ============    =============
      START            Start of GTI (observation)   s               TDOUBLE (1D)
      STOP             End of GTI (observation)     s               TDOUBLE (1D) 
    =============  ============================== ============    =============


.. _tab_1:

.. table:: GTI extension header keyword

    ==============  =========================    =================    ======================
      Keyword         Description                    Unit                  FITS type
    ==============  =========================    =================    ======================
	   MJDREFI      MJD time reference            days                  int
	   MJDREFF      MJD time reference            days                  float
    ==============  =========================    =================    ======================
    
    
Disclaimer: About names of HDU and file structure
-------------------------------------------------

For the moment, we require the HDUs ``EVENTS`` and ``GTI`` to be present in the same file to conduct a
ctools analysis.
   
