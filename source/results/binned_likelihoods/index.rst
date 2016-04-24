.. include:: ../../references.txt

.. _binned_likelihoods:

Binned Likelihood Profiles
==========================

This page describes formats for bin-by-bin likelihood profiles as
currently used in some LAT analyses.  


2D Binned Likelihood
--------------------

The 2D binned likelihood is a representation of the profile likelihood
for the normalization of a source vs. energy.  The 2D likelihood can
be used in the same way as a traditional SED but has the advantage
that it retains information about the shape of the likelihood function
around the likelihood maximum.  The proposed format is a BINTABLE with
the following columns:

* ``E_MIN`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * Lower edge of energy bin.
* ``E_MAX`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * Upper edge of energy bin.
* ``EFLUX`` -- ndim: 1, unit: MeV cm^{-2} s^{-1}
    * Dimension: nebins
    * Energy flux of best-fit source normalization integrated over the energy bin.
* ``DFDE`` -- ndim: 1, unit: MeV^{-1} cm^{-2} s^{-1}
    * Dimension: nebins
    * Differential flux of best-fit source normalization evaluated at
      the bin center.
* ``NPRED`` -- ndim: 1, unit: counts
    * Dimension: nebins
    * Number of predicted counts of best-fit source normalization.
* ``NORM_ERR`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Symmetric error on the source normalization.      
* ``NORM_ERRP`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Positive error on the source normalization.
* ``NORM_ERRN`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Negative error on the source normalization.
* ``NORM_UL`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Upper limit on the source normalization.            
* ``TS`` -- ndim: 1, unit: counts
    * Dimension: nebins
    * Source test statistic as a function of energy bin.
* ``DNLL_SCAN`` -- ndim: 2, unit: None
    * Dimension: nebins x nnorms
    * Delta negative LogLikelihood value vs. normalization.  The
      Delta-Loglikelihood is evaluated with respect to the maximum of
      the likelihood function in each energy bin.
* ``NLL_SCAN`` -- ndim: 2, unit: None
    * Dimension: nebins x nnorms
    * Absolute negative LogLikelihood value vs. normalization.
* ``NORMSCAN`` -- ndim: 2, unit: None
    * Dimension: nebins x nnorms
    * Normalization scan values in each energy bin expressed as the
      ratio with respect to the best-fit normalization.  Scan matrix
      can be multiplied by ``EFLUX``, ``DFDE``, or ``NPRED`` vectors
      to get the normalization in the respective units.
      
TS Cube
-------

Recent releases of the Fermi ScienceTools provide a *gttscube*
application which can be used to fit a test source as a function of
energy and spatial position within the ROI.  The output of this tool
is a FITS file containing maps that encode the fit results.  The
PRIMARY HDU contains the same output as *gttsmap* -- a 2-dimensional
map with the test source test statistic evaluated at each spatial
pixel.  The other HDUs contain information about the fit results in
individual energy planes.  The SCANDATA HDU contains the full
information about the likelihood scan in each energy bin and spatial
pixel and can be used to reconstruct the likelihood for an arbitrary
spectral model (not necessarily the test source model).  Here is the
list of HDUs:

.. csv-table:: TS Cube HDUs
   :header:    HDU, HDU Type, HDU Name, Dimensions, Description
   :file: tscube_hdus.csv
   :delim: |
   :widths: 10,10,10,10,80

The EBOUNDS HDU is a table with 1 row per energy bin and the following
columns:

* ``E_MIN``, unit: keV
    * Lower edge of energy bin.
* ``E_MAX``, unit: keV
    * Upper edge of energy bin.
* ``E_MIN_FL``
    * Differential flux evaluated at the lower edge of the energy bin.
* ``E_MAX_FL``
    * Differential flux evaluated at the upper edge of the energy bin.
* ``NPRED``
    * Number of predicted counts in the energy bin.
  
The SCANDATA HDU is a table with 1 row per spatial pixel and the
following columns:

* ``NLL_SCAN`` -- ndim: 2, unit: None
    * Dimension: nebins X nnorms
    * Normalization values for the test source.
* ``NORMSCAN`` -- ndim: 2, unit: None
    * Dimension: nebins X nnorms
    * Negative log-likelihood values.

