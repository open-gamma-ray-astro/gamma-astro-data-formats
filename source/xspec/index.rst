.. include:: ../references.txt

OGIP  1D data formats
=====================

The :ref:`iact-events` and 2D :ref:`iact-irfs` can be transformed into a 1D counts vector and 1D IRFs that can serve as input to general X-ray spectral analysis packages such as Sherpa_. For an introduction to this so-called OGIP data format please refer to the official `Documentation <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/spectra/ogip_92_007/ogip_92_007.html>`__ on :ref:`glossary-heasarc`.


The following section only highlight differences and modifications made to the OGIP standard in order to meet the requirement of gamma-astronomy.


PHA file
--------
The OGIP standard PHA file format is described `here <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/spectra/ogip_92_007/node5.html>`__. Additional header keyword that can be stored in the PHA header for :ref:`glossary-IACT` analysis are listed below. 

* ``OFFSET`` type: tbd, unit deg
    * Distance between observation position and target of spectral analysis
* ``MUONEFF`` type: tbd
    * Muon efficiency of the observation
* ``ZEN`` type: tbd, unit: deg
    * Zenith angle of the observation



BKG file
--------


ARF file
--------
The OGIP standard ARF file format is described `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_002/cal_gen_92_002.html#tth_sEc4>`__

RMF file
--------
The OGIP standard RMF file format is described `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_002/cal_gen_92_002.html#tth_sEc3.1>`__




