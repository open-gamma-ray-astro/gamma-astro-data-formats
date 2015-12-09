.. _iact-aeff:

Effective Area
==============

The proposed effective area format follows mostly the
`OGIP format for effective area files <https://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_019/cal_gen_92_019.html>`__

The extension holding the data is called ```EFFECTIVE AREA```. The data within
the extension is organised as a BINTABLE with the following columns
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


In addition to the standard header keywords we store information about the
recommended energy range for the observation corresponding to the effective area
file. There are two additional header keywords in this HDU, which specify the
recommended energy range

+----------------+--------------------------+--------+-------------+
| Keyword        | Description              | Unit   | FITS Type   |
+================+==========================+========+=============+
|   LO_THRES     | Lower energy threshold   | TeV    | TFLOAT      |
+----------------+--------------------------+--------+-------------+
|   HI_THRES     | Upper energy boundary    | TeV    | TFLOAT      |
+----------------+--------------------------+--------+-------------+


For the moment, the format for the effective area works to satisfactory detail.
Nevertheless, for instance the energy threshold variation across the FoV is not
taken into account. However, since the threshold definitions are currently
non-unified an inclusion of this variation is still arbitrary and subject to
analysis chain. In addition, this feature is currently not supported in current
open source tools. We therefore keep the optional opportunity to add an
individual extension listing the energy threshold varying across the FoV. This
will likely be included in future releases.
