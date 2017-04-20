.. include:: ../../../references.txt

.. _iact-aeff-format:

Effective area format
=====================

Here we specify the format to store the effective area of a full-enclosure 
IRF. It is possible to store as a function of the true energy or as a function 
of the reconstructed energy.

.. _aeff_2d_full:

``aeff_2d_full``
----------------

Effective Area vs true energy
+++++++++++++++++++++++++++++

The effective area as a function of the true energy and offset angle is saved as
a :ref:`fits-arrays-bintable-hdu` with required columns listed below.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1
    * Field of view offset axis
* ``EFFAREA`` -- ndim: 2
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
    
As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EFF_AREA'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'AEFF_2D'
    
Although not a requirement, the recommended ``EXTNAME`` keyword is "EFFECTIVE AREA".

.. _aeff_reco_2d_full:

Effective Area vs reconstructed energy
++++++++++++++++++++++++++++++++++++++

The effective area as a function of the reconstructed energy, may be stored as
an additional HDU within  the FITS file, following an analog format as described
in ``aeff_2d_full``:

Columns:

* ``ERECO_LO``, ``ERECO_HI`` -- ndim: 1, unit: TeV
    * Reconstructed energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
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
    
As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.2'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EFF_AREA'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'AEFF_2D_RECO'


Same header keywords as in ``aeff_2d_full`` are required, although is recommended to
change the ``EXTNAME`` keyword to "EFFECTIVE AREA (RECO)".

Note within the IRFs, we label the true energy as ``ENERGY`` and the
reconstructed energy as ``ERECO``, while in the  event lists ``ENERGY`` refers
to the reconstructed energy. Although it may be formally inconsistent, this
convention follows  current standards.

An example file is provided  :download:`here <./aeff_2d_full_example.fits>`.
