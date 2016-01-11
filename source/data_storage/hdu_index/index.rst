.. include:: ../../references.txt

.. _hdu-index:

HDU index table
===============

The HDU index table is stored in a FITS file as a BINTABLE HDU:

* Suggested filename: ``hdu-index.fits.gz``
* Suggested HDU name: ``HDU_INDEX``

The HDU index table can be used to locate HDUs. E.g. for a given ``OBS_ID`` and
(``HDU_TYPE`` and / or ``HDU_CLASS``), the HDU can be located via the
information in the ``FILE_DIR``, ``FILE_NAME`` and ``HDU_NAME`` columns.
The path listed in ``FILE_DIR`` has to be relative to the location of the index file.

TODO: discuss if we want to support a ``BASE_DIR`` header keyword, to allow the
use case where ``FILE_DIR`` is not relative to the index file location (e.g. in
cases where the user creates or modifies the index file and doesn't have write
permission in the folder where the data files are.)

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

The difference is that ``HDU_TYPE`` corresponds generally to e.g. PSF,
whereas ``HDU_CLASS`` corresponds to a specific PSF format.
Declaring ``HDU_CLASS`` here means that tools loading these files don't have
to do guesswork to infer the format on load.

Valid ``HDU_TYPE`` values (others optional):

* ``events`` - Event list
* ``gti`` - Good time interval
* ``aeff`` - Effective area
* ``psf`` - Point spread function
* ``edisp`` - Energy dispersion
* ``bkg`` - Background

(can be optional, e.g. if no bkg model is available another approach has to be used)

Valid ``HDU_CLASS`` values:

* ``events`` - see format spec: :ref:`iact-events`
* ``gti`` - see format spec: TODO
* ``aeff_2d`` - see format spec: :ref:`aeff_2d`
* ``edisp_2d`` - see format spec: :ref:`edisp_2d`
* ``psf_table`` - see format spec: :ref:`psf-table`
* ``psf_3gauss`` - see format spec: :ref:`psf_3gauss`
* ``psf_king`` - see format spec: :ref:`psf_king`
* ``psf_gtpsf`` -- see format spec: :ref:`psf_gtpsf`
* ``bkg_2d`` - see format spec: :ref:`bkg_2d`
* ``bkg_3d`` - see format spec: :ref:`bkg_3d`

We recommend that HDU names are chosen to be identical to either the ``HDU_TYPE``
or the ``HDU_CLASS`` names mentioned above. This is not a requirement, usually
end users will access data via HDU index files and the HDU names don't matter.
Or, if HDUs are accessed directly, the package or tool should be flexible to
allow loading the HDU with any name.

Future ideas
------------    

* Not required columns are for future usage when downloading and syncing files with a server.
* We keep in mind to incoorporate "CHUNK_ID" column to support splitting of runs into chunks.

.. _hdu-index-header:
