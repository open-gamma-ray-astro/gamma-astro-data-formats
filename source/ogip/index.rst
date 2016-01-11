.. include:: ../references.txt

OGIP  1D data formats
=====================

The :ref:`iact-events` and 2D :ref:`iact-irfs` can be transformed into a 1D counts vector and 1D IRFs that can serve as input to general X-ray spectral analysis packages such as Sherpa_. For an introduction to this so-called OGIP data format please refer to the official `Documentation <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/spectra/ogip_92_007/ogip_92_007.html>`__ on :ref:`glossary-heasarc`.


The following section only highlight differences and modifications made to the OGIP standard in order to meet the requirements of gamma-astronomy.


PHA file
--------
The OGIP standard PHA file format is described `here <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/spectra/ogip_92_007/node5.html>`__.

TODO: Should an EBOUNDS extension be added to the PHA file (channels -> energy)? In OGIP this info has to be extraced from the RMF file.

The values of following header keywords need some attention when using them for :ref:`glossary-IACT` analysis.

* ``BACKSCAL``
    * For now it is assumed that exposure ration between signal and background counts does not depend on energy, thus this keyword must be set
    * The BACKSCAL keywords in the PHA and the BKG file must be set so that 

      .. math:: \alpha = \frac{\mathrm{PHA}_{\mathrm{backscal}}}{\mathrm{BKG}_{\mathrm{backscal}}}
    * It is recommended to set the ``BACKSCAL`` keyword to 1 in the PHA file and to :math:`1/\alpha` in the BKG file


Additional header keyword that can be stored in the PHA header for :ref:`glossary-IACT` analysis are listed below. 

* ``OFFSET`` type: tbd, unit deg
    * Distance between observation position and target of a spectral analysis
* ``MUONEFF`` type: tbd
    * Muon efficiency of the observation
* ``ZEN`` type: tbd, unit: deg
    * Zenith angle of the observation


BKG file
--------
The values of following header keywords need some attention when using them for :ref:`glossary-IACT` analysis.

* ``BACKSCAL``
    * It is recommended to set the ``BACKSCAL`` keyword to :math:`1/\alpha` in the BKG file (see above)


ARF file
--------
The OGIP standard ARF file format is described `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_002/cal_gen_92_002.html#tth_sEc4>`__

Additional header keyword that can be stored in the PHA header for :ref:`glossary-IACT` analysis are listed below. 

* ``LO_THRES`` type: tbd, unit: TeV
    * Low energy threshold of the analysis
* ``HI_THRES`` type: tbd, unit: TeV
    * High energy threshold of the analysis

RMF file
--------
The OGIP standard RMF file format is described `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_002/cal_gen_92_002.html#tth_sEc3.1>`__




