.. include:: ../../references.txt

.. _region_skymap:

Region Formats
==============

This page describes data format conventions for region based data, such
as spectra or spectra depending on other physical variables.


The format splits the specification of the region based data into two HDUs: an
:ref:`bin_table_hdu` and a :ref:`region_table_hdu`. The data bin table HDU
contains the data as well as the bands definition (see :ref:`bands_hdu`)
and an optional bin table HDU which contains the region information.


.. _region_sample_files:

Sample Files
------------

* Energy dependent region map: :download:`FITS <region_map_1d.fits>`
* Time & energy dependent region map: :download:`FITS <region_map_2d.fits>`


.. _bin_table_hdu:

Data HDU
--------
The data HDU is a ``BinTableHDU`` containing the flattened n dimensional data.
The associated table column should be named "DATA". The header requires to define
the keywords ``BANDSHDU`` to define the name of the bands HDU and ``REGHDU`` to define
the name of the optional region HDU.

.. _region_table_hdu:

Bands HDU
---------
The definition of bands HDU exactly follows :ref:`bands_hdu`.


Region HDU
----------

The region HDU contains the region information following the standard
`FITS Region Binary Table <https://fits.gsfc.nasa.gov/registry/region.html>`_
convention as supported by the `regions <https://astropy-regions.readthedocs.io/en/latest/fits_region.html>`_
package as well. In general this HDU is optional.

