.. include:: ../references.txt

Instrument response functions (IRFs)
====================================

The instrument response function (IRF) formats currently in use
for imaging atmospheric Cherenkov telescopes (IACTs) are FITS
BinTables with a single row and array columns.
The format was based on and is similar to the one use by Fermi-LAT IRFs.
See :ref:`fits-arrays`.

At the moment (November 2015), this format is used by H.E.S.S. and
VERITAS and supported by Gammapy and Gammalib, yet there is no publicly available document or webpage
describing or defining the format, so we'll describe it in detail here.

Note that a different FITS format has been proposed for CTA:
http://adsabs.harvard.edu/abs/2015arXiv150807437W
As far as we know, this format is currently not (yet?) supported by any
analysis package.

Specific IRFs
-------------

TODO: Copy over the format summary and desriptions from here:
https://gammapy.readthedocs.org/en/latest/dataformats/index.html#overview

Table of contents
-----------------

.. toctree::

   psf-histo-offset-energy/index
