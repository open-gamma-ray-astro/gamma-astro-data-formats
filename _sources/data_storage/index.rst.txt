.. _iact-storage:

IACT data storage
=================

At the moment there is no agreed way to organise IACT data, and how to connect
``EVENTS`` with IRFs or other information such as time or pointing information
that is needed for analysis.

Here we document one scheme that is used extensively in H.E.S.S., and partly
also by other IACTs. We expect that it will be superceded in the future by a
different scheme developed by CTA.

The basic idea is that current IACT data consists of "runs" or "observations"
with a given ``OBS_ID``, and that for each observation there is one ``EVENTS``
and several IRF FITS HDUs that contain everything needed to analyse that data.

A second idea is that with H.E.S.S. we export all data to FITS, so we have many
1000s of observations and users usually will need to do a run selection e.g. by
sky position or observation time, and they want to do that in an efficient way
that doesn't require globbing for 1000s of files and opening up the FITS headers
to find out what data is present.

There are two index tables:

.. toctree::
   :maxdepth: 1

   obs_index/index
   hdu_index/index
   
The observation index provides information of meta data about each observation
run. E.g. pointing in the sky, duration, number of events, etc. The HDU index
table provides a list of all available HDUs and in what files they are located.
Science tools can make use of this index files to build filenames of required
files according to some user parameters.

Note that the HDU index table would be superfluous if IRFs were always bundled
in the same file with ``EVENTS`` and if the observation index table contained
the location of that file. For HESS this wasn't done initially, because the
background IRFs were large in size and re-used for many runs. The level of
indirection that the HDU index table offers allows to support both IRFs bundled
with EVENTS ("per-run IRFs" as used in HESS) as well as the use of a global
lookup database of IRFs located separately from EVENTS (sometimes called a
CALDB), as used for the CTA first data challenge.
