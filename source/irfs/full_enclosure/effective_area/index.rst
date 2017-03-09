.. include:: ../../../references.txt

.. _iact-aeff:

Effective Area
==============

Within the IACT community, the effective area has been expressed following two
different methods: as a function of the true energy, and as a function of the
reconstructed energy. Both have been widely used and documented, and each of
them bring certain advantages and disadvantages:

* Using the effective area as a function of true energy, together with the energy
  dispersion, is the most precise alternative, although it requires enough MC
  statistics for the energy dispersion noise to be acceptable. In addition, the
  likelihood fits performed by the science tools are also slower following this
  approach.

* In the case of using the effective area as a function of reconstructed energy,
  results may be less precise, but require less MC statistics and allows to
  perform faster likelihood fits by science tools.

The proposed effective area format, used for both cases mentioned above, follows
mostly the `OGIP effective area`_ format document.

For the moment, the format for the effective area works to a satisfactory level.
Nevertheless, for instance the energy threshold variation across the FoV is not
taken into account. However, since the threshold definitions are currently
non-unified an inclusion of this variation is still arbitrary and subject to
analysis chain. In addition, this feature is currently not supported in current
open source tools. We therefore keep the optional opportunity to add an
individual extension listing the energy threshold varying across the FoV. This
will likely be included in future releases.

.. _aeff_2d:

==================
``aeff_2d`` format
==================

Effective Area vs true energy
-----------------------------

The effective area as a function of the true energy and offset angle is saved as
a :ref:`fits-arrays-bintable-hdu` with required columns listed below.

Columns:

* ``THETA_LO``, ``THETA_HI`` -- ndim: 1
    * Field of view offset axis
* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``EFFAREA`` -- ndim: 2
    * Effective area value as a function of true energy

Recommended axis order: ``ENERGY``, ``THETA``

Header keywords:

In addition to the standard header keywords, the recommended energy range for
the observation corresponding to the effective area file is stored in two
additional header keywords. Another optional header keyword contains the theta
squared cut that was applied in the case of a effective area generation for
point-like sources. A hierarchical ``HDUCLASS`` keyword is used to declare the
effective area type contained within the HDU.

* ``OBS_ID`` type: int
    * Observation ID, run number
* ``LO_THRES`` type: float, unit: TeV
    * Low energy threshold
* ``HI_THRES`` type: float, unit: TeV
    * High energy threshold
* ``RAD_MAX`` type: float, unit: deg
    * On region radius for point-like observations
* ``HDUCLAS2`` type: string
    * Secondary extension class (option: 'EFF_AREA').
    
Although not a requirement, the recommended ``EXTNAME`` keyword is "EFFECTIVE AREA".

.. _aeff_reco_2d:

Effective Area vs reconstructed energy
--------------------------------------

The effective area as a function of the reconstructed energy, may be stored as
an additional HDU within  the FITS file, following an analog format as described
in ``aeff_2d``:

Columns:

* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``ERECO_LO``, ``ERECO_HI`` -- ndim: 1, unit: TeV
    * Reconstructed energy axis
* ``EFFAREA`` -- ndim: 2, unit: none
    * Effective area value as a function of reconstructed energy

Recommended axis order: ``ERECO``, ``THETA``

Header keywords:

* ``OBS_ID`` type: int
    * Observation ID, run number
* ``LO_THRES`` type: float, unit: TeV
    * Low energy threshold
* ``HI_THRES`` type: float, unit: TeV
    * High energy threshold
* ``RAD_MAX`` type: float, unit: deg
    * On region radius for point-like observations
* ``HDUCLAS2`` type: string
    * Secondary extension class (option: 'EFF_AREA_RECO').
    

Same header keywords as in ``aeff_2d`` are required, although is recommended to
change the ``EXTNAME`` keyword to "EFFECTIVE AREA (RECO)".

Note within the IRFs, we label the true energy as ``ENERGY`` and the
reconstructed energy as ``ERECO``, while in the  event lists ``ENERGY`` refers
to the reconstructed energy. Although it may be formally inconsistent, this
convention follows  current standards.

An example file is provided  :download:`here <./aeff_2d_example.fits>`.
