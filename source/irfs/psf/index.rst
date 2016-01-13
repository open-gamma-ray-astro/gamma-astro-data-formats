.. include:: ../../references.txt

.. _psf:

Point spread function
=====================

Introduction
------------

The point spread function (PSF) (`Wikipedia - PSF`_) represents the spatial probability
distribution of reconstructed event positions for a point source.

So far we're only considering radially symmetric PSFs :math:`dP/d\Omega(r)`,
where ...




Radial PSF representations
--------------------------

\begin{equation}
\frac{dP}{d\theta^2}(\theta^2) = \sum_{i=1}^3 A_i \exp\left(-\frac{\theta^2}{2\sigma_i^2}\right),
\end{equation}
where $A_i$ and $\sigma_i$ are the weights and widths of the corresponding

.. math::

   P(r,\sigma,\gamma) =
   \frac{1}{2\pi\sigma^2}
   \left(1-\frac{1}{\gamma}\right)
   \left(1+\frac{r^2}{2\gamma\sigma^2}\right)^{- \gamma}



PSF formats
-----------

.. toctree::

   psf_table/index
   psf_3gauss/index
   psf_king/index
   psf_gtpsf/index
