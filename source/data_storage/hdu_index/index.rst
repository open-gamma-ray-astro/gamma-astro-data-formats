.. _hdu-index:

HDU index table
===============

The HDU index table is stored in a FITS file as a BINTABLE HDU:

* Suggested filename: ``hdu-index.fits``
* Suggested HDU name: ``HDU_INDEX``

It contains one row per HDU it refers to and can be used to e.g. find the ``TYPE=AEFF`` HDU
for ``OBS_ID=42`` by looking at the ``FILE_DIR``, ``FILE_NAME`` and ``HDUNAME`` fields.

.. _hdu-index-columns:

Columns
-------

==============  ================================================  ========= =========
Column Name     Description                                       Data type Required?
==============  ================================================  ========= =========
OBS_ID          Observation ID (a.k.a. run number)                int       yes
CHUNK_ID        In case of run splitting                          int       no
TYPE            HDU type                                          int       yes
FILE_DIR        Directory of file (rel. to this file)             string    yes
FILE_NAME       Name of file                                      string    yes
HDUNAME         Name of HDU in file                               string    yes
HDUCLASS        HDU format type                                   string    yes
SIZE            File size (bytes)                                 int       no
MTIME           Modification time                                 double    no
MD5             Checksum                                          string    no
==============  ================================================  ========= =========


TODO: where are the valid TYPE values listed?

.. _hdu-index-header:

Header keywords
---------------

========== =========================  ========= =========
Keyword    Description                Data type Required?
========== =========================  ========= =========
TELESCOP   Name of telescope          string    no
CHAIN      Analysis chain/framework   string    no
FITSVER    Version of FITS exporter   string    no
DSTVER     DST Version                string    no
CONFIG     Cut configuration          string    no
========== =========================  ========= =========

