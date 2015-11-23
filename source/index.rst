Data formats for gamma-ray astronomy
====================================

A place to propose and share data format descriptions for gamma-ray astronomy.

* Repository: https://github.com/gammapy/gamma-astro-data-formats
* Docs: http://gamma-astro-data-formats.readthedocs.org/

Table of contents
-----------------

.. toctree::

   source-models/index
   irfs/index

What is this?
-------------

This is a grassroots effort to describe data formats that are in use,
but are not specified anywhere else. Examples range from FITS format instrument
response functions for imaging atmospheric Cherenkov telescopes (IACTs)
to YAML format spectral and spatial model specifications,
to high-level analysis results like spectra and light curves.

The formats described here and the whole effort are not official in any way,
i.e. not supported or ratified by any institutes, collaborations or committees.
In some cases the formats described here will likely be adopted or superceded
by more official formats in the coming years.

Everyone is welcome to adopt these formats or even contribute,
development and discussion is done openly on Github.
Especially if you are a software library or tool developer,
we encourage you to support the formats described here instead of inventing your own.

How to contribute?
------------------

The documentation is written in restructured text (RST) and rendered to HTML
and PDF with Sphinx and hosted at Readthedocs.

Everyone can contribute by making a pull request with a change or addition
to https://github.com/gammapy/gamma-astro-data-formats .

References
----------

Some relevant references:

* https://gammapy.readthedocs.org/en/latest/dataformats/index.html
* http://naima.readthedocs.org/en/latest/dataformat.html
* http://docs.astropy.org/en/stable/modeling/
* http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/source_models.html


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
