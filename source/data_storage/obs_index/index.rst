.. include:: ../../references.txt

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
    * Obsevation pointing right ascension (see :ref:`coords-radec`)
* ``DEC_PNT`` type: float, unit: deg
    * Observation pointing declination (see :ref:`coords-radec`)
* ``TSTART`` type: float, unit: s
    * Start time of observation relative to the reference time (see :ref:`time`)
* ``TSTOP`` type: float, unit: s
    * End time of observation relative to the reference time (see :ref:`time`)

.. _obs-index-optional-columns:

Optional columns
----------------

The following columns are optional. They are sometimes used for observation
selection or data quality checks or analysis, but aren't needed for most users.

* ``ZEN_PNT`` type: float, unit: deg
    * Observation pointing zenith angle at observation mid-time ``TMID`` (see :ref:`coords-altaz`)
* ``ALT_PNT`` float, deg
    * Observation pointing altitude at observation mid-time ``TMID`` (see :ref:`coords-altaz`)
* ``AZ_PNT`` type: float, unit: deg
    * Observation pointing azimuth at observation mid-time ``TMID`` (see :ref:`coords-altaz`)
* ``ONTIME`` type: float, unit: s
    * Total observation time (including dead time).
    * Equals ``TSTOP`` - ``TSTART``
* ``LIVETIME`` type: float, unit: s
    * Total livetime (observation minus dead time)
* ``DEADC`` type: float
    * Dead time correction.
    * It is defined such that ``LIVETIME`` = ``DEADC`` * ``ONTIME``
      i.e. the fraction of time the telescope was actually able to take data.
* ``DATE-OBS`` type: string
    * Observation start date (see :ref:`time`)
* ``TIME-OBS`` type: string
    * Observation start time (see :ref:`time`)
* ``DATE-END`` type: string
    * Observation end date (see :ref:`time`)
* ``TIME-END`` type: string
    * Observation end time (see :ref:`time`)
* ``N_TELS`` type: int
    * Number of participating telescopes 
* ``TELLIST`` type: string
    * Telescope IDs (e.g. '1,2,3,4')
* ``QUALITY`` type: int
    * Observation data quality. The following levels of data quality are defined:
        * -1 = unknown quality
        *  0 = best quality, suitable for spectral analysis.
        *  1 = medium quality, suitable for detection, but not spectra (typically if the atmosphere was hazy).
        *  2 = bad quality, usually not to be used for analysis. 
* ``OBJECT`` type: string
    * Primary target of the observation
    * Recommendations:
        * Use a name that can be resolved by `SESAME`_
        * For survey observations, use "survey".
        * For :ref:`glossary-obs-off`, use "off observation"
* ``GLON_PNT`` type: float, unit: deg
    * Observation pointing Galactic longitude (see :ref:`coords-galactic`).
* ``GLAT_PNT`` type: float, unit: deg
    * Observation pointing Galactic latitude (see :ref:`coords-galactic`).
* ``RA_OBJ`` type: float, unit: deg
    * Right ascension of ``OBJECT``
* ``DEC_OBJ`` type: float, unit: deg
    * Declination of ``OBJECT``
* ``TMID`` type: float, unit: s
    * Mid time of observation relative to the reference time
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
    * Observation-dependent background scaling factor. See notes below.
* ``TRGRATE`` type: float, unit: Hz
    * Mean system trigger rate
* ``ZTRGRATE`` type: float, unit: Hz
    * Zenith equivalent mean system trigger rate
    * Some HESS chains export this at the moment and this quantity can be useful
      for data selection. Comparing values from different chains or other
      telescopes would require a more specific specification.
* ``MUONEFF`` type: float
    * Mean muon efficiency
    * Currently use definitions from analysis chain, since creating a unified
      specification is tricky.
* ``BROKPIX`` type: float
    * Fraction of broken pixels (0.15 means 15% broken pixels)
* ``AIRTEMP`` type: float, unit: deg C
   * Mean air temperature at ground during the observation.
* ``PRESSURE`` type: float, unit: hPa
   * Mean air pressure at ground during the observation.
* ``NSBLEVEL`` type: float, unit: a.u.
   * Measure for NSB level
   * Some HESS chains export this at the moment and this quantity can be useful
     for data selection. Comparing values from different chains or other
     telescopes would require a more specific specification.
* ``RELHUM`` type: float
   * Relative humidity
   * `Definition <https://en.wikipedia.org/wiki/Relative_humidity>`__

Mandatory Header keywords
-------------------------

The standard FITS reference time header keywords should be used (see :ref:`time-formats`).
An observatory Earth location should be given as well (see :ref:`coords-location`).

.. _obs-index-notes:

Notes
-----

* Observation runs where the telescopes don't point to a fixed RA / DEC position
  (e.g. drift scan runs) aren't supported at the moment by this format.
* Purpose / definition of ``BKG_SCALE``:
  For a 3D likelihood analysis a good estimate of the background is important.
  The run-by-run varation of the background rate is ~20%. The main reasons are
  the changing atmospheric conditions. This parameter allows to specify (from
  separate studies) a scaling factor to the :ref:`bkg` This factor comes e.g.
  from the analysis of off runs. The background normalisation usually dependends
  on e.g. the number of events in a run, the zenith angle and other parameters.
  This parameter provides the possibility to give the user a better prediction
  of the background normalisation. For CTA this might be induced from
  atmospheric monitoring and additional diagnostic input. For HESS we try to
  find a trend in the off run background normalisations and other parameters
  such as number of events per unit livetime. The background scale should be
  around 1.0 if the background model is good. This number should also be set to
  1.0 if no dependency analysis has been performed. If the background model
  normalisation is off by a few orders of magnitude for some reasons, this can
  also be incorporated here.
