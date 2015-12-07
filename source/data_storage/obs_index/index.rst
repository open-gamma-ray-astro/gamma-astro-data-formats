Observation index file
======================

The observation index file contains information about each run.

OBS SUMMARY extension
---------------------

The first and only extension is called "OBS SUMMARY"

.. _tab_1: 

.. table:: OBS SUMMARY column names

    =====================  ================================================    =================   ======================
    Keyword                Description                                         Unit                FITS type
    =====================  ================================================    =================   ======================
    OBS\_ID                Run number                                                              int
    N\_TELS                Number of participating telescopes                                      int
    RA\_PNT                Nominal pointing RA                                 deg                 float
    DEC\_PNT               Nominal pointing RA                                 deg                 float
    ALT\_PNT               Mean altitude of pointing                           deg                 float
    AZ\_PNT                Mean azimuth of pointing                            deg                 float
    ZEN\_PNT               Mean zenith of pointing                             deg                 float
    RA\_OBJ                RA of target                                        deg                 float
    DEC\_OBJ               DEC of target                                       deg                 float
    TRGRATE                Mean trigger rate                                   Hz                  float
    ZTRGRATE               zenith averaged trigger rate                        Hz                  float
    MUONEFF                muon efficiency                                                         float
    MEANTEMP               mean temperature                                    deg C               float
    ONTIME                 Total good time including deadtime                  s                   float
    LIVETIME               Total livetime                                      s                   float
    DEADC                  Dead time correction                                                    float
    OBJECT                 Observed object                                                         string
    TSTART                 Start time of observation                           s                   float
    TSTOP                  End time of observation                             s                   float
    BKG_SCALE              Input background scaling factor                                         float
    EVENT\_COUNT           Number of events in run                                                 int
    EVENT\_RA\_MEDIAN      Median right ascension of events                                        float
    EVENT\_DEC\_MEDIAN     Median declination of events                                            float
    EVENT\_ENERGY\_MEDIAN  Median energy of events                                                 float
    EVENT\_TIME\_MIN       First event time                                                        double
    EVENT\_TIME\_MAX       Last event time                                                         double
    QUALITY                Run quality (0=good, 1=bad, 2=dubious)                                  int
    TELLIST                Telescope IDs (e.g. '1,2,3,4')                                          string
    OBS\_MODE              Observation mode                                                        string
    DATE\_OBS              Observation start date                              yyyy-mm-dd          string
    TIME\_OBS              Observation start time                              hh:mm:ss            string
    DATE\_END              Observation end date                                yyyy-mm-dd          string
    TIME\_END              Observation end time                                hh:mm:ss            string
    =====================  ================================================    =================   ======================

.. _tab_2:

.. table:: OBS SUMMARY header keywords

    ==============  =========================    =================    ======================
      Keyword         Description                    Unit                  FITS type
    ==============  =========================    =================    ======================
       MJDREFI      MJD time reference            days                  int
       MJDREFF      MJD time reference            days                  float
    ==============  =========================    =================    ======================

