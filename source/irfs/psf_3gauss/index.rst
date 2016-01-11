.. include:: ../../references.txt

.. _psf_3gauss:

``psf_3gauss`` format
=====================

In this format we store the gamma and sigma parameters resulting from a
King-Function fit.

* ``ENERG_LO``, ``ENERG_HI`` -- 1D, unit: TeV
    * Energy axis
* ``THETA_LO``, ``THETA_HI`` -- 1D, unit: deg
    * Field of view offset axis
* ``SCALE`` -- 1D, unit: none
    * absolute scale of the 1st Gaussian
* ``SIGMA1`` -- 1D, unit: deg
    * sigma of the 1st Gaussian
* ``AMPL_2`` -- 1D, unit: none
    * relative amplitude of the 2nd Gaussian with respect to the 1st Gaussian
* ``SIGMA2`` -- 1D, unit: deg
    * sigma of the 2nd Gaussian
* ``AMPL_3`` -- 1D, unit: none
    * relative amplitude of the 3rd Gaussian with respect to the 1st Gaussian
* ``SIGMA3`` -- 1D, unit: deg
    * sigma of the 3rd Gaussian
    
.. note::

    By setting the amplitudes of the 3rd (and 2nd) Gaussians to 0 one can implement double (or single) Gaussian models as well. 


Example data file: TODO: add HESS HAP example file as soon as available.
