.. include:: ../../references.txt

.. _flux-points:

SED
===

The SED format is a flexible specification for representing
one-dimensional spectra (distributions of amplitude vs. energy).  The
SED is structured as a table with one row per energy bin/point and
columns for the energy, measured normalization, and normalization
errors.  The format supports both integral and differential
representations of the normalization as described in
:ref:`norm_representations`.

The list of supported columns is given in the :ref:`sed_columns` section.
All columns are optional by default, and an SED may contain any
combination of the allowed columns.  :ref:`sed_types` are a
specification for defining groups of columns that are required to be
present in the file.  The :ref:`likelihood_sed` format is an example
of an SED type that contains both measured flux points and the profile
likelihoods versus normalization in each energy bin.

The SED format does not enforce a specific set of units but units
should be defined in the column metadata for all quantities with
physical dimensions.  Recommended units are provided in the
:ref:`sed_columns` section to indicate the dimensionality of each column.

The intended serialization format is a FITS BINTABLE with one row per
energy bin.  However any serialization format that supports tabular
data and column metadata could also be supported (e.g. ECSV or HDF5).
Because the SED occupies a single HDU multiple SEDs can be written to
a single FITS file with an identifier (e.g. source name or observation
epoch) used as the HDU name.  Sample FITS and ECSV files are provided
in :ref:`sample_files`.

.. _norm_representations:

Normalization Representation
----------------------------

The SED format supports both differential and integral representations
of the source normalization.  Integral representations correspond to
quantities integrated over an energy bin as defined by the ``E_MIN``
and ``E_MAX`` columns.  Differential representations are quantities
evaluated at a discrete energies defined by the ``E_REF`` column.  The
supported :ref:`norm_columns` are:

* ``DNDE`` : Differential photon flux at ``E_REF``. Dimensionality:
  photons / (time * area * energy)
* ``RATE`` : Photon rate between ``E_MIN`` and ``E_MAX``. Dimensionality:
  photons / time.
* ``FLUX`` : Photon flux (integral of ``DNDE``) between ``E_MIN`` and
  ``E_MAX``. Dimensionality: photons / ( time * area )
* ``EFLUX`` : Energy flux (integral of E times ``DNDE``) between
  ``E_MIN`` and ``E_MAX``. Dimensionality: energy / ( time * area )
* ``NPRED`` : Photon counts between ``E_MIN`` and ``E_MAX``.
  Dimensionality: photons
* ``NORM`` : Normalization in units of the reference model.
  Dimensionality: unitless

An SED should contain at least one of the normalization
representations listed above.  Multiple representations (e.g. ``FLUX``
and ``DNDE``) may be included in a single SED.

Errors and upper limits on the normalization are defined with the
:ref:`error_columns` by appending the appropriate suffix to the
normalization column name.  For example in the case of photon flux the
error and upper limit columns are:

* ``FLUX_ERR`` : Symmetric 1-sigma error.
* ``FLUX_ERRP`` : Asymmtric 1-sigma positive error.
* ``FLUX_ERRN`` : Asymmtric 1-sigma negative error.
* ``FLUX_UL`` : Upper limit with confidence level given by ``UL_CONF``
  header keyword.

.. _ref_model:

Reference Model
---------------

The *reference model* of an SED is the global parameterization that
was used to extract the normalization in each energy bin.  The choice
of reference model is relevant when considering models that
are rapidly changing across a bin or when energy dispersion is large
relative to the bin size.  The :ref:`refmodel_columns` define the
reference model in different representations.  When an SED includes a
reference model, the normalizations, errors, and upper limits can be
given in the ``NORM`` representation which is expressed in units of
the reference model.  ``NORM`` columns can be converted to another
representation by performing an element-wise multiplication of the
column with the ``REF`` column of the desired representation.

.. _likelihood:

Likelihood Profiles
-------------------

The :ref:`like_columns` contain values of the model likelihood and
likelihood profiles versus normalization.  Likelihood profiles provide
additional information about the measurement uncertainty in each bin.
A more detailed discussion of the motivation for SED likelihood
profiles can be found in :ref:`likelihood_sed`.

.. _sed_types:

SED Types
---------

By default all columns in the SED format are optional.  To facilitate
interoperability of files produced by different packages/tools, the
SED format defines an *SED Type* string which is set with the
``SED_TYPE`` header keyword.  The SED type defines a minimal set of
columns that must be present in the SED.  The SED types and their
required columns are given in the following list:

* ``DIFF_FLUX_POINTS``: ``E_REF``, ``DNDE``, ``DNDE_ERR``
* ``INT_FLUX_POINTS``: ``E_MIN``, ``E_MAX``, ``FLUX``, and ``FLUX_ERR``
* ``LIKELIHOOD``: See :ref:`likelihood_sed`.

.. _sample_files:
  
Sample Files
------------

* Differential Flux Points: :download:`FITS <diff_flux_points.fits>` :download:`ECSV <diff_flux_points.ecsv>`
* Integral Flux Points: :download:`FITS <int_flux_points.fits>` :download:`ECSV <int_flux_points.ecsv>`
* H.E.S.S. 1ES0229 Spectrum: :download:`FITS <1es0229_hess_spectrum.fits>` :download:`ECSV <1es0229_hess_spectrum.ecsv>`

Header Keywords
---------------

* ``UL_CONF``, **optional**
    * Confidence level of the upper limit given in the ``NORM_UL`` column.

* ``SED_TYPE``, **optional**
    * SED type string (see :ref:`sed_types` for more details).

.. _sed_columns:
      
Columns
-------

.. _energy_columns:

Energy Columns
~~~~~~~~~~~~~~

* ``E_MIN`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * ucd : ``em.energy``
    * Lower edge of energy bin.  This defines the lower integration
      bound for integral representations of the normalization.
* ``E_MAX`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * ucd : ``em.energy``
    * Upper edge of energy bin.  This defines the upper integration
      bound for integral representations of the normalization.
* ``E_REF`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * ucd : ``em.energy``
    * Energy at which differential representations of the normalization
      are evaluated (e.g. ``DNDE``).  This can be the geometric center
      of the bin or some weighted average of the energy distribution
      within the bin.

.. _norm_columns:
      
Normalization Columns
~~~~~~~~~~~~~~~~~~~~~
      
* ``NORM`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Measured normalization in units of the reference model.  
* ``DNDE`` -- ndim: 1, unit: ph / (cm2 s MeV)
    * Dimension: nebins
    * ucd : ``phot.flux.density``
    * Measured differential photon flux at ``E_REF``. 
* ``FLUX`` -- ndim: 1, unit: ph / (cm2 s)
    * Dimension: nebins
    * ucd : ``phot.count``
    * Measured photon flux between ``E_MIN`` and ``E_MAX``.
* ``EFLUX`` -- ndim: 1, unit: MeV / (cm2 s)
    * Dimension: nebins
    * ucd : ``phot.flux``
    * Measured energy flux between ``E_MIN`` and ``E_MAX``.
* ``NPRED`` -- ndim: 1, unit: ph
    * Dimension: nebins
    * Measured counts between ``E_MIN`` and ``E_MAX``.

.. _error_columns:
      
Error Columns
~~~~~~~~~~~~~

The error columns define the error and upper limit for a given
representation of the normalization.  In the following column
specifications ``{NORM_REP}`` indicates a placeholder for the name of
the normalization column (e.g. ``FLUX_ERR``).

* ``{NORM_REP}_ERR`` -- ndim: 1
    * Dimension: nebins
    * Symmetric error on the normalization in the representation
      ``{NORM_REP}``.
* ``{NORM_REP}_ERRP`` -- ndim: 1
    * Dimension: nebins
    * Positive error on the normalization in the representation
      ``{NORM_REP}``.
* ``{NORM_REP}_ERRN`` -- ndim: 1
    * Dimension: nebins      
    * Negative error on the normalization in the representation
      ``{NORM_REP}``.  A negative or NaN value indicates that the
      negative error is undefined.
* ``{NORM_REP}_UL`` -- ndim: 1
    * Dimension: nebins
    * Upper limit on the normalization in the representation
      ``{NORM_REP}``.  The upper limit confidence level is specified
      with the ``UL_CONF`` header keyword.

.. _refmodel_columns:
      
Reference Model Columns
~~~~~~~~~~~~~~~~~~~~~~~
      
* ``REF_DNDE`` -- ndim: 1, unit: ph / (MeV cm2 s)
    * Dimension: nebins
    * Differential flux of reference model at the ``E_REF``.
* ``REF_EFLUX`` -- ndim: 1, unit: MeV / (cm2 s)
    * Dimension: nebins
    * Energy flux (integral of E times ``DNDE``) of reference model
      from ``E_MIN`` to ``E_MAX``.
* ``REF_FLUX`` -- ndim: 1, unit: ph / (cm2 s)
    * Dimension: nebins
    * Flux (integral of ``DNDE``) of reference model from ``E_MIN`` to ``E_MAX``.
* ``REF_DFDE_E_MIN`` -- ndim: 1, unit: ph / (MeV cm2 s)
    * Dimension: nebins
    * Differential flux of reference model at ``E_MIN``.
* ``REF_DFDE_E_MAX`` -- ndim: 1, unit: ph / (MeV cm2 s)
    * Dimension: nebins
    * Differential flux of reference model at ``E_MAX``.
* ``REF_NPRED`` -- ndim: 1, unit: counts
    * Dimension: nebins
    * Number of photon counts of reference model.

.. _like_columns:
      
Likelihood Columns
~~~~~~~~~~~~~~~~~~
      
* ``TS`` -- ndim: 1, unit: none
    * Dimension: nebins
    * Source test statistic in each energy bin defined as twice the
      difference between best-fit and null log-likelihood values.  In the
      asymptotic limit this is square of the significance.
* ``LOGLIKE`` -- ndim: 1, unit: none
    * Dimension: nebins
    * Log-Likelihood value of the best-fit model.
* ``LOGLIKE_NULL`` -- ndim: 1, unit: none
    * Dimension: nebins
    * Log-Likelihood value of the zero normalization model.
* ``{NORM_REP}_SCAN`` -- ndim: 2, unit: None
    * Dimension: nebins x nnorms
    * Likelihood scan points in each energy bin in the representation
      ``{NORM_REP}``.       
* ``DLOGLIKE_SCAN`` -- ndim: 2, unit: none
    * Dimension: nebins x nnorms
    * Scan over delta LogLikelihood value vs. normalization in each
      energy bin.  The Delta-Loglikelihood is evaluated with respect
      to the zero normalization model (``LOGLIKE_NULL``).
