HDU index file
===========

The HDU index file should contain each HDU which is available in the respective directory containing the cut configuration.

HDU INDEX extension
----------------

The first and only extension is called "HDU INDEX"

.. _tab_1: 

.. table:: HDU INDEX Column names

    ==============  ================================================    =================    ======================
      Column Name         Description                                         Unit                  FITS type
    ==============  ================================================    =================    ======================
      OBS\_ID         Run number                                                                 int
      CHUNK\_ID       In case of run splitting (optional)                                        int
      TYPE            HDU type    					                         int
      FILE_DIR	      Directory of file	(rel. to this file)					 string
      FILE_NAME       Name of file								 string
      HDUNAME         Name of HDU in file 							 string
      SIZE 	      File Size									 int
      MTIME           Modification time                                                          double
      MD5 	      checksum                                                                   string
      HDUCLASS        HDU format type								 string
    ==============  ================================================    =================    ======================

.. _tab_2:

.. table:: HDU INDEX header keywrods

    ==============  =========================    =================    ======================
      Keyword         Description                    Unit                  FITS type
    ==============  =========================    =================    ======================
	  TELESCOP     Name of telescope        			string
	  CHAIN        Analysis chain/framework				string
	  FITSVER      Version of FITS exporter                         string
	  DSTVER       DST Version                                      string
	  CONFIG       Cut configuration				string
    ==============  =========================    =================    ======================

