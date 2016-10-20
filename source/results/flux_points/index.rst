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
:ref:`sed_columns` section to indicate the dimensionality of each
column.  Column UCDs are intended for defining the type of physical
quantity associated to each column (e.g. energy, photon flux, etc.).
The convention for including UCDs in the column metdata is still under
discussion and the UCDs defined in the current format are optional.

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
quantities integrated over an energy bin as defined by the ``e_min``
and ``e_max`` columns.  Differential representations are quantities
evaluated at a discrete energies defined by the ``e_ref`` column.  The
supported :ref:`norm_columns` are:

* ``dnde`` : Differential photon flux at ``e_ref``. Dimensionality:
  photons / (time * area * energy)
* ``RATE`` : Photon rate between ``e_min`` and ``e_max``. Dimensionality:
  photons / time.
* ``flux`` : Photon flux (integral of ``dnde``) between ``e_min`` and
  ``e_max``. Dimensionality: photons / ( time * area )
* ``eflux`` : Energy flux (integral of E times ``dnde``) between
  ``e_min`` and ``e_max``. Dimensionality: energy / ( time * area )
* ``npred`` : Photon counts between ``e_min`` and ``e_max``.
  Dimensionality: photons
* ``norm`` : Normalization in units of the reference model.
  Dimensionality: unitless

An SED should contain at least one of the normalization
representations listed above.  Multiple representations (e.g. ``flux``
and ``dnde``) may be included in a single SED.

Errors and upper limits on the normalization are defined with the
:ref:`error_columns` by appending the appropriate suffix to the
normalization column name.  For example in the case of photon flux the
error and upper limit columns are:

* ``flux_err`` : Symmetric 1-sigma error.
* ``flux_errp`` : Asymmtric 1-sigma positive error.
* ``flux_errn`` : Asymmtric 1-sigma negative error.
* ``flux_ul`` : Upper limit with confidence level given by ``UL_CONF``
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
given in the ``norm`` representation which is expressed in units of
the reference model.  ``norm`` columns can be converted to another
representation by performing an element-wise multiplication of the
column with the ``ref`` column of the desired representation.

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

* ``diff_flux_points``: ``e_ref``, ``dnde``, ``dnde_err``
* ``int_flux_points``: ``e_min``, ``e_max``, ``flux``, and ``flux_err``
* ``likelihood``: See :ref:`likelihood_sed`.

.. _sample_files:
  
Sample Files
------------

* Differential Flux Points: :download:`FITS <diff_flux_points.fits>` :download:`ECSV <diff_flux_points.ecsv>`
* Integral Flux Points: :download:`FITS <int_flux_points.fits>` :download:`ECSV <int_flux_points.ecsv>`
* H.E.S.S. 1ES0229 Spectrum: :download:`FITS <1es0229_hess_spectrum.fits>` :download:`ECSV <1es0229_hess_spectrum.ecsv>`

Header Keywords
---------------

* ``UL_CONF``, **optional**
    * Confidence level of the upper limit given in the ``norm_ul`` column.

* ``SED_TYPE``, **optional**
    * SED type string (see :ref:`sed_types` for more details).

.. _sed_columns:
      
Columns
-------

.. _energy_columns:

Energy Columns
~~~~~~~~~~~~~~

* ``e_min`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * ucd : ``em.energy``
    * Lower edge of energy bin.  This defines the lower integration
      bound for integral representations of the normalization.
* ``e_max`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * ucd : ``em.energy``
    * Upper edge of energy bin.  This defines the upper integration
      bound for integral representations of the normalization.
* ``e_ref`` -- ndim: 1, unit: MeV
    * Dimension: nebins
    * ucd : ``em.energy``
    * Energy at which differential representations of the normalization
      are evaluated (e.g. ``dnde``).  This can be the geometric center
      of the bin or some weighted average of the energy distribution
      within the bin.

.. _norm_columns:
      
Normalization Columns
~~~~~~~~~~~~~~~~~~~~~
      
* ``norm`` -- ndim: 1, unit: None
    * Dimension: nebins
    * Measured normalization in units of the reference model.  
