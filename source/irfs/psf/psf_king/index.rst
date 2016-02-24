.. include:: ../../../references.txt

.. _psf_king:

``psf_king`` format
===================

The King function parametrisations for PSFs has been in use in astronomy
as an analytical PSF model for many instruments, for example
by the Fermi-LAT (see `2013ApJ...765...54A`_).

The distribution has two parameters ``GAMMA`` :math:`\gamma` and ``SIGMA`` :math:`\sigma`
and is given by the following formula:

.. math::

   dP/d\Omega(r,\sigma,\gamma) =
   \frac{1}{2\pi\sigma^2}
   \left(1-\frac{1}{\gamma}\right)
   \left(1+\frac{r^2}{2\gamma\sigma^2}\right)^{- \gamma}

This formula integrates to 1 (see :ref:`psf-intro`).

Columns:

* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``GAMMA`` -- ndim: 2, unit: none
    * Model parameter (see formula above)
* ``SIGMA`` -- ndim: 2, unit: deg
    * Model parameter (see formula above)

The ``GAMMA`` and ``SIGMA`` arrays are 2-dimensional:
* Axis order: THETA, ENERGY
* Shape: (len(THETA), len(ENERGY))

Header keywords: none

Example data file: TODO: add HESS HAP example file as soon as available.
