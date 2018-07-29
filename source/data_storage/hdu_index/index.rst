.. include:: ../../references.txt

.. _hdu-index:

HDU index table
===============

The HDU index table is stored in a FITS file as a BINTABLE HDU:

* Suggested filename: ``hdu-index.fits.gz``
* Suggested HDU name: ``HDU_INDEX``

The HDU index table can be used to locate HDUs. E.g. for a given ``OBS_ID`` and
(``HDU_TYPE`` and / or ``HDU_CLASS``), the HDU can be located via the
information in the ``FILE_DIR``, ``FILE_NAME`` and ``HDU_NAME`` columns. The
path listed in ``FILE_DIR`` has to be relative to the location of the index
file.

.. _hdu-index-base-dir:

BASE_DIR
--------

By default, file locations should be relative to the location of this HDU index
file, i.e. the total file path is ``PATH_INDEX_TABLE / FILE_DIR / FILE_NAME``.
Tools are expected to support relative file paths in POSIX notation like
``FILE_DIR = "../../data/"`` as well as absolute file path like ``FILE_DIR =
"/data/cta"``.

To allow for some additional flexibility, an optional header keyword
``BASE_DIR`` can be used. If it is given, the file path is ``BASE_DIR / FILE_DIR
/ FILE_NAME``, i.e. the location of the HDU index table becomes irrelevant.

.. _hdu-index-columns:

Columns
-------

==============  ================================================  ========= =========
Column Name     Description                                       Data type Required?
==============  ================================================  ========= =========
``OBS_ID``      Observation ID (a.k.a. run number)                int       yes
``HDU_TYPE``    HDU type (see below)                              string    yes
``HDU_CLASS``   HDU class (see below)                             string    yes
``FILE_DIR``    Directory of file (rel. to this file)             string    yes
``FILE_NAME``   Name of file                                      string    yes
``HDU_NAME``    Name of HDU in file                               string    yes
``SIZE``        File size (bytes)                                 int       no
``MTIME``       Modification time                                 double    no
``MD5``         Checksum                                          string    no
==============  ================================================  ========= =========

.. _hdu-type-class:

HDU_TYPE and HDU_CLASS
----------------------

The ``HDU_TYPE`` and ``HDU_CLASS`` can be used to select the HDU of interest.

The difference is that ``HDU_TYPE`` corresponds generally to e.g. PSF, whereas
``HDU_CLASS`` corresponds to a specific PSF format. Declaring ``HDU_CLASS`` here
means that tools loading these files don't have to do guesswork to infer the
format on load.

Valid ``HDU_TYPE`` values:

* ``events`` - Event list
* ``gti`` - Good time interval
* ``aeff`` - Effective area
* ``psf`` - Point spread function
* ``edisp`` - Energy dispersion
* ``bkg`` - Background

Valid ``HDU_CLASS`` values:

* ``events`` - see format spec: :ref:`iact-events`
* ``gti`` - see format spec: :ref:`iact-gti`
* ``aeff_2d`` - see format spec: :ref:`aeff_2d`
* ``edisp_2d`` - see format spec: :ref:`edisp_2d`
* ``psf_table`` - see format spec: :ref:`psf_table`
* ``psf_3gauss`` - see format spec: :ref:`psf_3gauss`
* ``psf_king`` - see format spec: :ref:`psf_king`
* ``bkg_2d`` - see format spec: :ref:`bkg_2d`
* ``bkg_3d`` - see format spec: :ref:`bkg_3d`


Relation to HDUCLAS
-------------------

At :ref:`hduclass` and throughout this spec, ``HDUCLAS`` header keys are defined
as a declarative HDU classification scheme. This appears similar to this HDU
index table, but in reality is different and incompatible!

Here in the index table, we have ``HDU_CLASS`` and ``HDU_TYPE``. In
:ref:`hduclass`, there is ``HDUCLASS`` which is always "GADF" and then there is
a hierarchical ``HDUCLAS1``, ``HDUCLAS2``, ``HDUCLAS3`` and ``HDUCLAS4`` that
corresponds to the information in ``HDU_CLASS`` and ``HDU_TYPE`` here. Also the
values are different: here we have lower-case and use e.g. ``HDU_CLASS="aeff"``,
in :ref:`hduclass` we use upper-case and e.g. ``HDUCLAS2="EFF_AREA"``

One reason for these inconsistencies is that the spec for this HDU index table
was written first (in 2015), and then :ref:`hduclass` was introduced later (in
2017). Another reason is that here, we tried to be simple (flat, not
hierarchical classification), and for :ref:`hduclass` we tried to follow an
existing standard.

Given that these index tables have been in use in the past years, and that we
expect them to be replaced soon by a completely different way to locate and link
IACT data HDUs, we decided to keep this format as-is, instead of trying to align
it with :ref:`hduclass` and create some form of hierarchical index table.
