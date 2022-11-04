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

We use the Sphinx Readthedocs theme and manage dependencies using poetry.

You first need to install `poetry`.

With pip::

    pip install poetry

Then to build and view the HTML docs locally::

    poetry install
    poetry run make html
    poetry run python -m http.server -d build/html/index.html
