.. include:: ../../references.txt

PSF OGIP
========

This is a PSF FITS format we agree on for IACTs.
This file contains the energy * offset dependent table distribution of the PSF from monte carlo simulations. 
So far, there is no plan to implement any kind of smoothing before exporting. 

Reference: http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_020/cal_gen_92_020.html

For IACTs, the only difference from the OGIP format is the added dimension of camera offset (Theta), similar to the other IRFs. 

The psf-histo-offset-energy format
----------------------------------

* PRIMARY HDU -- empty
* PSF HDU
    * RAD_LO -- 1D (deg)    (offset angle from source position) 
    * RAD_HI -- 1D (deg)
    * ENERGY_LO -- 1D (TeV)  (photon energy)
    * ENERGY_HI -- 1D (TeV)
    * THETA_LO -- 1D (deg)   (offset angle from camera center)
    * THETA_HI -- 1D (deg) 
    * PSFPDF -- 3D (deg^-2), shape = (len(THETA) x len(ENERGY) x len(RAD))


Example data file: :download:`psf-histo-offset-energy.fits.gz`

Was generated with this script: :download:`make-test-file.py`

TODO: update these files with the slightly modified ones we use for H.E.S.S. data


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
