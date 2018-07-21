.. include:: references.txt

.. _about:

About
=====

In gamma-ray astronomy, a variety of data formats and proprietary software have
been traditionally used, often developed for one specific mission or experiment.
Especially for ground-based imaging atmospheric Cherenkov telescopes (IACTs),
data and software are mostly private to the collaborations operating the
telescopes. However, there is a general movement in science towards the use of
open data and software. In addition, the next-generation IACT instrument, the
Cherenkov Telescope Array (CTA), will be operated as an open observatory. 

To work towards open and interoperable data formats for gamma-ray astronomy, we
have started this open data format specification. This was started at the
`PyGamma15 workshop`_ in November 2017, followed by a `meeting in April 2016 in
Meudon`_ and another `meeting in March 2017 in Heidelberg`_. Version
0.1 of the spec was release in April 2016, version 0.2 in July 2018. You can
find more information about this effort in `Deil et al. (2017)
<https://adsabs.harvard.edu/abs/2017AIPC.1792g0006D>`__.

The scope of this effort is to cover all **high-level** data from gamma-ray
telescopes, starting at the level of event lists and IRFs, also covering reduced
IRFs, maps, spectra, light curves, up to source models and catalogs. Both
pointing (IACT) and slewing (Fermi-LAT, HAWC) telescope data is in scope. To a
large degree, the formats should also be useful for other astroparticle data,
e.g. from cosmic rays or neutrinos.

All of the data formats described here at the moment can be, and in practice
mostly are, stored in FITS. Some experimentation with HDF5 and ECSV is ongoing.
The data format specifications don't explicity mention the serialisation format,
but rather the key name and data type for each metadata or data field.

The formats described here are partially in use by current instruments
(Fermi-LAT, HESS, VERITAS, MAGIC, FACT) as well as in the next-generation
Cherenkov Telescope Array CTA. Prototyping and support for many of the formats
here is happening in the CTA science tool prototypes `Gammapy`_ and `ctools`_,
the data formats are being used e.g. in `gamma-cat`_.

However, we would like to stress that this is an inofficial effort, the formats
described here are work in progress and have not been officially adopted by any
of the mentioned instruments. The expectation is that CTA partially adopt these
formats, and partially develop new ones in the time frame 2018-2020, and then
the other IACTs will use the official format chosen by CTA.

Development of this data format specification happens at
https://github.com/open-gamma-ray-astro/gamma-astro-data-formats, information
how to contribute is given in ``CONTRIBUTING.md`` there. Discussion on major and
controversial points should happen on the mailing list
(https://lists.nasa.gov/mailman/listinfo/open-gamma-ray-astro). So far, no
official decision process exists, so some discussions are stuck because of major
differences in opinion. Probably, moving forward, decisions will be made not in
this open forum, but rather by the major instruments via their choices,
especially CTA.
