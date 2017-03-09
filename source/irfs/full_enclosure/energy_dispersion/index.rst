.. _iact-edisp:

Energy Dispersion
=================

The energy dispersion information is stored in a FITS file with one required
extensions (HDU). The stored quantity is a PDF for the **energy migration**

.. math::

     \mu = \frac{E_{\mathrm{reco}}}{E_{\mathrm{true}}}

as a function of true energy and offset. It should be normalized to unity. The
migration range covered in the file must be large enough to make this possible
(Suggestion: :math:`1/3 < \mu < 3`)

.. _edisp_trafo:

Transformation
--------------

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

.. _edisp_2d:

``edisp_2d`` format
-------------------

The energy dispersion information is saved as a
:ref:`fits-arrays-bintable-hdu` with the following required columns.

Columns:

* ``MATRIX`` type: float, dimensions: 3 
    * Matrix holding the probability for a given energy migration at a certain true energy and offset.

* ``ENERG_LO``, ``ENERG_HI`` -- ndim: 1, unit: TeV
    * Energy axis
* ``THETA_LO``, ``THETA_HI`` -- ndim: 1, unit: deg
    * Field of view offset axis
* ``MIGRA_LO``, ``MIGRA_HI`` -- ndim: 1, unit: dimensionless
    * Energy migration axis (defined above)
* ``MATRIX`` -- ndim: 3, unit: dimensionless
    * Energy dispersion :math:`dP/d\mu`, see formula above.

Recommended axis order: ``ENERGY``, ``MIGRA``, ``THETA``

Header keywords: none
