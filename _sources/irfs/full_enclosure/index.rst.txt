.. include:: ../../references.txt

.. _full-enclosure-irfs:

Full-enclosure IRFs
===================

Full-enclosure IRF format has been used for calibration data and IRF of
X-ray instruments, as well as for the IRFs that are distributed with the Fermi-LAT
science tools.

Any full-enclosure IRF component should contain the header keyword:

* ``HDUCLAS3 = FULL-ENCLOSURE``

From here on, the specific format of each IRF component:

.. toctree::

   aeff/index
   edisp/index
   psf/index
   bkg/index
