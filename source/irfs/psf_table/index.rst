.. include:: ../../references.txt

.. _psf-table:

psf_table format
================

This is a PSF FITS format we agree on for IACTs.
This file contains the offset- and energy-dependent table distribution of the PSF.

This format is almost identical to the `OGIP format for radial point spred function datasets
<http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_020/cal_gen_92_020.html>`__
The differences are that we don't have the dependency on azimuthal field of view position and the
units are different.

* ``RAD_LO``, ``RAD_HI`` -- 1D, unit: deg
    * Offset angle from source position
* ``THETA_LO``, ``THETA_HI`` -- 1D, unit: deg
    * Field of view offset axis
* ``ENERG_LO``, ``ENERG_HI`` -- 1D, unit: TeV
    * Energy axis
* ``RPSF`` -- 3D (deg^-2), shape = (len(RAD), len(THETA), len(ENERGY))
    * Probability density (probability per solid angle),
      see info on normalisation below.
    * Axis order: RAD, THETA, ENERGY


Some comments:

* Usually the PSF is derived from Monte Carlo simulations, but in principle
  it can be estimated from bright point sources (AGN) as well.
* Tools should assume the PSF is well-sampled and noise-free.
  I.e. if limited event statistics in the PSF computation is an issue,
  it is up to the PSF producer to denoise it to an acceptable level.


Example data file: TODO: add HESS HAP example file as soon as available.

Normalisation
+++++++++++++

Like the Fermi PSF, we require that the PSF `P` is normalised
to integrate to 1, i.e.

.. math::

    \int_{0}^{\infty} 2 \pi r P(r) dr = 1

This implies that the PSF producer is responsible for choosing the Theta
range and normalising. I.e. it's OK to choose a theta range that contains
only 95% of the PSF, and then the integral will be 0.95.

We recommend everyone store PSFs so that truncation is completely negligible,
i.e. the containment should be 99% or better for all of parameter space.
