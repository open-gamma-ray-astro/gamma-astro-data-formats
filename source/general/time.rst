.. include:: ../references.txt

.. _time:

Time
====

This page gives background information on times in gamma-ray astronomy.

It's not a format specification, rather a summary of the status quo:

* How times are stored in files.
* How times are represented in science tool codes
* How times are input by users and output to users from these codes.

.. _time-introduction:

Introduction
------------

Times are used in many places in high-level analysis, e.g.

* Observations have start and end times and sometimes are split up into
  "good time intervals" GTIs when hardware issues occur or clouds pass the field of view.
* Gamma-ray events are observed at given times, and those times are needed
  to convert the reconstructed AltAz position to RaDec, or to select events in
  a given GTI.
* Some gamma-ray sources are variable, e.g. AGNs can flare on timescales of seconds or minutes,
  or pulsars emit a periodic signal on timescales of seconds or milli-seconds.

This page contains specifications and recommendations how to work with times
for high-level gamma-ray astronomy, i.e. how to store times in files
(e.g. event lists, GTI extension, observation tables) and
take times as input and output in analysis tools.

Reference documents and tools
-----------------------------

Basically we follow `Time in Fermi data analysis`_, so this is the number one
reference.

The `SOFA Time Scale and Calendar Tools`_ document provides a detailed
description of times in the high-precision IAU SOFA library, which is the
gold standard for times in astronomy.
The SOFA time routines are available via the  `Astropy time`_ Python package,
which makes it easy to convert between different **time scales**
(``utc``, ``tt`` and ``mjd`` in this example)

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

Finally, the "Representation of Time Coordinates in FITS" standard (`2015A%26A...574A..36R`_)
explains in detail how times should be stored in FITS files.

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

For data acquisition and low-level analysis (event triggering, traces, ...),
IACTs require nanosecond precision or better. There, the simple advice to use
64-bit floats representing seconds wrt. a single reference time doesn't work!
One either needs to have several reference times (e.g. per-observation) or
two integer or float values. This is not covered by this spec.

Computation
+++++++++++

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

.. _time-files:

Files
-----

Here's a summary of how times are stored in files:

* :ref:`iact-events`:

  * Table column ``TIME``, ``float64``, MET
  * Header keywords ``MJDREFI``, ``MJDREFF`` -- Reference time
  * Header keywords ``TSTART``, ``TSTOP`` -- MET
  * ``TSTART_STR``, ``TSTOP_STR`` -- UTC or TT str -> TIMESYS.
  * ``TIMESYS``, ``TIMEREF`` -- need it?
* :ref:`iact-gti`:

  * Table columns: ``TSTART``, ``TSTOP``, MET
  * Header keywords: ``MJDREFI``, ``MJDREFF`` -- Reference time

* :ref:`obs-index`

  * Column ``TSTART``, ``TSTOP``, ``TMID`` -- MET
  * Column ``TSTART_STR``, ``TSTOP_STR``, ``TMID_STR`` -- UTC string
  * Header keywords ``MJDREFI``, ``MJDREFF`` -- Reference time
  * Header keywords ``TIMEUNIT``, ``TIMESYS``

.. _time-tools:

Tools
-----

Here's a summary of how gamma-ray science tool codes handle times.

Fermi Science Tools
+++++++++++++++++++

The Fermi Science tools (e.g. `gtselect`_) support only Fermi-LAT MET for user
input / output (and probably also just use MET internally).
Some info on other time scales and formats is given on a docs
page at `Time in Fermi data analysis`_, converting to MET is left up to the user.
Note that no leap second table is in the code, i.e. MET -- UTC conversions are
not supported (one can use Astropy for this though).

* TODO: Is this correct? How does the software store times internally?

TODO: We should also document what time scales and formats are supported by the
Fermi-LAT data selection tool:

* http://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi
* http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#observationDates
* http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#timeSystem

This is the equivalent of our :ref:`obs-index` format and observation selection
tools and unless there's a good reason not to we should just adopt whatever
Fermi-LAT does here.

Gammalib / ctools
+++++++++++++++++

The ctools (e.g. `ctselect`_) use MET for user input (the reference time is taken
from the event list header). Internally a time is represented as a ``GTime`` object,
which has a time scale (supports JD, MJD, TT, UTC, leap second table in the library code)
and supports different formats (including parsing ISO and ISOT strings).
Internally times are stored as 64-bit float METs wrt. a single reference time
defined by Gammalib. See `Times in Gammalib`_.

TODO: this means that TIME columns in event lists are
converted to that reference time on file read or attribute access?

Astropy / Gammapy
+++++++++++++++++

As already mentioned above, the `Astropy time`_ package contains the ``Time``
class, which supports all common scales and formats.
Internally times are stored as two 64-bit floats.

TODO: describe how MET values from event list ``TIME`` columns are converted
to that internal format on read / write in ``gammapy.time``.
TODO: where do they store leap seconds / how are those updated?

Examples
--------

TODO: write a set of tests doing equivalent time computations using Gammalib and
Astropy time (or possibly Gammapy wrappers where useful).
