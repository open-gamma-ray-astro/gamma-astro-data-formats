.. include:: ../../../references.txt

.. _psf:

Point spread function
=====================

.. _psf-intro:

Introduction
------------

The point spread function (PSF) (`Wikipedia - PSF`_) represents the spatial probability
distribution of reconstructed event positions for a point source.
So far we're only considering radially symmetric PSFs here.

.. _psf-pdf:

Probability distributions
+++++++++++++++++++++++++

* :math:`dP/d\Omega(r)`, where :math:`dP` is the probability to find an event
  in a solid angle :math:`d\Omega` at an offset :math:`r` from the point source.
  This is the canonical form we use and the values we store in files.
* Often, when comparing observered event distributions with a PSF model,
  the :math:`dP/dr^2` distributions in equal-width bins in :math:`r^2` is
  used. The relation is :math:`d\Omega = \pi dr^2`, i.e. :math:`dP/dr^2=(1/\pi)(dP/d\Omega)`.
* Sometimes, the distribution :math:`dP/dr(r)` is used.
  The relation is :math:`dP/dr = 2 \pi r dP/d\Omega`.

TODO: explain "encircled energy" = "encircled counts" = "cumulative" representation
of PSF and define containment fraction and containment radius.

Normalisation
+++++++++++++

PSFs must be normalised to integrate to total probability 1, i.e.

.. math::

    \int_{0}^{\infty} 2 \pi r dP/dr(r) dr = 1, where dP/dr = 2 \pi r dP/d\Omega

    
This implies that the PSF producer is responsible for choosing the Theta
range and normalising. I.e. it's OK to choose a theta range that contains
only 95% of the PSF, and then the integral will be 0.95.

We recommend everyone store PSFs so that truncation is completely negligible,
i.e. the containment should be 99% or better for all of parameter space.


Comments
++++++++

* Usually the PSF is derived from Monte Carlo simulations, but in principle
  it can be estimated from bright point sources (AGN) as well.
* Tools should assume the PSF is well-sampled and noise-free.
  I.e. if limited event statistics in the PSF computation is an issue,
  it is up to the PSF producer to denoise it to an acceptable level.


PSF formats
-----------

.. toctree::

   psf_table/index
   psf_3gauss/index
   psf_king/index
   psf_gtpsf/index
