.. include:: ../../references.txt

.. _bkg:

Background
==========

One method of background modeling for IACTs is to construct spatial and / or
spectral model templates of the irreducible cosmic ray background for a given reconstruction and
gamma-hadron separation from :ref:`glossary-obs-off`.
These templates can then be used as an ingredient to model the background
in observations that contain gamma-ray emission of interest, or to compute
the sensitivity for that set of cuts.

Here we specify two formats for such background template models:

* ``BKG_2D`` models depend on ``ENERGY`` and ``THETA``, i.e. are radially symmetric.
* ``BKG_3D`` models depend on ``ENERGY`` and field of view coordinates ``DETX`` and ``DETY``.

Note that generating background models requires the construction of several
intermediate products (counts and livetime histograms, both filled by cutting
out exclusion regions around sources like AGN) to arrive at the models
containing an absolute rate described here. At this time we don't specify a
format for those intermediate formats.

.. _bkg-2d:

BKG_2D format
-------------

TODO

Example data file: TODO

.. _bkg-3d:

BKG_3D format
-------------

TODO

Example data file: TODO
