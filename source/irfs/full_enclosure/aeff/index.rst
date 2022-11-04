.. include:: ../../../references.txt

.. _iact-aeff-format:

Effective area format
=====================

Here we specify the format to store the effective area of a full-enclosure IRF.
Effective area is always stored as a function of true energy. (see :ref:`iact-aeff`) 

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
