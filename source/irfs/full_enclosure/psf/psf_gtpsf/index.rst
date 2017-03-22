.. include:: ../../../../references.txt

.. _psf_gtpsf_full:

``gtpsf_full``
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

* ``HDUCLAS1`` type: string
    * First extension class (option: 'RESPONSE').
* ``HDUCLAS2`` type: string
    * Second extension class (option: 'RPSF').
* ``HDUCLAS3`` type: string
    * Third extension class (option: 'FULL-ENCLOSURE').
* ``HDUCLAS4`` type: string
    * Fourth extension class (option: 'gtpsf').
* ``HDU_DOC = TODO``

Example data file: :download:`psf-fermi.fits`
