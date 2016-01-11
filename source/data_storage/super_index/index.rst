.. _iact-storage-master:

Master index file
=================

.. warning:: We are currently in a prototyping phase. This format is under development.

The idea is to have an index file containing and listing the locations to all
further hdu index files. To allow for human-readable and human-editable files,
we use a ``JSON`` format here

* Required filename: ``master.json``

The user copies this file from the server along with selected data. The Science
tools that access this file just ignore chains/configs that are not present on
the users' machine. Ideally, the Science tools provide the possibility to
inspect the local master index file and print the users' options on the screen.
Since all paths must be relative to the location of the master index file, the
user doesn't have to edit and maintain the master index file. The  Science tools
naturally will allow the analysis of a certain chain/config or not. Of course
the user can always add  own FITS productions etc simply by hand (or locally
change names of configs for convenience). The ``JSON`` table should contain an
array named ``datasets``. Each dataset is specified by the following required
keys:

Required keys
-------------
* ``name`` type: string
    * Unique name describing the present FITS production, e.g."hess-hap-hd-prod01-std_zeta_fullEnclosure". 
* ``hduindx`` type: string
    * Location of corresponding hdu index file. This path must be relative to the location of the master index file
* ``obsindx`` type: string
    * Location of corresponding observation index file. This path must be relative to the location of the master index file

Of course any optional and additional information can be added, e.g. the
telescope name, analysis chain, cut configuration, etc. The Science tools should
be able to show these information to the user to simplify the choice for a
preferred FITS production.

Here is an example of the master index file:

.. code-block:: json

   {
       "datasets": [
           {
               "name": "fits-prod1-stdcuts",
	           "obsindx": "relative/path/to/prod1-std/obs-index.fits.gz",
               "hduindx": "relative/path/to/prod1-std/hdu-index.fits.gz",
	           "comment": "First test version",
	           "drawback": "Not all data available"
           },
           {
	           "name": "fits-prod2-hardcuts",
	           "obsindx": "relative/path/to/prod2-hard/obs-index.fits.gz",
               "hduindx": "relative/path/to/prod2-hard/hdu-index.fits.gz",
	           "recommendation:": "use for science publications"
           }
       ]
   }


Note that the keywords "comment", "drawback" and "recommendation" are arbitray
and can be added from the user or maintainer of the master index file. The
Science tools can display them for the user to get more details about each FITS
dataset on the users' machine.