* ``dnde`` -- ndim: 1, unit: ph / (cm2 s MeV)
    * Dimension: nebins
    * ucd : ``phot.flux.density``
    * Measured differential photon flux at ``e_ref``. 
* ``flux`` -- ndim: 1, unit: ph / (cm2 s)
    * Dimension: nebins
    * ucd : ``phot.count``
    * Measured photon flux between ``e_min`` and ``e_max``.
* ``eflux`` -- ndim: 1, unit: MeV / (cm2 s)
    * Dimension: nebins
    * ucd : ``phot.flux``
    * Measured energy flux between ``e_min`` and ``e_max``.
* ``npred`` -- ndim: 1, unit: ph
    * Dimension: nebins
    * Measured counts between ``e_min`` and ``e_max``.

.. _error_columns:
      
Error Columns
~~~~~~~~~~~~~

The error columns define the error and upper limit for a given
representation of the normalization.  In the following column
specifications ``{NORM_REP}`` indicates a placeholder for the name of
the normalization column (e.g. ``flux_err``).

* ``{NORM_REP}_err`` -- ndim: 1
    * Dimension: nebins
    * Symmetric error on the normalization in the representation
      ``{NORM_REP}``.
* ``{NORM_REP}_errp`` -- ndim: 1
    * Dimension: nebins
    * Positive error on the normalization in the representation
      ``{NORM_REP}``.
* ``{NORM_REP}_errn`` -- ndim: 1
    * Dimension: nebins      
    * Negative error on the normalization in the representation
      ``{NORM_REP}``.  A negative or NaN value indicates that the
      negative error is undefined.
* ``{NORM_REP}_ul`` -- ndim: 1
    * Dimension: nebins
    * Upper limit on the normalization in the representation
      ``{NORM_REP}``.  The upper limit confidence level is specified
      with the ``UL_CONF`` header keyword.

.. _refmodel_columns:
      
Reference Model Columns
~~~~~~~~~~~~~~~~~~~~~~~
      
* ``ref_dnde`` -- ndim: 1, unit: ph / (MeV cm2 s)
    * Dimension: nebins
    * Differential flux of reference model at the ``e_ref``.
* ``ref_eflux`` -- ndim: 1, unit: MeV / (cm2 s)
    * Dimension: nebins
    * Energy flux (integral of E times ``dnde``) of reference model
      from ``e_min`` to ``e_max``.
* ``ref_flux`` -- ndim: 1, unit: ph / (cm2 s)
    * Dimension: nebins
    * Flux (integral of ``dnde``) of reference model from ``e_min`` to ``e_max``.
* ``ref_dnde_e_min`` -- ndim: 1, unit: ph / (MeV cm2 s)
    * Dimension: nebins
    * Differential flux of reference model at ``e_min``.
* ``ref_dnde_e_max`` -- ndim: 1, unit: ph / (MeV cm2 s)
    * Dimension: nebins
    * Differential flux of reference model at ``e_max``.
* ``ref_npred`` -- ndim: 1, unit: counts
    * Dimension: nebins
    * Number of photon counts of reference model.

.. _like_columns:
      
Likelihood Columns
~~~~~~~~~~~~~~~~~~
      
* ``ts`` -- ndim: 1, unit: none
    * Dimension: nebins
    * Source test statistic in each energy bin defined as twice the
      difference between best-fit and null log-likelihood values.  In the
      asymptotic limit this is square of the significance.
* ``loglike`` -- ndim: 1, unit: none
    * Dimension: nebins
    * Log-Likelihood value of the best-fit model.
* ``loglike_null`` -- ndim: 1, unit: none
    * Dimension: nebins
    * Log-Likelihood value of the zero normalization model.
* ``{NORM_REP}_scan`` -- ndim: 2, unit: None
    * Dimension: nebins x nnorms
    * Likelihood scan points in each energy bin in the representation
      ``{NORM_REP}``.       
* ``dloglike_scan`` -- ndim: 2, unit: none
    * Dimension: nebins x nnorms
    * Scan over delta LogLikelihood value vs. normalization in each
      energy bin.  The Delta-Loglikelihood is evaluated with respect
      to the zero normalization model (``loglike_null``).
