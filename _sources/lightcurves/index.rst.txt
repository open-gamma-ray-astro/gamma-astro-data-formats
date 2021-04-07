.. _lc:

Light curves
============

For light-curves, we recommend to store the information in an as
similar format as possible to the one for :ref:`spectra` and specifically :ref:`flux-points`.

For measurements at a given time, a ``TIME`` column should be added,
for measurements for a given time interval, ``TIME_MIN`` and ``TIME_MAX``
columns should be added.

As explained in :ref:`time`, times should be given as 64-bit floats,
using the FITS time standard to specify a reference time point.
Note that this allows some flexibility, and e.g. the commonly used
"MJD values" for light curves are supported via these header keys::

    MJDREFI =  0
    MJDREFF =  0
    TIMEUNIT= 'd'

Light curve producers are highly encouraged to always give the ``TIMESYS``.
For archival data this is often not given, and it's unclear if the times
are e.g. in the ``UTC`` or ``TT`` or some other ``TIMESYS``.

This is a very preliminary description, based on the discussion here:
https://github.com/open-gamma-ray-astro/gamma-astro-data-formats/pull/61

If someone has time to provide a more detailed description, and to produce
example files in FITS or possibly also ECSV format, this would be highly welcome.
