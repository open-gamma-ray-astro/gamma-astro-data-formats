.. _iact-aeff:

Effective Area
==============

The proposed effective area format follows mostly the `OGIP effective area
format`_ document.

For the moment, the format for the effective area works to satisfactory detail.
Nevertheless, for instance the energy threshold variation across the FoV is not
taken into account. However, since the threshold definitions are currently
non-unified an inclusion of this variation is still arbitrary and subject to
analysis chain. In addition, this feature is currently not supported in current
open source tools. We therefore keep the optional opportunity to add an
individual extension listing the energy threshold varying across the FoV. This
will likely be included in future releases.

EFFECTIVE AREA extension
------------------------

Valid names for the extension holding the effective area are ``EFFECTIVE AREA``
and ``AEFF_2D``. The effective area information is saved as a
:ref:`fits-arrays-bintable-hdu` with required columns listed below. In addition
to the standard header keywords the recommended energy range for the observation
corresponding to the effective area file is stored in two additional header.
Another optional header keyword contains the theta squared cut that was applied
in the case of a effective area generation for point-like sources.

Required Column Names
---------------------

* ``ENERG_LO`` type: float, unit: TeV
    * Lower energy bin edges 
* ``ENERG_HI`` type: float, unit: TeV
    * Upper energy bin edges 
* ``THETA_LO`` type: float, unit: deg
    * Lower offset bin edges
* ``THETA_HI`` type: float, unit: deg
    * Upper offset bin edges
* ``EFFAREA`` type: float, dimensions: 2
    * Matrix holding the effective area for a given true energy and offset.
* ``EFFAREA_RECO`` type: float, dimensions: 2
    * Matrix holding the effective area for a given reconstructed energy and offset.
    * TODO: Is this still up-to-date?

Optional Column Names
---------------------

* ``LO_THRES`` type: float, unit: TeV
    * Low energy threshold
* ``HI_Thres`` type: float, unit: TeV
    * High energy threshold
* ``RAD_MAX`` type: float, unit: deg
    * On region radius for point-like observations
