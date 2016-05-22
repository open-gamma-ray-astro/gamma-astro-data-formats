.. include:: ../../references.txt

.. _flux-points:

Flux points
===========

SED
---

This is a propsal for a flux point format that uses a subset of the
columns from the :ref:`likelihood_sed` format.  The SED is stored in a
BINTABLE with one row per energy bin (*nebins*).  The format itself
does not define a specific set of units but units are provided in the
list below to indicate the dimensionality of each column.  Because the
SED occupies a single HDU multiple SEDs could be written to a single
file with some identifier used as the HDU name.

Sample FITS files:

* Low Significance Source: :download:`sed_lowts.fits`
* High Significance Source: :download:`sed_hights.fits`

Header Keywords
~~~~~~~~~~~~~~~

* ``UL_CONF``, **optional**
    * Confidence level of the upper limit given in the ``NORM_UL`` column.
  
Required Columns
~~~~~~~~~~~~~~~~

* ``E_MIN`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * Lower edge of energy bin.
* ``E_MAX`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * Upper edge of energy bin.     
* ``E_REF`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * Bin reference energy that defines the energy at which
      ``REF_DFDE`` is evaluated.  This can be the geometric center of
      the bin or some weighted average of the energy distribution
      within the bin.
* ``REF_DFDE`` -- ndim: 1, unit: MeV^{-1} cm^{-2} s^{-1}
    * Dimension: nebins
    * Differential flux of reference model evaluated at the energy in ``E_REF``.
* ``REF_EFLUX`` -- ndim: 1, unit: MeV cm^{-2} s^{-1}
    * Dimension: nebins
    * Energy flux (integral of E x dF/dE) of reference model in the energy bin.
* ``REF_FLUX`` -- ndim: 1, unit: cm^{-2} s^{-1}
    * Dimension: nebins
    * Flux (integral of dF/dE) of reference model in the energy bin.      
* ``NORM`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Best-fit amplitude in units of the reference model amplitude.      
* ``NORM_ERR`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Symmetric error on the source normalization in units of the reference model amplitude.  


Optional Columns
~~~~~~~~~~~~~~~~

* ``REF_DFDE_E_MIN`` -- ndim: 1, unit: MeV^{-1} cm^{-2} s^{-1}
    * Dimension: nebins
    * Differential flux of reference model evaluated at the lower edge
      of the energy bin.
* ``REF_DFDE_E_MAX`` -- ndim: 1, unit: MeV^{-1} cm^{-2} s^{-1}
    * Dimension: nebins
    * Differential flux of reference model evaluated at the upper edge
      of the energy bin.
* ``REF_NPRED`` -- ndim: 1, unit: counts
    * Dimension: nebins
    * Number of predicted counts of reference model.
* ``NORM_ERRP`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Positive error on the source normalization in units of the reference model amplitude.
* ``NORM_ERRN`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Negative error on the source normalization in units of the
      reference model amplitude.  A negative or NaN value indicates
      that the negative error is undefined.
* ``NORM_UL`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Upper limit on the source normalization in units of the reference model amplitude.
* ``TS`` -- ndim: 1, unit: counts
    * Dimension: nebins
    * Source test statistic as a function of energy bin.
