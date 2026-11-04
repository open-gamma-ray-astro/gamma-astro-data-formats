.. include:: ../../../references.txt

.. _iact-aeff-format:

Effective area format
=====================

Here we specify the format to store the effective area of a full-enclosure IRF.
Effective area is always stored as a function of true energy (see :ref:`iact-aeff`).
Two formats are specified:

* ``AEFF_2D`` depends on true energy and the field of view offset theta,
  i.e. it is radially symmetric.
* ``AEFF_3D`` depends on true energy and the field of view coordinates
  ``DETX`` and ``DETY``. It can capture a non-radially-symmetric acceptance,
  e.g. for small arrays or for the zenith-angle gradient across the field of
  view in divergent-pointing observations.

.. _aeff_2d:

AEFF_2D
-------

Effective Area vs true energy
+++++++++++++++++++++++++++++

The effective area as a function of the true energy and offset angle is saved as
a :ref:`fits-arrays-bintable-hdu` with required columns listed below.

Columns:

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``EFFAREA`` -- ndim: 2, unit: m^2
    * Effective area value as a function of true energy

Recommended axis order: ``ENERGY``, ``THETA``

Header keywords:

If the IRFs are only known to be "valid" or "safe" to use within a given energy
range, that range can be given via the following two keywords. The keywords are
optional, not all telescopes use the concept of a safe range; e.g. in CTA at
this time this hasn't been defined. Note that a proper scheme to declare IRF
validity range (e.g. masks or weights, or safe cuts that depend on other
parameters such as FOV offset) is not available yet.

* ``LO_THRES`` type: float, unit: TeV
    * Low energy threshold
* ``HI_THRES`` type: float, unit: TeV
    * High energy threshold

If the effective area corresponds to a given observation with an ``OBS_ID``,
that ``OBS_ID`` should be given as a header keyword. Note that this is not
always the case, e.g. sometimes IRFs are simulated and produced for instruments
that haven't even been built yet, and then used to simulate different kinds of
observations.

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.3'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EFF_AREA'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE'
* ``HDUCLAS4`` = 'AEFF_2D'
    
The recommended ``EXTNAME`` keyword is "EFFECTIVE AREA".

Example data file: :download:`here <./aeff_2d_full_example.fits>`.

.. _aeff_3d:

AEFF_3D
-------

The ``AEFF_3D`` format contains a 3-dimensional array of effective area,
stored in the :ref:`fits-arrays-bintable-hdu` format. It is an extension of
``AEFF_2D`` where the scalar field of view offset is replaced by the two field
of view coordinates ``DETX`` and ``DETY``, so that the effective area can vary
with the direction inside the field of view (see :ref:`coords-fov`). The
effective area is given as a function of the **true** source direction relative
to the array pointing position.

``HDUCLAS3`` must be either ``'FULL-ENCLOSURE'`` (see :ref:`full-enclosure-irfs`)
or ``'POINT-LIKE'`` (see :ref:`point-irfs`).

Required columns:
+++++++++++++++++

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * True energy axis
* ``DETX_LO``, ``DETX_HI``, ``DETY_LO``, ``DETY_HI`` -- ndim: 1, unit: deg
    * Field of view coordinates binning (see :ref:`coords-fov`).
      Coordinates of the true source position relative to the array
      pointing position.
* ``EFFAREA`` -- ndim: 3, unit: m^2
    * Effective area value as a function of true energy and field of view
      coordinates

Recommended axis order: ``ENERGY``, ``DETX``, ``DETY``

Header keywords:
++++++++++++++++

The optional ``LO_THRES``, ``HI_THRES`` and ``OBS_ID`` keywords defined for
``AEFF_2D`` apply equally here.

As explained in :ref:`hduclass`, the following header keyword should be used to 
declare the type of HDU:

* ``HDUDOC``   = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats'
* ``HDUVERS``  = '0.4'
* ``HDUCLASS`` = 'GADF'
* ``HDUCLAS1`` = 'RESPONSE'
* ``HDUCLAS2`` = 'EFF_AREA'
* ``HDUCLAS3`` = 'FULL-ENCLOSURE' / 'POINT-LIKE'
* ``HDUCLAS4`` = 'AEFF_3D'

Further header keywords:

* ``FOVALIGN`` = 'ALTAZ' / 'RADEC'
    * Alignment of the field-of-view coordinate system (see :ref:`coords-fov`).
      It is recommended to always fill this keyword explicitly.

The recommended ``EXTNAME`` keyword is "EFFECTIVE AREA".

Example data file: :download:`here <./aeff_3d_full_example.fits>`.
