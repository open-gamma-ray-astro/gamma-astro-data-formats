.. include:: ../../../references.txt

.. _psf_3gauss:

``psf_3gauss`` format
=====================

In this format we store the :math:`scale`, :math:`\sigma` and :math:`A`
parameters from a triple-Gauss parametrisation:

.. math::

   dP/d\Omega(r,\sigma,\gamma) =
   \frac{1}{2\pi\sigma^2}
   \left(1-\frac{1}{\gamma}\right)
   \left(1+\frac{r^2}{2\gamma\sigma^2}\right)^{- \gamma}



TODO: comment on normalisation

.. note::

    By setting the amplitudes of the 3rd (and 2nd) Gaussians to 0 one can
    implement double (or single) Gaussian models as well. 

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- 1D, unit: TeV
    * Energy axis
* ``THETA_LO``, ``THETA_HI`` -- 1D, unit: deg
    * Field of view offset axis
* ``SCALE`` -- 1D, unit: none
    * Absolute scale of the 1st Gaussian
* ``SIGMA_1`` -- 1D, unit: deg
    * Sigma of the 1st Gaussian
* ``AMPL_2`` -- 1D, unit: none
    * Relative amplitude of the 2nd Gaussian with respect to the 1st Gaussian
* ``SIGMA_2`` -- 1D, unit: deg
    * Sigma of the 2nd Gaussian
* ``AMPL_3`` -- 1D, unit: none
    * Relative amplitude of the 3rd Gaussian with respect to the 1st Gaussian
* ``SIGMA_3`` -- 1D, unit: deg
    * Sigma of the 3rd Gaussian

Header keywords: none

Example data file: TODO: add HESS HAP example file as soon as available.
