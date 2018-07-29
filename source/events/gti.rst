.. include:: ../references.txt

.. _iact-gti:

GTI
===

The ``GTI`` extension is a binary FITS table that contains the Good Time
Intervals ('GTIs') for the event list. A general description of GTIs can
be found in the `OGIP GTI`_ standard.

This HDU contains two mandatory columns named ``START`` and ``STOP``. At
least one row is containing the start and end time of the observation must
be present. The values are in units of seconds with respect to the reference
time defined in the header (keywords MJDREFI and MJDREFF). This extension
allows for a detailed handling of good time intervals (i.e. excluding periods
with cloud cover or lightning during one observation).

High-level Science tools could modify the GTIs according to user parameter.
See e.g. `gtmktime`_ for an application example from the Fermi Science Tools.

Mandatory columns
-----------------

* ``START`` type: float64, unit: s
    * Start time of good time interval (see :ref:`time`)
* ``STOP`` type: float64, unit: s
    * End time of good time interval (see :ref:`time`)


Mandatory header keywords
-------------------------

The standard FITS reference time header keywords should be used (see :ref:`time-formats`).
