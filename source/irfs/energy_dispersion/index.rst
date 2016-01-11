.. _iact-edisp:

Energy Dispersion
=================

The extension holding the energy dispersion is called ```ENERGY DISPERSION```. 
The energy dispersion is saved as a BINTABLE with the following columns
(:ref:`fits-arrays-bintable-hdu`)

+--------------------+------------------------------------+-------------------+-------------+
| Column Name        | Description                        | Unit              | FITS Type   |
+====================+====================================+===================+=============+
|   ENERG_LO         | Lower energy bin edges             | TeV               | TFLOAT      |
+--------------------+------------------------------------+-------------------+-------------+
|   ENERG_HI         | Upper energy bin edges             | TeV               | TFLOAT      |
+--------------------+------------------------------------+-------------------+-------------+
|   THETA_LO         | Lower offset bin edges             | deg               | TFLOAT      |
+--------------------+------------------------------------+-------------------+-------------+
|   THETA_HI         | Upper offset bin edges             | deg               | TFLOAT      |
+--------------------+------------------------------------+-------------------+-------------+
|   EFFAREA          | Effective Area (wrt true energy)   | m\ :math:`^{2}`   | TFLOAT      |
+--------------------+------------------------------------+-------------------+-------------+
|   EFFAREA_RECO     | Effective Area (wrt reco energy)   | m\ :math:`^{2}`   | TFLOAT      |
+--------------------+------------------------------------+-------------------+-------------+
