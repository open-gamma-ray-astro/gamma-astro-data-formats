# PSF Histo Offset Energy Format Spec

This is a PSF FITS format we agree on for IACTs.

## Fermi gtpsf format

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
 
## The psf-histo-offset-energy format

The difference is that we add an axis for the field of view offset
and put the `Theta` array in the `PSF` HDU:

* PRIMARY HDU -- empty
* PSF HDU
  * Theta -- 1D (deg)
  * Energy -- 1D (MeV)
  * Exposure -- 1D (cm^2 s)
  * Offset -- 1D (deg)
  * Psf -- 3D (sr^-1), shape = (len(Energy) x len(Theta) x len(Offset))

  See `psf-histo-offset-energy.fits` as a valid example file.
