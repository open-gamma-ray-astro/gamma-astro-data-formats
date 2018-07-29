.. include:: ../references.txt

IACT events
===========

This document describes the format to store DL3 event data for IACTs.

The main table is ``EVENTS``, which at the moment contains not only event
parameters, but also key information about the observation needed to analyse the
data such as the pointing position or the livetime.

The ``GTI`` table gives the "good time intervals". The ``EVENTS`` table should
match the ``GTI`` table, i.e. contain the relevant events within these time
intervals.

No requirement is stated yet whether event times must be sorted chronologically;
this is under discussion and might be added in a future version of the spec;
sorting events by time now when producing EVENTS tables is highly recommended.

The ``POINTING`` table defines the pointing position at given times, allowing to
interpolate the pointing position at any time. It currently isn't in use yet,
science tools access the pointing position from the EVENTS header and only
support fixed-pointing observations.

We note that it is likely that the EVENTS, GTI, and POINTING will change
significantly in the future. Discusssion on observing modes is ongoing, a new
HDU might be introduced that stores the "observation" (sometimes called "tech")
information, like e.g. the observation mode and pointing information. Other
major decision like whether there will be on set of IRFs per OBS_ID (like we
have now), or per GTI, is being discussed in CTA. Another discussion point is
how to handle trigger dead times. Currently science tools have to access
``DEADC`` or ``LIVETIME`` from the event header, and combine that with ``GTI``
if they want to analyse parts of observations. One option could be to absorb the
dead-time correction into the effective areas, another option could be to add
dead-time correction factors to GTI tables.

Without further ado, here is the current spec:

.. toctree::
   :maxdepth: 1

   events
   gti
   pointing
