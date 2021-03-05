.. include:: ../references.txt

.. _iact-events:

EVENTS
======

The ``EVENTS`` extension is a binary FITS table that contains an event list.
Each row of the table provides information that characterises one event.
The mandatory and optional columns of the table are listed below. In
addition, a list of header keywords providing metadata is specified.
Also here there are mandatory and optional keywords.
The recommended extension name of the binary table is ``EVENTS``.


Mandatory columns
-----------------

We follow the `OGIP event list`_ standard.

* ``EVENT_ID`` type: int64
    * Event identification number at the DL3 level.
      See notes on :ref:`iact-events-event-id` below.
* ``TIME`` type: float64, unit: s
    * Event time (see :ref:`time`)
* ``RA`` type: float, unit: deg
    * Reconstructed event Right Ascension (see :ref:`coords-radec`).
* ``DEC`` type: float, unit: deg
    * Reconstructed event Declination (see :ref:`coords-radec`).
* ``ENERGY`` type: float, unit: TeV
    * Reconstructed event energy.

Optional columns
----------------

.. note::
   None of the following columns is required to be part of an ``EVENTS``
   extension. Any software **using** these columns should first check whether the
   columns exist, and warn in case of their absence. Any software **ignoring**
   these columns should make sure that their presence does not detoriate the
   functioning of the software.

* ``EVENT_TYPE`` type: bit field (in FITS ``tform=32X``)
    * Event quality partition.
* ``MULTIP`` type: int
    * Telescope multiplicity. Number of telescopes that have seen the event.
* ``GLON`` type: float, unit: deg
    * Reconstructed event Galactic longitude (see :ref:`coords-galactic`).
* ``GLAT`` type: float, unit: deg
    * Reconstructed event Galactic latitude (see :ref:`coords-galactic`).
* ``ALT`` type: float, unit: deg
    * Reconstructed altitude (see :ref:`coords-altaz`)
* ``AZ`` type: float, unit: deg
    * Reconstructed azimuth (see :ref:`coords-altaz`)
* ``DETX`` type: float, unit: deg
    * Reconstructed field of view X (see :ref:`coords-fov`).
* ``DETY`` type: float, unit: deg
    * Reconstructed field of view Y (see :ref:`coords-fov`).
* ``THETA`` type: float, unit: deg
    * Reconstructed field of view offset angle (see :ref:`coords-fov`).
* ``PHI`` type: float, unit: deg
    * Reconstructed field of view position angle (see :ref:`coords-fov`).
* ``GAMMANESS`` type: float
    * Classification score of a signal / background separation. SHOULD be between 0 and 1, with higher values indicating larger confidence that the event was produced by a gamma ray.
* ``DIR_ERR`` type: float, unit: deg
    * Direction error of reconstruction 
* ``ENERGY_ERR`` type: float, unit: TeV
    * Error on reconstructed event energy
* ``COREX`` type: float, unit: m
    * Reconstructed core position X of shower
* ``COREY`` type: float, unit: m
    * Reconstructed core position Y of shower
* ``CORE_ERR`` type: float, unit: m
    * Error on reconstructed core position of shower
* ``XMAX`` type: float, unit: radiation lengths
    * First interaction depth 
* ``XMAX_ERR`` type: float, unit: radiation lengths
    * Error on first interaction depth 
* ``HIL_MSW`` type: float
    * Hillas mean scaled width
* ``HIL_MSW_ERR`` type: float
    * Hillas mean scaled width error
* ``HIL_MSL`` type: float
    * Hillas mean scaled length
* ``HIL_MSL_ERR`` type: float
    * Hillas mean scaled length error


Mandatory header keywords
-------------------------

The standard FITS reference time header keywords should be used (see :ref:`time-formats`).
An observatory Earth location should be given as well (see :ref:`coords-location`).

* ``HDUCLASS`` type: string
    * Signal conformance with HEASARC/OGIP conventions (option: 'OGIP'). See :ref:`hduclass`.
* ``HDUDOC`` type: string
    * Reference to documentation where data format is documented. See :ref:`hduclass`.
* ``HDUVERS`` type: string
    * Version of the format (e.g. '1.0.0'). See :ref:`hduclass`.
* ``HDUCLAS1`` type: string
    * Primary extension class (option: 'EVENTS'). See :ref:`hduclass`.
* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``TSTART`` type: float, unit: s
    * Start time of observation (relative to reference time, see :ref:`time`)
* ``TSTOP`` type: float, unit: s
    * End time of observation (relative to reference time, see :ref:`time`)
* ``ONTIME`` type: float, unit: s
    * Total *good time* (sum of length of all Good Time Intervals).
      If a Good Time Interval (GTI) table is provided, ``ONTIME`` should be
      calculated as the sum of those intervals. Corrections for instrumental
      *dead time* effects are **NOT** included.
* ``LIVETIME`` type: float, unit: s
    * Total time (in seconds) on source, corrected for the *total* instrumental
      dead time effect.
* ``DEADC`` type: float
    * Dead time correction, defined by ``LIVETIME/ONTIME``.
      Is comprised in [0,1]. Defined to be 0 if ``ONTIME=0``.
