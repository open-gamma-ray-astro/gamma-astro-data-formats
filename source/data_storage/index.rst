Data Storage
====================================

Here we give an overview of how the data storage for IACTs should look like.
In general, IACT data is divided into "runs" of a few tens of minutes of data taking. 
We have per-run IRFs and per run event lists. The challenge is that in the data structure,
we have to accomodate user choices on various levels:
.. toctree::
   :maxdepth: 1

   Reconstruction chain (e.g. paris)
   Version of FITS exporter (e.g prod01)
   Version of internal data storage (e.g. model_deconvoluted_prod26)
   Cut configuration (e.g. mpp_std)
   
We here propose a two-level index file scheme to allow for arbitrary folder structures.
For each directory tree containing the files of the cut configuration, two files should be present:

.. toctree::

   obs_index/index
   hdu_index/index
   
The observation index provides information of meta data about each observation run. E.g. pointing in the sky, duration, number of events, etc.
The hdu index file provides a list of all available HDUs and in what files they are located. Science tools can make use of this index files to
build filenames of required files according to some user parameters.

In addition, we have an index of all available index files to simply allow a quick look on what configurations are available. This file also
provides the locations of the hdu index and observation index files.


Table of contents
-----------------

.. toctree::

   obs_index/index
   hdu_index/index
   super_index/index
