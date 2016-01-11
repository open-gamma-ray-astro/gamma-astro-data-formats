.. include:: ../references.txt

.. _about:

About
=====

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

The documentation is written in `restructured text (RST)`_ and rendered to HTML
and PDF with `Sphinx <http://sphinx-doc.org/index.html>`__ and hosted at `Readthedocs <https://readthedocs.org/>`__.

Everyone can contribute by making a pull request with a change or addition
to https://github.com/gammapy/gamma-astro-data-formats .

We use the Sphinx Readthedocs theme as described
`here <http://docs.readthedocs.org/en/latest/theme.html#how-do-i-use-this-locally-and-on-read-the-docs>`__,
i.e. to build the HTML docs locally you have to `pip install sphinx_rtd_theme` before `make html`.

References
----------

Existing FITS specs and recommendations:

* http://fits.gsfc.nasa.gov/fits_home.html
* http://fits.gsfc.nasa.gov/registry/grouping.html

Existing HEASARC specs and recommendations:

* https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/ofwg_recomm.html
* http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/caldb_doc.html

Other references:

* https://gammapy.readthedocs.org/en/latest/dataformats/index.html
* http://naima.readthedocs.org/en/latest/dataformat.html
* http://docs.astropy.org/en/stable/modeling/
* http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/source_models.html
