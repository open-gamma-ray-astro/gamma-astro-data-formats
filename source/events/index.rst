.. include:: ../references.txt

Event lists
===========

Event lists are stored in FITS files with three extensions (HDUs).

EVENTS extension
----------------

The first extension contains characteristic information about each
event. These information are stored in a FITS binary table. The columns
are listed in the :ref:`tab_1` table. In addition, a list of header keywords to be contained in each FITS event list is documented in the  :ref:`tab_2` table. Many of the keywords are not necessarily required for an analysis. The information is, however, included as meta data in the event lists to enable instrument-dependent studies and selections of particular observations.

GTI extension
-------------

Each event list file contains an extension to specify the good time intervals ('GTIs'). A general description of GTITs can be found in the `OGIP standard <http://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/rates/ogip_93_003/ogip_93_003.html#tth_sEc6.3>`__. This HDU contains two columns named START and STOP. At least one row is containing the start and end time of the observation must be present. The values are in units of seconds with respect to the reference time defined in the associated header (keywords MJDREFI and MJDREFF). This extension allows for a detailed handling of good time intervals (i.e. excluding periods with cloud cover or lightning during one observation). The column names and FITS header keywords are documented in Table  :ref:`tab_3` and  :ref:`tab_4`, respectively.

TELARRAY extension
------------------

To be defined

Reference Tables
----------------

.. _tab_1: 

.. table:: EVENTS extension columns

    =============  ============================== ============    =============
    Column Name    Description                     Unit            FITS Type
    =============  ============================== ============    =============
    OBS_ID         Run number                                      TLONG (1J)  
     BUNCH_ID       Bunch number                                    TLONG (1J)  
    EVENT_ID       Event number\*                                  TLONG (1J)  
    TIME           Event time stamp\*              s               TDOUBLE (1D)
    MULTIP         Telescope multiplicity                          TSHORT (1I) 
    RA             Right ascension\*               deg             TFLOAT (1E) 
    DEC            Declination\*                   deg             TFLOAT (1E) 
    DIR_ERR        Direction error                 deg             TFLOAT (1E) 
    DETX           Nominal System X\*              deg             TFLOAT (1E)  
    DETY           Nominal System Y\*              deg             TFLOAT (1E) 
    ALT            Altitude                        deg             TFLOAT (1E) 
    AZ             Azimuth                         deg             TFLOAT (1E) 
    COREX          Core position X                 m               TFLOAT (1E) 
    COREY          Core position Y                 m               TFLOAT (1E) 
    CORE_ERR       Core position error             m               TFLOAT (1E) 
    XMAX           First interaction depth         rad length      TFLOAT (1E) 
    XMAX_ERR       First interaction depth error   rad length      TFLOAT(1E) 
    ENERGY         Reconstructed energy\*          TeV             TFLOAT (1E)  
    ENERGY_ERR     Reconstructed energy error      TeV             TFLOAT (1E) 
    HIL_MSW        Mean scaled width                               TFLOAT (1E) 
    HIL_MSW_ERR    Mean scaled width error                         TFLOAT (1E) 
    HIL_MSL        Mean scaled length                              TFLOAT (1E) 
    HIL_MSL_ERR    Mean scaled length error                        TFLOAT (1E) 
    =============  ============================== ============    =============




.. _tab_2:

.. table:: EVENTS extension header keyword

    ==============  ================================================    =================    ======================
      Keyword         Description                                         Unit                  FITS type
    ==============  ================================================    =================    ======================
      CREATOR         Program which created the file                                             string
      TELESCOP        Telescope ('HESS')                                                         string
      OBS\_ID         Run number                                                                 int
      DATE\_OBS       Observation start date                              yyyy-mm-dd             string
      TIME\_OBS       Observation start time                              hh:mm:ss               string
      DATE\_END       Observation end date                                yyyy-mm-dd             string
      TIME\_END       Observation end time                                hh:mm:ss               string
      TSTART          Start time of observation                           s                      float 
      TSTOP           End time of observation                             s                      float
      MJDREFI         MJD time reference                                  days                   int 
      MJDREFF         MJD time reference                                  days                   float
      TIMESYS         Time system ('TT')                                                         string   
      TIMEREF         Time reference ('LOCAL')                                                   string    
      TASSIGN         Place of time reference ('Namibia')                                        string   
      TELAPSE         Start-End time                                      s                      float    
      ONTIME          Total good time including deadtime                  s                      float   
      LIVETIME        Total livetime                                      s                      float   
      DEADC           Dead time correction                                                       float   
      OBJECT          Observed object                                                            string   
      RA\_OBJ         RA of target                                        deg                    float   
      DEC\_OBJ        DEC of target                                       deg                    float   
      RA\_PNT         Nominal pointing RA                                 deg                    float   
      DEC\_PNT        Nominal pointing RA                                 deg                    float   
      ALT\_PNT        Mean altitude of pointing                           deg                    float   
      AZ\_PNT         Mean azimuth of pointing                            deg                    float   
      RADECSYS        Equatorial system type ('FK5')                                             string   
      EQUINOX         Base equinox (2000.)                                                       float   
      CONV\_DEP       convergence depth (0 for parallel pointing)                                float   
      CONV\_RA        Convergence Right Ascension                         deg                    float   
      CONV\_DEC       Convergence Declination                             deg                    float   
      OBS\_MODE       observation mode                                                           string   
      OBSERVER        Observer ('HESS')                                                          string    
      N\_TELS         Number of observing telescopes                                             int   
      TELLIST         Telescope IDs (e.g. '1,2,3,4')                                             string    
      GEOLAT          Geographic latitude of array centre (-23.27)        deg                    float   
      GEOLON          Geographic longitude of array centre (-16.5)        deg                    float   
      ALTITUDE        Altitude of array centre (1.835)                    km                     float     
      EUNIT           Energy unit ('TeV')                                                        string   
      TRGRATE         Mean trigger rate                                   Hz                     float   
      ZTRGRATE        zenith averaged trigger rate                        Hz                     float   
      MUONEFF         muon efficiency                                                            float   
      MEANTEMP        mean temperature                                    deg C                  float   
      CONFIG          Used cut configuration (e.g. 'std')                                        string   
      DST\_VER        Used DST version                                                           string   
      ANA\_VER        Reconstruction software version                                            string   
      CAL\_VER        Calibration software version                                               string   
      CREATED         Date and time of creation                                                  string            
    ==============  ================================================    =================    ======================



.. _tab_3:

.. table:: GIT extension columns

    =============  ============================== ============    =============
    Column Name    Description                     Unit            FITS Type
    =============  ============================== ============    =============
      START            Start of GTI (observation)   s               TDOUBLE (1D)
      STOP             End of GTI (observation)     s               TDOUBLE (1D) 
    =============  ============================== ============    =============


.. _tab_4:

.. table:: GTI extension header keyword

    ==============  =========================    =================    ======================
      Keyword         Description                    Unit                  FITS type
    ==============  =========================    =================    ======================
	   MJDREFI      MJD time reference            days                  int
	   MJDREFF      MJD time reference            days                  float
    ==============  =========================    =================    ======================
