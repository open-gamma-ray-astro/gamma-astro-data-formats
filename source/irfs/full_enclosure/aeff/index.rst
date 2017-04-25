.. include:: ../../../references.txt

.. _iact-aeff-format:

Effective area format
=====================

Here we specify the format to store the effective area (see :ref:`iact-aeff`) of a full-enclosure 
IRF. It is possible to store as a function of the true energy or as a function 
of the reconstructed energy.

.. _aeff_2d:

``aeff_2d``
-----------

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
    
The recommended ``EXTNAME`` keyword is "EFFECTIVE AREA".

.. _aeff_2d_reco:

Effective Area vs reconstructed energy
++++++++++++++++++++++++++++++++++++++

The effective area as a function of the reconstructed energy, may be stored as
an additional HDU within  the FITS file. Note in this case, the ``ENERG_LO`` and ``ENERG_HI`` columns
contain the reconstructed energy instead of the true energy.

The format is analog to the one described in ``aeff_2d``, except for the ``HDUCLAS4`` keyword:

* ``HDUCLAS4`` = 'AEFF_2D_RECO'

The ``EXTNAME`` keyword is recommended to be "EFFECTIVE AREA (RECO)".

Example data file: :download:`here <./aeff_2d_full_example.fits>`.