* ``RA_PNT`` type: float, unit: deg
    * Pointing Right Ascension (see :ref:`coords-radec`).
* ``DEC_PNT`` type: float, unit: deg
    * Pointing declination (see :ref:`coords-radec`).
* ``EQUINOX`` type: float
    * Equinox in years for the celestial coordinate system in which positions
      given in either the header or data are expressed (options: 2000.0).
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``RADECSYS`` type: string
    * Stellar reference frame used for the celestial coordinate system in
      which positions given in either the header or data are expressed.
      (options: 'ICRS', 'FK5').
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``ORIGIN`` type: string
    * Organisation that created the FITS file.
      This can be the same as ``TELESCOP`` (e.g. "HESS"), but it could
      also be different if an organisation has multiple telescopes (e.g. "NASA" or "ESO").
* ``TELESCOP`` type: string
    * Telescope (e.g. 'CTA', 'HESS', 'VERITAS', 'MAGIC', 'FACT')
* ``INSTRUME`` type: string
    * Instrument used to aquire the data contained in the file.
      Each organisation and telescop has to define this.
      E.g. for CTA it could be 'North' and 'South', or sub-array configurations,
      this has not been defined yet.
* ``CREATOR`` type: string
    * Software that created the file. When appropriate, the value of the
      ``CREATOR`` keyword should also reference the specific version of the
      program that created the FITS file. It is intented that this keyword
      should refer to the program that originally defined the FITS file
      structure and wrote the contents. If a FITS file is subsequently
      copied largely intact into a new FITS by another program, then the value
      of the ``CREATOR`` keyword should still refer to the original program.
      ``HISTORY`` keywords should be used instead to document any further
      processing that is performed on the file after it is created.
      For more reading on the OGIP standard, see
      `here <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/r7.html>`_.


Optional header keywords
------------------------

* ``OBSERVER`` type: string
    * Name of observer. This could be for example the PI of a proposal.
* ``CREATED`` type: string
    * Time when file was created in ISO standard date representation
      "ccyy-mm-ddThh:mm:ss" (UTC)
* ``OBJECT`` type: string
    * Observed object (e.g. 'Crab')
* ``RA_OBJ`` type: float, unit: deg
    * Right ascension of ``OBJECT``
* ``DEC_OBJ`` type: float, unit: deg
    * Declination of ``OBJECT``                
* ``OBS_MODE`` type: string
    * Observation mode. See notes on :ref:`iact-events-obs-mode` below.
* ``EV_CLASS`` type: str
    * Event class. See notes on :ref:`iact-events-class-type` below.
* ``TELAPSE`` type: float, unit: s
    * Time interval between start and stop time (``TELAPSE=TSTOP-TSTART``).
      Any gaps due to bad weather, or high background counts and/or other
      anomalies, are included.

.. warning::
   Keywords below seem to be pretty low-level and eventually instrument
   specific. It needs to be discussed whether a recommendation on these
   keywords should be made, or whether the definition should be left
   to the respective consortia.

* ``HDUCLAS2`` type: string
    * Secondary extension class (option: 'ACCEPTED'). See :ref:`hduclass`.
* ``TELLIST`` type: string
    * Telescope IDs in observation (e.g. '1,2,3,4')   
* ``N_TELS`` type: int
    * Number of observing telescopes       
* ``TASSIGN`` type: string
    * Place of time reference ('Namibia')
* ``DST_VER`` type: string
    * Version of DST/Data production 
* ``ANA_VER`` type: string
    * Reconstruction software version   
* ``CAL_VER`` type: string
    * Calibration software version 
* ``CONV_DEP`` type: float
    * convergence depth (0 for parallel pointing)  
* ``CONV_RA`` type: float, unit: deg
    * Convergence Right Ascension    
* ``CONV_DEC`` type: float, unit: deg
    * Convergence Declination
* ``TRGRATE`` type: float, unit: Hz
    * Mean system trigger rate
* ``ZTRGRATE`` type: float, unit: Hz
    * Zenith equivalent mean system trigger rate    
* ``MUONEFF`` type: float
    * Mean muon efficiency
* ``BROKPIX`` type: float
    * Fraction of broken pixels (0.15 means 15% broken pixels)
* ``AIRTEMP`` type: float, unit: deg C
   * Mean air temperature at ground during the observation.
* ``PRESSURE`` type: float, unit: hPa
   * Mean air pressure at ground during the observation.
* ``RELHUM`` type: float
   * Relative humidity
* ``NSBLEVEL`` type: float, unit: a.u.
   * Measure for night sky background level

.. _iact-events-notes:

Notes
-----

This paragraph contains some explanatory notes on some of the columns
and header keys mentioned above.

.. _iact-events-event-id:

EVENT_ID
~~~~~~~~

Most analyses with high-level science tools don't need ``EVENT_ID`` information.
But being able to uniquely identify every event is important, e.g. when
comparing the high-level reconstructed event parameters (``RA``, ``DEC``,
``ENERGY``) for different calibrations, reconstructions or gamma-hadron
separations.

