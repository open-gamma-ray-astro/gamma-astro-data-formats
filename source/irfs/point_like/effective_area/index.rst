.. include:: ../../../references.txt

.. _iact-point-aeff-format:

Effective area format
=====================

Here we specify the format to store the effective area of a point-like 
IRF. It is possible to store as a function of the true energy or as a function 
of the reconstructed energy.

.. _point-aeff:

``point_aeff``
--------------

Effective Area vs true energy
+++++++++++++++++++++++++++++

The effective area as a function of the true energy is saved as
a :ref:`fits-arrays-bintable-hdu` with required columns listed below.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``RAD_MAX`` -- ndim: 1, unit: deg
    * Radial cut applied to each energy bin to calculate the IRF
* ``EFFAREA`` -- ndim: 1
    * Effective area value as a function of true energy

Recommended axis order: ``ENERGY``, ``THETA``

Header keywords:

In addition to the standard header keywords, the recommended energy range for
the observation corresponding to the effective area file is stored in two
additional header keywords. A hierarchical ``HDUCLASS`` keyword is used to declare the
effective area type contained within the HDU.

* ``OBS_ID`` type: int
    * Observation ID, run number
* ``LO_THRES`` type: float, unit: TeV
    * Low energy threshold
* ``HI_THRES`` type: float, unit: TeV
    * High energy threshold
* ``HDUCLAS2`` type: string
    * Secondary extension class (option: 'EFF_AREA').
    
Although not a requirement, the recommended ``EXTNAME`` keyword is "EFFECTIVE AREA".

.. _point-aeff-reco:

Effective Area vs reconstructed energy
++++++++++++++++++++++++++++++++++++++

The effective area as a function of the reconstructed energy, may be stored as
an additional HDU within  the FITS file, following an analog format as described
in ``point_aeff``:

Columns:

* ``ERECO_LO``, ``ERECO_HI`` -- ndim: 1, unit: TeV
    * Reconstructed energy axis
* ``RAD_MAX`` -- ndim: 1, unit: deg
    * Radial cut applied to each energy bin to calculate the IRF
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
* ``HDUCLAS2`` type: string
    * Secondary extension class (option: 'EFF_AREA_RECO').
    

Same header keywords as in ``point_aeff`` are required, although is recommended to
change the ``EXTNAME`` keyword to "EFFECTIVE AREA (RECO)".

Note within the IRFs, we label the true energy as ``ENERGY`` and the
reconstructed energy as ``ERECO``, while in the  event lists ``ENERGY`` refers
to the reconstructed energy. Although it may be formally inconsistent, this
convention follows  current standards.

An example file is provided  :download:`here <./aeff_2d_example.fits>`.
