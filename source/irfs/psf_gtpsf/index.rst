.. include:: ../../references.txt

.. _psf_gtpsf:

``gtpsf`` format
================

The FITS file has the following BinTable HDUs / columns:

* PRIMARY HDU -- empty
* PSF HDU
    * Energy -- 1D (MeV)
    * Exposure -- 1D (cm^2 s)
    * Psf -- 2D (sr^-1), shape = (len(Energy) x len(Theta))
* THETA HDU
    * Theta -- 1D (deg)

Example data file: :download:`psf-fermi.fits`
