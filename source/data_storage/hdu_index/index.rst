.. _hdu-index:

HDU index table
===============

The HDU index table is stored in a FITS file as a BINTABLE HDU:

* Suggested filename: ``hdu-index.fits.gz``
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
HDUTYPE         HDU type                                          int       yes
HDUCLASS        HDU format type                                   string    yes
HDUNAME         Name of HDU in file                               string    yes
FILE_DIR        Directory of file (rel. to this file)             string    yes
FILE_NAME       Name of file                                      string    yes
SIZE            File size (bytes)                                 int       no
MTIME           Modification time                                 double    no
MD5             Checksum                                          string    no
==============  ================================================  ========= =========

+ Valid TYPE values (others optional):
    + "events"
    + "aeff"
    + "psf"
    + "edisp"
    + "bkg" (can be optional, e.g. if no bkg model is available another approach has to be used)

+ Valid and supported HDUCLASS values:
    + EVENTS
    + AEFF2D
    + PSF_KING
    + PSF_3GAUSS
    + PSF_TABLE
    + EDISP2D
    + BACKGROUND3D

Disclaimer: About HDUNAME
-------------------------
For the moment, we require the following HDU names to be present to conduct a ctools analysis:
* EVENTS
* EFFECTIVE AREA
* POINT SPREAD FUNCTION
* ENERGY DISPERSON
* BACKGROUND

It is therefore currently required (but will eventualy fade) that each observation contains at least one HDU with the listed names, e.g.

========  ==========  ======================= 
OBS_ID    HDUTYPE     HDUNAME	
========  ==========  ======================= 
000001    "events"    "EVENTS"    
000001    "aeff"      "EFFECTIVE AREA"       
000001    "psf"       "POINT SPREAD FUNCTION"	 
000001    "edisp"     "ENERGY DISPERSON"
000001    "bkg"       "BACKGROUND"  
========  ==========  ======================= 

Future ideas
------------    
+ Not required columns are for future usage when downloading and syncing files with a server.
+ We keep in mind to incoorporate "CHUNK_ID" column to support splitting of runs into chunks.

.. _hdu-index-header:

Header keywords
---------------

There only one information that should be stored as header keywords:
+ NAME (string, required=yes): should be a unique name describing the present FITS production, e.g."hess-hap-hd-prod01-std_zeta_fullEnclosure"
This keywords helps to circumvent the absolute need for a master index file which is still under development.



