.. include:: ../../../references.txt

.. _psf_king:

``psf_king`` format
===================

The King function parametrisations for PSFs has been in use in astronomy
as an analytical PSF model for many instruments, for example
by the Fermi-LAT (see `2013ApJ...765...54A`_).

The distribution has to parameters gamma :math:`\gamma` and sigma :math:`\sigma`
and is given by the following formula:

.. math::

   dP/d\Omega(r,\sigma,\gamma) =
   \frac{1}{2\pi\sigma^2}
   \left(1-\frac{1}{\gamma}\right)
   \left(1+\frac{r^2}{2\gamma\sigma^2}\right)^{- \gamma}

This formula integrates to 1 (see :ref:`psf-intro`).

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- 1D, unit: TeV
    * Energy axis
* ``THETA_LO``, ``THETA_HI`` -- 1D, unit: deg
    * Field of view offset axis
* ``GAMMA`` -- 1D, unit: none
    * gamma parameter of the King-Function 
* ``SIGMA`` -- 1D, unit: deg
    * sigma parameter of the King-Function

Header keywords: none

Example data file: TODO: add HESS HAP example file as soon as available.
