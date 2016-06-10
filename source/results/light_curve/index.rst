.. include:: ../../references.txt

.. _lightcurve:

Light curve
===========

.. warning::

   This is a first draft proposal.
   The format is likely to change.
   Please give feedback!

Introduction
------------

The light curve format specified here is a simple table where each row
represents the ``FLUX`` measurement of a given astronomical object at a given
``TIME``.

* If you have multiple light curves, e.g. from different instruments or energy bands,
  you can use multiple tables in this format.
* To specify the ``TIME``, ``MJD`` values in the ``TT`` system should be used.
* The flux is allowed to be a differential or integral flux, as long as the units
  are given correctly. All of these are valid:
    * ``cm^-2 s^-1`` (integral flux)
    * ``m^-2 s^-1 TeV^-1`` (differential flux)
    * ``cm^-2 s^-1 MeV^-1`` (differential flux)
* For integral fluxes, the energy band should be specified via the ``E_MIN`` and
  ``E_MAX`` header keywords. For differential fluxes, the ``E_REF`` header keyword
  should be used.
* For upper limits, the ``FLUX`` field should be set to ``NaN``.


Required columns
----------------

* ``TIME`` type: float64, unit: s
    * MJD time in TT system
* ``FLUX`` type: float, unit: flexible
    * Flux (see notes on units above)

Optional columns
----------------

* ``TIME_MIN``, ``TIME_MAX`` type: float64, unit: s
    * Start and end of time bin (MJD, TT)
* ``FLUX_ERR`` type: float, unit: flexible
    * Flux error (1 sigma) (see notes on units above)
* ``FLUX_UL`` type: float, unit: flexible
    * Flux upper limit (at ``UL_CONF`` level) (see notes on units above)


Required header keywords
------------------------

None.

Optional header keywords
------------------------

* ``E_MIN``, ``E_MAX`` -- type: float, unit: TeV
    * Energy band of the flux measurement
* ``UL_CONF``
    * Confidence level of the upper limit given in the ``FLUX_UL`` column.
* ``OBJECT`` type: string
    * Observed object
* ``TELESCOP`` type: string
    * Telescope

Example files
-------------

TODO: Make an example FITS file in this format.

Existing light curve providers (not in this format though):

* http://vobs.magic.pic.es/fits/
* http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2yr_catalog/ap_lcs.php (uses MJD only)
* http://fermi.gsfc.nasa.gov/ssc/data/access/lat/msl_lc/ (uses MET only)
* http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermilasp.html (uses MET and JD)
