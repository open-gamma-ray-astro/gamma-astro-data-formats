.. include:: ../references.txt

.. _hdu-hierarchy:

HDU hierarchy
=============
 
Following NASA's recommendation 
(see `HFWG Recommendation R8 <http://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/general/ogip_94_006/ogip_94_006.html>`__), 
a hierarchical classification is applied to each HDU within DL3 FITS files, 
using the HDUCLASS and HDUCLASn keywords.

Some useful links from other projects:

* http://cxc.harvard.edu/contrib/arots/fits/content.txt
* https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/hduclas.html
* http://www.starlink.rl.ac.uk/docs/sun167.htx/sun167se3.html
* https://confluence.slac.stanford.edu/display/ST/LAT+Photons

The current scheme used is the following:

* HDUCLASS: General identifier of the data format. Recommended value: "OGIP"

* HDUCLAS1: General type of HDU, currently: ``EVENTS``, ``GTI`` or ``RESPONSE``

* HDUCLAS2: In case of ``RESPONSE`` type, refers to the IRF components stored within the HDU: ``EFF_AREA``, ``BKG``, ``EDISP`` or ``RPSF``

* HDUCLAS3: In case of ``RESPONSE`` type, refers to the way the IRF component was produced (``POINT-LIKE`` or ``FULL-ENCLOSURE``)

* HDUCLAS4: In case of ``RESPONSE`` type, refers to the name of the specific format

+------------+-----------+------------+-----------------+--------------+
|  HDUCLASS  |  HDUCLAS1 |  HDUCLAS2  |  HDUCLAS3       |   HDUCLAS4   |
+============+===========+============+=================+==============+
|    OGIP    |    GTI    |            |                 |              |
+------------+-----------+------------+-----------------+--------------+
|            |  EVENTS   |            |                 |              |
+------------+-----------+------------+-----------------+--------------+
|            |  RESPONSE | EFF_AREA   |   POINT-LIKE    |   aeff_2d    |
+------------+-----------+------------+-----------------+--------------+
|            |           |            |                 | aeff_2d_reco |
+------------+-----------+------------+-----------------+--------------+
|            |           |            | FULL-ENCLOSURE  |   aeff_2d    |
+------------+-----------+------------+-----------------+--------------+
|            |           |            |                 | aeff_2d_reco |
+------------+-----------+------------+-----------------+--------------+
|            |           |   EDISP    |   POINT-LIKE    |   edisp_2d   |
+------------+-----------+------------+-----------------+--------------+
|            |           |            | FULL-ENCLOSURE  |   edisp_2d   |
+------------+-----------+------------+-----------------+--------------+
|            |           |   RPSF     | FULL-ENCLOSURE  |  psf_table   |
+------------+-----------+------------+-----------------+--------------+
|            |           |            |                 |  psf_3gauss  |
+------------+-----------+------------+-----------------+--------------+
|            |           |            |                 |   psf_king   |
+------------+-----------+------------+-----------------+--------------+
|            |           |            |                 |     gtpsf    |
+------------+-----------+------------+-----------------+--------------+
|            |           |   BKG      |   POINT-LIKE    |    bkg_2d    |
+------------+-----------+------------+-----------------+--------------+
|            |           |            |                 |    bkg_3d    |
+------------+-----------+------------+-----------------+--------------+
|            |           |            | FULL-ENCLOSURE  |    bkg_2d    |
+------------+-----------+------------+-----------------+--------------+
|            |           |            |                 |    bkg_3d    |
+------------+-----------+------------+-----------------+--------------+

.. code-block:: bash

  HDUCLASS   HDUCLAS1     HDUCLAS2     HDUCLAS3          HDUCLAS4   

  OGIP       GTI   
             EVENTS     
             RESPONSE     EFF_AREA     POINT-LIKE        aeff_2d
                                                         aeff_2d_reco
                                       FULL-ENCLOSURE    aeff_2d
                                                         aeff_2d_reco
                          RPSF         FULL-ENCLOSURE    psf_table
                                                         psf_3gauss
                                                         psf_king
                                                         gtpsf
                          EDISP        POINT-LIKE        edisp_2d
                                       FULL-ENCLOSURE    edisp_2d
                          BKG          POINT-LIKE        bkg_2d
                                                         bkg_3d
                                       FULL-ENCLOSURE    bkg_2d
                                                         bkg_3d