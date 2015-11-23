PSF Histo Offset Energy Format Spec
===================================

This is a PSF FITS format we agree on for IACTs.

Fermi gtpsf format
------------------

The format we're about to define is very similar to the [gtpsf](http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/help/gtpsf.txt)
format (which is supported in Gammapy via the [EnergyDependentTablePSF](https://gammapy.readthedocs.org/en/latest/api/gammapy.irf.EnergyDependentTablePSF.html) class).

The FITS file has the following BinTable HDUs / columns:

* PRIMARY HDU -- empty
* PSF HDU
  * Energy -- 1D (MeV)
  * Exposure -- 1D (cm^2 s)
  * Psf -- 2D (sr^-1), shape = (len(Energy) x len(Theta))
* THETA HDU
  * Theta -- 1D (deg)
 
 See `psf-fermi.fits` as a valid example file.
 
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

Normalisation
+++++++++++++

See `psf-histo-offset-energy.fits` as a valid example file.

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
