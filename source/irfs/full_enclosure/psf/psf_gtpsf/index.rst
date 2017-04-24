.. include:: ../../../../references.txt

.. _psf_gtpsf:

``gtpsf``
==============

The FITS file has the following BinTable HDUs / columns:

* PRIMARY HDU -- empty
* PSF HDU
    * Energy -- 1D (MeV)
    * Exposure -- 1D (cm^2 s)
    * Psf -- 2D (sr^-1), shape = (len(Energy) x len(Theta))
      Point spread function value :math:`dP/d\Omega`, see :ref:`psf-pdf`.

* THETA HDU
    * Theta -- 1D (deg)

Header keywords:

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'PSF'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'GTPSF'  

Example data file: :download:`psf-fermi.fits`
