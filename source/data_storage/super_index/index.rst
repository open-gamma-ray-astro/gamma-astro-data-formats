Super index file
================

.. warning:: This format is under discussion. These are just some notes, we haven't converged yet.

The idea is to have an index file containing and listing the locations to all further hdu index
files. Here are two proposal how this could look like:

Proposal A
----------
A .yaml file located somewhere on the machine. The file needs to be maintained
by the user to point to the right data directiory and list the available index
files. See https://gammapy.readthedocs.org/en/latest/obs/dm.html#data-registry-config-file
for details

Proposal B
----------

The index file should be located under a certain environment variable, e.g.
$IACT_FITS or $VHEFITS or similar. The file should have a certain name and
contain all available index files for all available chains /recos etc. The user
copies this file from the server. The Science tools that access this file just
ignore chains/configs that are not present on the users' machine. Then the index
file can also FITS (no need to introduce another file and data format). Since
all paths are relative to the environment variable, the user doesn't have to
edit and maintain the super index file. The Science tools naturally will allow
the analysis of a certain chain/config or not. The super index FITS file could look the following:

===========  ==============================
Column Name  Description
===========  ==============================
CHAIN        Analysis Chain/Framework
FITSVER      Version of FITS exporter
DSTVER       Version of DST processing
CONFIG       Cut configuration
OBSINDX      File name of observation index
HDUINDX      File name of hdu index file
===========  ==============================

The file names of "OBSINDX" and "HDUINDX" are relative to the above environment variable.
