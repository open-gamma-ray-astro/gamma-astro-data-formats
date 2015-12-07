.. _iact-storage:

Master index file
=================

.. warning:: This format is under discussion. These are just some notes, we haven't converged yet.


Proposal A
----------

In H.E.S.S. we have FITS data for various analysis chains, FITS versions, DST versions and
reco / cut configurations. I.e. for each observation, there are several versions of the events
and IRF files for a given observation.

We would like to have a master index file on the data server that lists what is available.
A file in the same format would also be on the user's machine, listing what is available there.

In Gammapy we have been prototyping this idea of having a master index configuration file:
https://gammapy.readthedocs.org/en/latest/obs/dm.html#data-registry-config-file

We already use the `~/.gammapy/data-registry.yaml` file to select which data to use as input
from the `gammapy-spectrum` script and we'll have to think if end-user scripts should select data
via this master index file, or via individual observation and HDU index files.

The `YAML <https://en.wikipedia.org/wiki/YAML>`__ format is nice because it is human-readable
and -editable as well as machine-readable (whereas FITS is not nice for manual editing,
or leaving comments). We don't need scripts or tools to edit it (e.g. when we add a new
"FITS prod" on the server or to adjust a PATH on the user's machine.

The use cases and a proposed format for this file will be posted at a later point in time,
we'd like to think about this some more and prototype it for a while.

Proposal B
----------

The idea is to have an index file containing and listing the locations to all further hdu index files.

The index file should be located under a certain environment variable, e.g.
$IACT_FITS or $VHEFITS or similar. The file should have a certain name and
contain all available index files for all available chains /recos etc. The user
copies this file from the server. The Science tools that access this file just
ignore chains/configs that are not present on the users' machine. Then the index
file can also FITS (no need to introduce another file and data format). Since
all paths are relative to the environment variable, the user doesn't have to
edit and maintain the master index file. The Science tools naturally will allow
the analysis of a certain chain/config or not.
The master index FITS file could look the following:

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
