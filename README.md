# Data formats for gamma-ray astronomy

A place to propose and share data format descriptions for gamma-ray astronomy.

* Repository: https://github.com/open-gamma-ray-astro/gamma-astro-data-formats
* Docs: https://gamma-astro-data-formats.readthedocs.io/
* Mailing list: https://lists.nasa.gov/mailman/listinfo/open-gamma-ray-astro

## Stable versions

Stable versions of the spec are done via git tags and are shown as releases here:
https://github.com/open-gamma-ray-astro/gamma-astro-data-formats/releases

HTML and PDF versions for stable versions are available via the version selector
in the lower left on ReadTheDocs. As an example, for version 0.2:

- HTML at https://gamma-astro-data-formats.readthedocs.io/en/v0.2/
- PDF at https://media.readthedocs.org/pdf/gamma-astro-data-formats/v0.2/gamma-astro-data-formats.pdf

For v0.2 we also archived the sources of the spec as well as a rendered PDF and HTML version here:
https://doi.org/10.5281/zenodo.1409830 
To cite that version, you can use the bibtex entry [here](https://zenodo.org/record/1409831/export/hx#.W5EBLNgzY_U).

## Building the documents locally

To build this document locally, clone this repository and install `poetry`,
the tool used for dependency management:
```bash
$ python3 -m pip install [--user] poetry
```
Use `--user` if you are using a system python installation, leave it out if
you are in a virtual environment or conda environment already.

Install the dependencies for building this document:
```
$ poetry install
```

Make the html:
```
$ poetry run make html
```

Start the python http server to get a preview in your browser:
```
$ python3 -m http.server -d build/html
```

You then should be able to browse <http://localhost:8000> and see the document.
