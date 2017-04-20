.. include:: ../references.txt

.. _hduclass:

HDU classes
===========
 
Following NASA's recommendation 
(see `HFWG Recommendation R8 <http://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/general/ogip_94_006/ogip_94_006.html>`__), 
a hierarchical classification is applied to each HDU within DL3 FITS files, 
using the HDUCLASS and HDUCLASn keywords.

Some useful links from other projects:

* http://cxc.harvard.edu/contrib/arots/fits/content.txt
* https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/r8.html
* https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/hduclas.html
* http://www.starlink.rl.ac.uk/docs/sun167.htx/sun167se3.html
* https://confluence.slac.stanford.edu/display/ST/LAT+Photons

The current scheme used is the following:

* HDUCLASS: General identifier of the data format. Recommended value: "CTA"

* HDUDOC: Link to the DL3 specifications documentation

* HDUVERS: Version of the DL3 specification format

* HDUCLAS1: General type of HDU, currently: ``EVENTS``, ``GTI`` or ``RESPONSE``

* HDUCLAS2: In case of ``RESPONSE`` type, refers to the IRF components stored within the HDU: ``EFF_AREA``, ``BKG``, ``EDISP`` or ``RPSF``

* HDUCLAS3: In case of ``RESPONSE`` type, refers to the way the IRF component was produced (``POINT-LIKE`` or ``FULL-ENCLOSURE``)

* HDUCLAS4: In case of ``RESPONSE`` type, refers to the name of the specific format



+-----------+------------+-----------------+--------------+
|  HDUCLAS1 |  HDUCLAS2  |    HDUCLAS3     |   HDUCLAS4   |
+===========+============+=================+==============+
|    GTI    |            |                 |              |
+-----------+------------+-----------------+--------------+
|  EVENTS   |            |                 |              |
+-----------+------------+-----------------+--------------+
|  RESPONSE | EFF_AREA   |   POINT-LIKE    |   AEFF_2D    |
+-----------+------------+-----------------+--------------+
|           |            |                 | AEFF_2D_RECO |
+-----------+------------+-----------------+--------------+
|           |            | FULL-ENCLOSURE  |   AEFF_2D    |
+-----------+------------+-----------------+--------------+
|           |            |                 | AEFF_2D_RECO |
+-----------+------------+-----------------+--------------+
|           |   EDISP    |   POINT-LIKE    |   EDISP_2D   |
+-----------+------------+-----------------+--------------+
|           |            | FULL-ENCLOSURE  |   EDISP_2D   |
+-----------+------------+-----------------+--------------+
|           |   RPSF     | FULL-ENCLOSURE  |  PSF_TABLE   |
+-----------+------------+-----------------+--------------+
|           |            |                 |  PSF_3GAUSS  |
+-----------+------------+-----------------+--------------+
|           |            |                 |   PSF_KING   |
+-----------+------------+-----------------+--------------+
|           |            |                 |     GTPSF    |
+-----------+------------+-----------------+--------------+
|           |   BKG      |   POINT-LIKE    |    BKG_2D    |
+-----------+------------+-----------------+--------------+
|           |            |                 |    BKG_3D    |
+-----------+------------+-----------------+--------------+
|           |            | FULL-ENCLOSURE  |    BKG_2D    |
+-----------+------------+-----------------+--------------+
|           |            |                 |    BKG_3D    |
+-----------+------------+-----------------+--------------+