Assigning a unique ``EVENT_ID`` during data taking can be difficult or
impossible. E.g. in H.E.S.S. we have two numbers ``BUNCH_ID_HESS`` and
``EVENT_ID_HESS`` that only together uniquely identify an event within a given
run (i.e. ``OBS_ID``). Probably the scheme to uniquely identify events at the
DL0 level for CTA will be even more complicated, because of the much larger
number of telescopes and events.

So given that data taking and event identification is different for every IACT
at low data levels and is already fixed for existing IACTs, we propose here to
have an ``EVENT_ID`` that is simpler and works the same for all IACTs at the DL3
level.

As an example: for H.E.S.S. we achieve this by using an INT64 for ``EVENT_ID``
and to store ``EVENT_ID = (BUNCH_ID_HESS << 32) | (EVENT_ID_HESS)``, i.e. use
the upper bits to contain the low-level bunch ID and the lower bits to contains
the low-level event ID. This encoding is unique and reversible, i.e. it's easy
to go back to ``BUNCH_ID_HESS`` and ``EVENT_ID_HESS`` for a given ``EVENT_ID``,
and to low-level checks (e.g. look at the shower images for a given event that
behaves strangely in reconstructed high-level parameters).

.. _iact-events-class-type:

EV_CLASS and EVENT_TYPE
~~~~~~~~~~~~~~~~~~~~~~~

Currently in this format specification, event class ``EV_CLASS`` is a header key
(i.e. the same for all events in a given event list) and ``EVENT_TYPE`` is a
bitfield column (i.e. can have a different value for each event). Both are
optional at this time, only used as provenance information, not by science tools
to make any decisions how to analyse the data.

The reason for this is simply that we have not agreed yet on a scheme what event
class and event type means, and how it should be used by science tools for
analysis. Developing this will be one of the major topics for the next version
of the spec. It is likely that a proper definition of event classes and types
will not be compatible with what is currently defined here, so not filling
``EV_CLASS`` and ``EVENT_TYPE`` when creating DL3 data is not a bad idea.

To summarise a bit the discussions on this important point in the past years,
they were mostly done by looking at what Fermi-LAT is doing and some
prototyping in H.E.S.S. to export DL3 data to FITS.

The scheme in Fermi-LAT for event classes and event types is nicely summarised
`here
<https://github.com/gammapy/PyGamma15/blob/gh-pages/talks/fermi2/fermi_advanced_v0.pdf>`__
or `here
<https://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/Cicerone_Data/LAT_DP.html>`__.
There event classes and types are key parts of the data model, used for EVENT to
IRF association and even end users need to learn about them and pass event class
and type information when using science tools.

One option could be to mostly adopt what Fermi-LAT does for IACTs. However, a
major difference is that Fermi-LAT is a more stable detector, that has a CALDB
of a very limited number or IRFs that can be used for all data, whereas for
IACTs with changing telescope configurations, degrading mirrors, changing
atmosphere, zenith angle, ... most likely we will have to produce per-observation
IRFs, and then it's easier to bundle the IRFs with the EVENTS in one file,
and the use of event class and type to link EVENTS and IRFs is no longer needed.

An alternative scheme is to use the term "event class" to describe a given
analysis configuration. This is e.g. how we currently use ``EV_CLASS`` in
H.E.S.S., we fill values like "standard" or "hard" or "loose" to describe a
given full configuration that is the result of a calibration, event
reconstruction and gamma-hadron separation pipeline. This is similar to what
Fermi-LAT does, except less sophisticated, the event classes are completely
independent, there is no nesting, and separate events and IRF files are produced
for each class/configuration. To analyse data from a given class, the user
chooses which set of files to download (e.g. "loose" for pulsars or "hard" for a
bright source where a good PSF is needed), and then the science tools don't need
to do anything with ``EV_CLASS``, it is just provenance information. Some people
are experimenting with the use of ``EVENT_TYPE`` in a similar way as Fermi-LAT,
e.g. to have event quality partitioning based on number of telescopes that saw a
given event, or other criteria. Again, it is left to users to split events by
``EVENT_TYPE`` and produce IRFs for each event type and pass those for a joint
fit to the science tools, as there is no agreement or implementation yet in the
science tools to support ``EVENT_TYPE`` directly.

So to conclude and summarise again: ``EV_CLASS`` and ``EVENT_TYPE`` as mentioned
here in this spec are optional and very preliminary. Defining event class and
type for IACTs needs more prototyping by the science tools and current IACTs and
CTA and discussion, and then a proposal for a specification.

.. _iact-events-obs-mode:

OBS_MODE 
~~~~~~~~

The observation mode ``OBS_MODE`` is currently provenance information, not used
by science tools to decide how to analyse the data. There is no set of defined
modes yet. Thus, at the moment it is optional.

Just to give an example: in H.E.S.S. the values of "WOBBLE" for wobble
observations (pointing slightly off target) and "SCAN" for Galactic plane survey
observation on a grid of sky positions (not wrt. a specific target) is used.

It is likely that ``OBS_MODE`` in the future will be a key piece of information
in the DL3 data model, defining the observation mode (e.g. pointed, divergent,
slewing, ...) and being required to analyse the data correctly.
