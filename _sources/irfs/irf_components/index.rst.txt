.. include:: ../../references.txt

.. _irf-components:

IRF components
==============

The IRF is made up of several components, described here:

.. _iact-aeff:

Effective Area
--------------


Effective area combines the detection efficiency of an instrument 
with the observable area.
It can be interpreted as the area a perfect detector directly measuring
gamma rays would have.

.. math::

    A_{\mathrm{eff}}(E, ...) = p(E, ...) \cdot A,

with :math:`A` the total observable area and :math:`p(E, ...)` the detection
probability for a gamma ray of a given energy and possibly other parameters,
like the position in the field of view.

Effective area has to be calculated from simulated events in a discretized manner.
:math:`p` is estimated in bins of the dependend variables by dividing the number
of detected and reconstructed events by the number of all simulated events.
Effective are in bin :math:`i` is then

.. math::
    A_{\mathrm{eff}, i} = \frac{N_{\mathrm{detected}, i}}{N_{\mathrm{simulated}, i}} \cdot A,


Usually, :math:`A` is the area in which the events were simulated,
for CORSIKA simulations this will be :math:`A = \pi R_{\mathrm{max}}^2`,
with :math:`R_{\mathrm{max}}` being the maximum scatter radius.

Calculation of effective area can be done at several analysis steps,
e.&thinsp;g. after trigger, after image cleaning
or most important for the DL3 event lists, after applying all event selection criteria,
including gamma-hadron separation and for the case of point-like IRFs the :math:`\theta^2` cut.

As in general, there is no reconstructed energy for the undetected events,
effective area can only be expressed in bins of the true simulated energy.

The proposed effective area format follows mostly the `OGIP effective area`_ format document.

For the moment, the format for the effective area works to a satisfactory level.
Nevertheless, for instance the energy threshold variation across the FoV is not
taken into account. However, since the threshold definitions are currently
non-unified an inclusion of this variation is still arbitrary and subject to
analysis chain. In addition, this feature is currently not supported in current
open source tools. We therefore keep the optional opportunity to add an
individual extension listing the energy threshold varying across the FoV. This
will likely be included in future releases.

.. _iact-edisp:

Energy Dispersion
-----------------

The energy dispersion information is stored in a FITS file with one required
extensions (HDU). The stored quantity is :math:`\frac{dP}{d\mu}`, a PDF for the **energy migration**

.. math::

     \mu = \frac{E_{\mathrm{reco}}}{E_{\mathrm{true}}}

as a function of true energy and offset. It should be normalized to unity, i.e.,

.. math::

     \int_0^\infty \frac{dP}{d\mu}\,d\mu = 1\,.

The migration range covered in the file must be large enough to make this possible
(Suggestion: :math:`0.2 < \mu < 5`)

.. _edisp_trafo:

Transformation
++++++++++++++

For the purpose of some analysis, for example when extracting an
:ref:`ogip-rmf`, it is necessary to calculate the detector response
:math:`R(I,J)`, i.e. the probability to find an energy from within a given true
energy bin *I* of width :math:`\Delta E_{\mathrm{true}}` within a certain
reconstructed energy bin *J* of width :math:`\Delta E_{\mathrm{reco}}`. In order
to do so, the following integration has to be performed (for a fixed offset). 

.. math::

    R(I,J) = \frac{ \int_{\Delta E_{\mathrm{true}}} R(I,E_{\mathrm{true}})\ d E_{\mathrm{true}}}{\Delta E_{\mathrm{true}}},

where

.. math::

    R(I,E_{\mathrm{true}}) = \int_{\mu(\Delta E_{\mathrm{reco}})} \mathrm{PDF}(E_{\mathrm{true}}, \mu)\ d \mu

is the probability to find a given true energy :math:`E_{\mathrm{true}}` in the
reconstructed energy band *J*.

.. _psf:

Point spread function
---------------------

.. _psf-intro:

Introduction
++++++++++++

The point spread function (PSF) (`Wikipedia - PSF`_) represents the spatial probability
distribution of reconstructed event positions for a point source.
So far we're only considering radially symmetric PSFs here.

.. _psf-pdf:

Probability distributions
+++++++++++++++++++++++++

* :math:`dP/d\Omega(r)`, where :math:`dP` is the probability to find an event
  in a solid angle :math:`d\Omega` at an offset :math:`r` from the point source.
  This is the canonical form we use and the values we store in files.
* Often, when comparing observered event distributions with a PSF model,
  the :math:`dP/dr^2` distributions in equal-width bins in :math:`r^2` is
  used. The relation is :math:`d\Omega = \pi dr^2`, i.e. :math:`dP/d\Omega=(1/\pi)(dP/dr^2)`.
* Sometimes, the distribution :math:`dP/dr(r)` is used.
  The relation is :math:`dP/dr = 2 \pi r dP/d\Omega`.

TODO: explain "encircled energy" = "encircled counts" = "cumulative" representation
of PSF and define containment fraction and containment radius.

Normalisation
+++++++++++++

PSFs must be normalised to integrate to total probability 1, i.e.

.. math::

    \int dP/d\Omega(r) d\Omega = 1\,.
    
This implies that the PSF producer is responsible for choosing the Theta
range and normalising. I.e. it's OK to choose a theta range that contains
only 95% of the PSF, and then the integral will be 0.95.

We recommend everyone store PSFs so that truncation is completely negligible,
i.e. the containment should be 99% or better for all of parameter space.


Comments
++++++++

* Usually the PSF is derived from Monte Carlo simulations, but in principle
  it can be estimated from bright point sources (AGN) as well.
* Tools should assume the PSF is well-sampled and noise-free.
  I.e. if limited event statistics in the PSF computation is an issue,
  it is up to the PSF producer to denoise it to an acceptable level.

.. _bkg:

Background
----------

One method of background modeling for IACTs is to construct spatial and / or
spectral model templates of the irreducible cosmic ray background for a given
reconstruction and gamma-hadron separation from :ref:`glossary-obs-off`. These
templates can then be used as an ingredient to model the background in
observations that contain gamma-ray emission of interest, or to compute the
sensitivity for that set of cuts.

.. note::

    Generating background models requires the construction of several
    intermediate products (counts and livetime histograms, both filled by cutting
    out exclusion regions around sources like AGN) to arrive at the models
    containing an absolute rate described here. At this time we don't specify a
    format for those intermediate formats.

.. note::

    Background models are sometimes considered an instrument response function
    (IRF) and sometimes not (e.g. when the background is estimated from different
    parts of the field of view for the same observation).

    Here we have the background format specifications listed under IRFs,
    simply because the storage format is very similar to the other IRFs
    (e.g. effective area) and we didn't want to introduce a new top-level
    section besides IRFs.
 
 
 
 
