.. _obs-index:

Observation index table
=======================

The observation index table is stored in a FITS file as a BINTABLE HDU:

* Suggested filename: ``obs-index.fits``
* Suggested HDU name: ``OBS_INDEX``

It contains one row per observation (a.k.a. run) and lists parameters that are
commonly used for observation selection, grouping and analysis.

.. _obs-index-columns:

Columns
-------

=====================  ================================================    =================   ========= =========
Keyword                Description                                         Unit                Data type Required?
=====================  ================================================    =================   ========= =========
OBS_ID                 Run number                                                              int       yes
N_TELS                 Number of participating telescopes                                      int       ?
RA_PNT                 Nominal pointing RA                                 deg                 float     yes
DEC_PNT                Nominal pointing RA                                 deg                 float     yes
ALT_PNT                Mean altitude of pointing                           deg                 float     no
AZ_PNT                 Mean azimuth of pointing                            deg                 float     no
ZEN_PNT                Mean zenith of pointing                             deg                 float     no
RA_OBJ                 RA of target                                        deg                 float     no
DEC_OBJ                DEC of target                                       deg                 float     no
TRGRATE                Mean trigger rate                                   Hz                  float     no
ZTRGRATE               zenith averaged trigger rate                        Hz                  float     no
MUONEFF                muon efficiency                                                         float     no
MEANTEMP               mean temperature                                    deg C               float     no
ONTIME                 Total good time including deadtime                  s                   float     no
LIVETIME               Total livetime                                      s                   float     no
DEADC                  Dead time correction                                                    float     no
OBJECT                 Observed object                                                         string    no
TSTART                 Start time of observation                           s                   float     no
TSTOP                  End time of observation                             s                   float     no
BKG_SCALE              Input background scaling factor                                         float     no
EVENT_COUNT            Number of events in run                                                 int       no
EVENT_RA_MEDIAN        Median right ascension of events                                        float     no
EVENT_DEC_MEDIAN       Median declination of events                                            float     no
EVENT_ENERGY_MEDIAN    Median energy of events                                                 float     no
EVENT_TIME_MIN         First event time                                                        double    no
EVENT_TIME_MAX         Last event time                                                         double    no
QUALITY                Run quality (0=good, 1=bad, 2=dubious)                                  int       no
TELLIST                Telescope IDs (e.g. '1,2,3,4')                                          string    no
OBS_MODE               Observation mode                                                        string    no
DATE_OBS               Observation start date                              yyyy-mm-dd          string    no
TIME_OBS               Observation start time                              hh:mm:ss            string    no
DATE_END               Observation end date                                yyyy-mm-dd          string    no
TIME_END               Observation end time                                hh:mm:ss            string    no
=====================  ================================================    =================   ========= =========

Extra notes on the definition of some columns and valid values:

* The recommended codes for run quality are:
  * 0 = best quality, suitable for spectral analysis.
  * 1 = medium quality, suitable for detection, but not spectra (typically if the atmosphere was hazy).
  * 2 = bad quality, usually not to be used for analysis.
* TODO: ZTRGRATE: remove!? (or define what it's supposed to be)
*

TODO: where are the valid TYPE values listed?

.. _obs-index-header:

Header keywords
---------------

TODO: are those needed? Do we have times in MET?

========== =========================  ========= =========
Keyword    Description                Data type Required?
========== =========================  ========= =========
MJDREFI    MJD time reference (days)  int       no
MJDREFF    MJD time reference (days)  int       no
========== =========================  ========= =========
