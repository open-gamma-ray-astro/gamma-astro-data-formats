.. include:: ../../references.txt

PSF OGIP
========

This is a PSF FITS format we agree on for IACTs.

Reference: http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_020/cal_gen_92_020.html

TODO: describe differences / format we use for IACTs

The psf-histo-offset-energy format
----------------------------------

The difference is that we add an axis for the field of view offset
and put the `Theta` array in the `PSF` HDU:

* PRIMARY HDU -- empty
* PSF HDU
    * Theta -- 1D (deg)
    * Energy -- 1D (MeV)
    * Exposure -- 1D (cm^2 s)
    * Offset -- 1D (deg)
    * Psf -- 3D (sr^-1), shape = (len(Energy) x len(Theta) x len(Offset))

TODO: think about axis order and specify it in an understandable way.

Example data file: :download:`psf-histo-offset-energy.fits.gz`

Was generated with this script: :download:`make-test-file.py`


Normalisation
+++++++++++++

Like the Fermi PSF, we require that the PSF `P` is normalised
to integrate to 1, i.e.
```
int_0_inf 2 * pi * r * P(r) dr = 1
```
This implies that the PSF producer is responsible for choosing the Theta
range and normalising. I.e. it's OK to choose a theta range that contains
only 95% of the PSF, and then the integral will be 0.95.

We recommend everyone store PSFs so that truncation is completely negligible,
i.e. the containment should be 99% or better for all of parameter space.
