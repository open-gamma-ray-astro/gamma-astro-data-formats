.. _hdu-index:

HDU index table
===============

The HDU index table is stored in a FITS file as a BINTABLE HDU:

* Suggested rilename: ``hdu-index.fits``
* Suggested HDU name: ``HDU_INDEX``

It contains one row per HDU it refers to and can be used to e.g. find the ``TYPE=AEFF`` HDU
for ``OBS_ID=42`` by looking at the ``FILE_DIR``, ``FILE_NAME`` and ``HDUNAME`` fields.

.. _hdu-index-columns:

Columns
-------

==============  ================================================  =========
Column Name     Description                                       FITS type
==============  ================================================  =========
OBS_ID          Observation ID (a.k.a. run number)                int
CHUNK_ID        In case of run splitting (optional)               int
TYPE            HDU type                                          int
FILE_DIR        Directory of file (rel. to this file)             string
FILE_NAME       Name of file                                      string
HDUNAME         Name of HDU in file                               string
SIZE            File Size                                         int
MTIME           Modification time                                 double
MD5             Checksum                                          string
HDUCLASS        HDU format type                                   string
==============  ================================================  =========


TODO: where are the valid TYPE values listed?

.. _hdu-index-header:

Header keywords
---------------


==============  =========================    =================    ======================
Keyword         Description                  Unit                 FITS type
==============  =========================    =================    ======================
TELESCOP        Name of telescope                                  string
CHAIN           Analysis chain/framework                          string
FITSVER         Version of FITS exporter                          string
DSTVER          DST Version                                       string
CONFIG          Cut configuration                                  string
==============  =========================    =================    ======================

