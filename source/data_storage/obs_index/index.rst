.. _obs-index:

Observation index table
=======================

The observation index table is stored in a FITS file as a BINTABLE HDU:

* Suggested filename: ``obs-index.fits.gz``
* Suggested HDU name: ``OBS_INDEX``

It contains one row per observation (a.k.a. run) and lists parameters that are
commonly used for observation selection, grouping and analysis.

.. _obs-index-columns:

Columns
-------
+ OBS_ID [int]: 
  Unique observation identifier (Run number)
+ RA_PNT [float, deg]: 
  Nominal pointing Right Ascension       
+ DEC_PNT [float, deg]: 
  Nominal pointing Declination
+ ALT_PNT [float, deg]: 
  Mean altitude of pointing       
+ AZ_PNT [float, deg]: 
  Mean azimuth of pointing       
+ ZEN_PNT [float, deg]: 
  Mean zenith of pointing
+ RA_OBJ [float, deg]: 
  RA of target 
+ DEC_OBJ [float, deg]: 
  DEC of target 
+ ONTIME [float, s]: 
  Total good time including deadtime 
+ LIVETIME [float, s]: 
  Total livetime
+ DEADC [float]: 
  Dead time correction. It is defined as the fraction LIVETIME / ONTIME, i.e. the fraction of time the telescope was actually able to take data
+ TSTART [float, days]: 
  Start of observation in MJD (note that we don't use MET here, since MJD is more handy)
+ TSTOP [float, days]: 
  End time of observation in MJD
+ DATE_OBS [string]: 
  Observation start date (yyyy-mm-dd)
+ TIME_OBS [string]: 
  Observation start time (hh:mm:ss)
+ DATE_END [string]: 
  Observation end date (yyyy-mm-dd)
+ TIME_END [string]: 
  Observation end time (hh:mm:ss)
+ N_TELS [int]: 
  Number of participating telescopes 
+ TELLIST [string]: 
  Telescope IDs (e.g. '1,2,3,4')
+ QUALITY [int]: 
  Run quality attribute. The recommended codes for run quality are:
    + 0 = best quality, suitable for spectral analysis.
    + 1 = medium quality, suitable for detection, but not spectra (typically if the atmosphere was hazy).
    + 2 = bad quality, usually not to be used for analysis. 
+ EVENT_COUNT [int]: 
  Number of events in run
+ EVENT_RA_MEDIAN [float, deg]: 
  Median right ascension of events 
+ EVENT_DEC_MEDIAN [float, deg]: 
  Median declination of events
+ EVENT_ENERGY_MEDIAN [float, deg]: 
  Median energy of events
+ EVENT_TIME_MIN [double, s]: 
  First event time
+ EVENT_TIME_MAX [double, s]: 
  Last event time
+ BKG_SCALE [float]: 
  Background scaling factor. This factor comes e.g. from the analysis of off runs. The background normalisation usually dependends on between the number of
  events in a run, the zenith angle and other parameters. This parameter provides the possibility to give the user a better prediction of the background normalisation. For CTA this might be induced from atmospheric monitoring and additional diagnostic input. For HESS we try to find a trend in the off run background normalisations and other parameters such as number of events per unit livetime. The
  Background scale should be around 1.0 if the background model is good. This number should also be set to 1.0 if no
  dependency analysis has been performed. If the background model normalisation if off by a few orders of magnitude
  for some reasons, this can be incorporated here.

+ (TRGRATE) [float, Hz]: 
  Mean system trigger rate
+ (ZTRGRATE) [float, Hz]: 
  Zenith averaged mean system trigger rate
+ (MUONEFF) [float]: 
  Mean muon efficiency 
+ (BROKPIX) [float]: 
  Percentage of broken pixels (0.15 means 15% broken pixels)
+ (MEANTEMP) [float, deg C]: 
  Mean temperature during run
+ (MEANPRES) [float, hPa]: 
  Mean air pressure
+ (NSBLEVEL) [float, a.u.] 
  Measure for NSB level
+ (RELHUM) [float]: 
  relative humidity

Column names in brackets denote that this column is optional
