.. include:: ../../../../references.txt

.. _psf_gtpsf:

``gtpsf``
=========

The FITS file has the following BinTable HDUs / columns:

* PRIMARY HDU -- empty
* PSF HDU
    * Energy -- 1D (MeV)
    * Exposure -- 1D (cm^2 s)
    * Psf -- 2D (sr^-1), shape = (len(Energy) x len(Theta))
      Point spread function value :math:`dP/d\Omega`, see :ref:`psf-pdf`.

* THETA HDU
    * Theta -- 1D (deg)

Header keywords: none


Example data file: :download:`psf-fermi.fits`
