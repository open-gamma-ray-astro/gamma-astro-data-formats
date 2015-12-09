.. _obs-index:

Observation index table
=======================

The observation index table is stored in a FITS file as a BINTABLE HDU:

* Suggested filename: ``obs-index.fits.gz``
* Suggested HDU name: ``OBS_INDEX``

It contains one row per observation (a.k.a. run) and lists parameters that are
commonly used for observation selection, grouping and analysis.

.. _obs-index-required-columns:

Required columns
----------------

* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``RA_PNT`` type: float, unit: deg
    * Obsevation pointing right ascension (see :ref:`sky-coordinates-radec`)
* ``DEC_PNT`` type: float, unit: deg
    * Observation pointing declination (see :ref:`sky-coordinates-radec`)
* ``ALT_PNT`` float, deg
    * Observation pointing mean altitude (see :ref:`sky-coordinates-altaz`)
    * Recommendation: use value at observation mid-time ``TMID``.
* ``AZ_PNT`` type: float, unit: deg
    * Observation pointing mean azimuth (see :ref:`sky-coordinates-altaz`)
    * Recommendation: use value at observation mid-time ``TMID``.
* ``ZEN_PNT`` type: float, unit: deg
    * Mean zenith of pointing (see :ref:`sky-coordinates-altaz`)
    * Recommendation: use value at observation mid-time ``TMID``.
* ``ONTIME`` type: float, unit: s
    * Total observation time (including dead time).
    * Equals ``TSTOP`` - ``TSTART``
* ``LIVETIME`` type: float, unit: s
    * Total livetime (observation minus dead time)
* ``DEADC`` type: float
    * Dead time correction.
    * It is defined such that ``LIVETIME`` = ``DEADC`` * ``ONTIME``
      i.e. the fraction of time the telescope was actually able to take data.
* ``TSTART`` type: float, unit: days
    * Start of observation in MJD
* ``TSTART_STR`` type: string
    * Start of observation in UTC string format: "YYYY-MM-DD HH:MM:SS"
* ``TSTOP`` type: float, unit: days
    * End time of observation in MJD
* ``TSTOP_STR`` type: string
    * End of observation in UTC string format: "YYYY-MM-DD HH:MM:SS"
* ``N_TELS`` type: int
    * Number of participating telescopes 
* ``TELLIST`` type: string
    * Telescope IDs (e.g. '1,2,3,4')
* ``QUALITY`` type: int
    * Observation data quality. The following levels of data quality are defined:
        * 0 = best quality, suitable for spectral analysis.
        * 1 = medium quality, suitable for detection, but not spectra (typically if the atmosphere was hazy).
        * 2 = bad quality, usually not to be used for analysis. 

.. _obs-index-optional-columns:

Optional columns
----------------

The following columns are optional. They are sometimes used for observation
selection or data quality checks or analysis, but aren't needed for most users.

* ``RA_OBJ`` type: float, unit: deg
    * RA of target
* ``DEC_OBJ`` type: float, unit: deg
    * DEC of target 
* ``TMID`` type: float, unit: days
    * Mid time of observation in MJD (= ``TSTART`` + 0.5 * ``ONTIME``)
* ``TMID_STR`` type: string
    * Mid time of observation in UTC string format: "YYYY-MM-DD HH:MM:SS"
* ``EVENT_COUNT`` type: int
    * Number of events in run
* ``EVENT_RA_MEDIAN`` type: float, unit: deg
    * Median right ascension of events 
* ``EVENT_DEC_MEDIAN`` type: float, unit: deg
    * Median declination of events
* ``EVENT_ENERGY_MEDIAN`` type: float, unit: deg
    * Median energy of events
* ``EVENT_TIME_MIN`` type: double, unit: s
    * First event time
* ``EVENT_TIME_MAX`` type: double, unit: s
    * Last event time
* ``BKG_SCALE`` type: float
    * Background scaling factor. See notes below.
* ``TRGRATE`` type: float, unit: Hz
    * Mean system trigger rate
* ``ZTRGRATE`` type: float, unit: Hz
    * Zenith averaged mean system trigger rate
    * TODO: define what "zenithed averaged mean" means or remove this column.
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

.. _obs-index-notes:

Notes
-----

* This table doesn't require header keywords. We recommend FITS is used,
  but it can be stored e.g. in CSV as well.
* Some of the required columns are redundant. E.g. ``ONTIME`` = ``TSTOP`` - ``TSTART``.
  The motivation to declare those columns required is to make it easy for users
  and tools to browse the observation lists and select observations via cuts
  on these parameters without having to compute them on the fly.
* Observation runs where the telescopes don't point to a fixed RA / DEC position
  (e.g. drift scan runs) aren't supported at the moment by this format.
* Times are given as a UTC string or MJD float.
  This is preferred over the use of mission elapsed time (MET),
  because MET requires a reference timepoint stored in header keywords
  ``MJDREFI`` and ``MJDREFF``, and we felt that having a simpler table
  format here that doesn't require a header would be nice.
* Purpose / definition of ``BKG_SCALE``:
  This factor comes e.g. from the analysis of off runs. The background
  normalisation usually dependends on between the number of events in a run, the
  zenith angle and other parameters. This parameter provides the possibility to
  give the user a better prediction of the background normalisation. For CTA
  this might be induced from atmospheric monitoring and additional diagnostic
  input. For HESS we try to find a trend in the off run background
  normalisations and other parameters such as number of events per unit
  livetime. The Background scale should be around 1.0 if the background model is
  good. This number should also be set to 1.0 if no dependency analysis has been
  performed. If the background model normalisation if off by a few orders of
  magnitude for some reasons, this can be incorporated here.
