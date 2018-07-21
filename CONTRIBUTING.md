# How to contribute

This page describes how to contribute.

## Edit

The documentation is written in
[restructured text (RST)](http://www.sphinx-doc.org/en/master/usage/restructuredtext/) and rendered to HTML
and PDF with [Sphinx](http://www.sphinx-doc.org/en/master/)
and hosted at [Readthedocs](http://gamma-astro-data-formats.readthedocs.io/).

## Pull request

Everyone can contribute by making a pull request with a change or addition
to https://github.com/open-gamma-ray-astro/gamma-astro-data-formats or by
sending comments and feedback via the Github issue tracker, or, for
high-level and important things, to 
https://lists.nasa.gov/mailman/listinfo/open-gamma-ray-astro .

## Run Sphinx

We use the Sphinx Readthedocs theme.
To build the HTML docs locally you first have to install Sphinx.

With pip::

    pip install sphinx sphinx_rtd_theme

If you use conda::

    conda create -n gadf python=3.6 sphinx sphinx_rtd_theme
    conda activate gadf

Then to build and view the HTML docs locally::

    make html
    open build/html/index.html
