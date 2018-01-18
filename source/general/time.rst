.. include:: ../references.txt

.. _time:

Time
====

Introduction
------------

This page describes how times should be stored.
This is a solved problem, we follow the `FITS standard`_.
However, the FITS standard is very complex (see also `FITS time paper`_),
and allows for different ways to store times in FITS, some of which
are hard to understand and implement.

To keep things simple, we here agree on a way to store times that
is fully compliant, but a subset of the ways allowed by the FITS standard
(see :ref:`time-formats` below).

This has the advantage of simplicity and uniformity for writers and readers
(see :ref:`time-tools` below).

One major point allowing for this simplicity is that we only need single 64-bit float precision for time
in high-level (DL3 and up) gamma-ray astronomy, as explained in the :ref:`time-precision` section below.

The following formats contain times:

* :ref:`iact-events`
* :ref:`iact-gti`
* :ref:`iact-pnt`
* :ref:`obs-index`

Other useful resources concerning time:

* https://heasarc.gsfc.nasa.gov/docs/fcg/common_dict.html
* `Time in Fermi data analysis`_

.. _time-formats:

Formats
-------

Times should be given as 64-bit float columns, relative to a reference time point
that is specified by the following FITS header keywords:

* ``MJDREFI`` type: int, unit: days
    * Integer part of instrument specific MJD time reference
* ``MJDREFF`` type: float, unit: days
    * Float part of instrument specific MJD time reference
* ``TIMEUNIT`` type: string
    * Time unit (e.g. 's')
* ``TIMESYS`` type: string
    * Time system, also referred as time scale (e.g. 'UT', 'UTC', 'TT', 'TAI')
* ``TIMEREF`` type: string
    * Time reference frame, used for example for barycentric corrections
      (options: 'LOCAL', 'SOLARSYSTEM', 'HELIOCENTRIC', 'GEOCENTRIC')

See the `FITS standard`_ and the `FITS time paper`_ for further information.

In addition to that main way of specifying times as a floating point number wrt. a reference timepoint,
the following header keys with date and time values as strings can be added.
This is for convenience and humans reading the information. Usually science tools will not access
this redundant and optional information. The time system used should be the one given by ``TIMESYS``.

* ``DATE-OBS`` type: string
    * Observation start date (format: "yyyy-mm-dd")
* ``TIME-OBS`` type: string
    * Observation start time (format: "hh:mm:ss.sss...")
* ``DATE-END`` type: string
    * Observation end date (format: "yyyy-mm-dd")
* ``TIME-END`` type: string
    * Observation end time (format: "hh:mm:ss.sss...")

Note that the FITS standard allows and it is quite common to instead put a
``TIME-OBS`` key with value "yyyy-mm-ddThh:mm:ss.sss..." and to omit the ``DATE-OBS`` key
(see `Dictionary of Commonly Used FITS Keywords`_). That is allowed as well.

.. _time-tools:

Tools
-----

The `SOFA Time Scale and Calendar Tools`_ document provides a detailed
description of times in the high-precision IAU SOFA library, which is the
gold standard for times in astronomy.
The SOFA time routines are available via the  `Astropy time`_ Python package,
which makes it easy to convert between different **time scales**
(``utc``, ``tt`` and ``mjd`` in this example).

.. code-block:: python

    >>> from astropy.time import Time
    >>> time = Time('2011-01-01 00:00:00', scale='utc', format='iso')
    >>> time
    <Time object: scale='utc' format='iso' value=2011-01-01 00:00:00.000>
    >>> time.tt
    <Time object: scale='tt' format='iso' value=2011-01-01 00:01:06.184>
    >>> time.mjd
    55562.0

as well as different **time formats** (``iso``, ``isot`` and ``fits`` in this example)

.. code-block:: python

    >>> time.iso
    '2011-01-01 00:00:00.000'
    >>> time.isot
    '2011-01-01T00:00:00.000'
    >>> time.fits
    '2011-01-01T00:00:00.000(UTC)'

If you don't want to install SOFA or Astropy (or to double-check),
you can use the `xTime`_ time conversion utility provided by HEASARC as a web tool.

* Gammapy uses `Astropy time`_, with custom utility functions for FITS I/O
  to write in the formats recommended here.
* Gammalib has custom code to hande times that is described in `Times in Gammalib`_.

.. _time-precision:

Precision
---------

Depending on the use case and required precision, times are stored as strings
or as one or several integer or floating point numbers. Tools usually use
one 64-bit or two 64-bit floating point numbers for time calculations.

For high-level gamma-ray astronomy, the situation can be summarised like this
(see sub-section computation below for details):

* **Do use single 64-bit floats for times.**
  The resulting precision will be about 0.1 micro-seconds or better,
  which is sufficient for any high-level analysis (including milli-second pulsars).
* **Do not use 32-bit floats for times.**
  If you do, times will be incorrect at the 1 to 100 second level.
* **Double-float precision is not needed.**

For data acquisition and low-level analysis (event triggering, traces, ...),
IACTs require nanosecond precision or better. There, the simple advice to use
64-bit floats representing seconds wrt. a single reference time doesn't work!
One either needs to have several reference times (e.g. per-observation) or
two integer or float values. This is not covered by this spec.

The time precision obtained with a single 32-bit or 64-bit float can be computed
with this function:

.. code-block:: python

    def time_precision(time_range, float_precision):
        """Compute time precision (seconds) in float computations.
        
        For a given `time_range` and `float_precision`, the `time_precision`
        is computed as the smallest time difference corresponding to the
        float precision.
        
        time_range -- (IN) Time range of application (years)
        float_precision -- (IN) {32, 64} Floating point precision
        time_precision -- (OUT) Time precision (seconds)    
        """
        import numpy as np
        YEAR_TO_SEC = 315576000
        
        dtype = {32: np.float32, 64: np.float64}[float_precision]
        t1 = dtype(YEAR_TO_SEC * time_range)
        t2 = np.nextafter(t1, np.finfo(dtype).max)
        print('Time range: {} years, float precision: {} bit => time precision: {:.3g} seconds.'
              ''.format(time_range, float_precision, t2-t1))

.. code-block:: python

    >>> time_precision(10, 32)
    Time range: 10 years, float precision: 32 bit => time precision: 256 seconds.
    >>> time_precision(10, 64)
    Time range: 10 years, float precision: 64 bit => time precision: 4.77e-07 seconds.
