.. include:: ../../references.txt

.. _psf_king:

``psf_king`` format
===================

In this format we store the gamma :math:`\gamma` and sigma :math:`\sigma`
parameters from a King function parametrisation:

.. math::

   P(r,\sigma,\gamma) =
   \frac{1}{2\pi\sigma^2}
   \left(1-\frac{1}{\gamma}\right)
   \left(1+\frac{r^2}{2\gamma\sigma^2}\right)^{- \gamma}

This formula integrates to 1.


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
