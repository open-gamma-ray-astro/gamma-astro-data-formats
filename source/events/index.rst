.. include:: ../references.txt

IACT event lists
================

This document describes IACT DL3 event lists.

Event lists are stored in FITS files with two required and one optional
extensions (HDUs).

* Suggested filename: ``events_OBS_ID.fits.gz``
* Suggested HDU name events: ``EVENTS``
* Suggested HDU name good time intervals: ``GTI``
* Suggested optional HDU name telescope array: ``TELARRAY``

.. include:: events.rst
.. include:: gti.rst
