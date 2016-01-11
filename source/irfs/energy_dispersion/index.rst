.. _iact-edisp:

Energy Dispersion
=================

The energy dispersion information is stored in a FITS file with one required extensions (HDU). The stored quantity is a PDF for the **energy migration**

.. math::

     \mu = \frac{e_{\mathrm{reco}}}{e_{\mathrm{true}}}

as a function of true energy and offset


ENERGY DISPERSION extension
---------------------------

Valid names for the extension holding the energy dispersion are ``ENERGY DISPERSION`` and ``EDISP_2D``. The energy dispersion information is saved as a :ref:`fits-arrays-bintable-hdu` with the following required columns.

Required Column Names
---------------------

* ``ETRUE_LO`` type: float, unit: TeV
    * Lower true energy bin edges 
* ``ETRUE_HI`` type: float, unit: TeV
    * Upper true energy bin edges 
* ``THETA_LO`` type: float, unit: deg
    * Lower offset bin edges
* ``THETA_HI`` type: float, unit: deg
    * Upper offset bin edges
* ``MIGRA_LO`` type: float
    * Energy migration lower bin edges
* ``MIGRA_HI`` type: float
    * Energy migration upper bin edges
* ``MATRIX`` type: float, dimensions: 3 
    * Matrix holding the probability for a given energy migration at a certain true energy and offset.
