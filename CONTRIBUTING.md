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

We use the Sphinx Readthedocs theme and manage dependencies using uv.

You first need to [install uv](https://docs.astral.sh/uv/getting-started/installation/).

To build and preview the HTML docs with live reload, run

    uv run --locked make dev

Open <http://127.0.0.1:8000> in your browser.
