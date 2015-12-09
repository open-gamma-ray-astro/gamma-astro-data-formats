.. _glossary:

Glossary
========

.. _glossary-fits:

FITS
++++

Flexible Image Transport System
http://fits.gsfc.nasa.gov/

.. _glossary-heasarc:

HEASARC
+++++++

High Energy Astrophysics Science Archive Research Centre.
http://heasarc.gsfc.nasa.gov/

.. _glossary-ogip:

OGIP FITS Standards
+++++++++++++++++++

The FITS Working Group in the Office of Guest Investigators Program has
established conventions for FITS files for high-energy astrophysics
projects.
http://hesperia.gsfc.nasa.gov/rhessidatacenter/software/ogip/ogip.html

.. _glossary-caldb:

CALDB
+++++

The HEASARC's calibration database (CALDB) system stores and indexes
datasets associated with the calibration of high energy astronomical
instrumentation.
http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/caldb_intro.html

.. _glossary-iact:

IACT
++++

IACT = imaging atmospheric Cherenkov telescope (see `wikipedia article
<https://en.wikipedia.org/wiki/IACT>`__).

.. _glossary-obs:

Observation = Run
+++++++++++++++++

For IACTs observations are usually conducted by pointing the array (or a
sub-array) for a period of time (typically half an hour for current IACTs)
at a fixed location in celestial coordinates (i.e. the telescopes slew in
horizontal Alt/Az coordinates to keep the pointing position RA/DEC in the
center of the field of view).

For current IACTs the term "run" is more common than "observation", but for
CTA probably the term "observation" will be used. So it's recommended to use
observation in these format specs.

.. _glossary-obs-off:

Off Observation
+++++++++++++++

The term "off observation" or "off run" refers to observations where most
of the field of view contains no gamma-ray emission (apart from a possible
diffuse extragalactic isotropic component, which is supposed to be very
weak at TeV energies).

`AGN <https://en.wikipedia.org/wiki/Active_galactic_nucleus>`__ observations
are sometimes also considered "off observations", because the fraction of the
field of view containing their gamma-ray emission is often very small, and
most of the field of view is empty.

For further info on background modeling see
`Berge (2007) <http://adsabs.harvard.edu/abs/2007A%26A...466.1219B>`__
