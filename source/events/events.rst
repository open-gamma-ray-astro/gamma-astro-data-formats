.. include:: ../references.txt

.. iact-events:

``EVENTS`` extension
====================

The ``EVENTS`` extension is a binary FITS table that contains an event list.
Each row of the table provides information that characterises one event.
The mandatory and optional columns of the table are listed below. In
addition, a list of header keywords providing metadata is specified.
Also here there are mandatory and optional keywords.
The recommended extension name of the binary table is ``EVENTS``.


Mandatory columns
-----------------

* ``EVENT_ID`` tform: ``1J``
    * Event identification number at the DL3 level
      (lower data levels could be different, see note below).
* ``TIME`` tform: ``1D``, unit: s
    * Time stamp of event in instrument specific MJD time reference. See the
      header keywords ``MJDREFI`` and ``MJDREFF`` for the zero point of
      the reference time.
      See also the `OGIP event list`_ standard.
* ``RA`` tform: ``1E``, unit: deg
    * Reconstructed event Right Ascension (see :ref:`sky-coordinates-radec`).
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``DEC`` tform: ``1E``, unit: deg
    * Reconstructed event Declination (see :ref:`sky-coordinates-radec`).
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``ENERGY`` tform: ``1E``, unit: TeV
    * Reconstructed event energy.
      See also the `OGIP event list`_ standard.
* ``DETX`` tform: ``1E``, unit: deg
    * Reconstructed event X-coordinate in detector system
      (nominal system, see :ref:`sky-coordinates-fov`).
      See also the `OGIP event list`_ standard.
* ``DETY`` tform: ``1E``, unit: deg
    * Reconstructed event Y-coordinate in detector system
      (nominal system, see :ref:`sky-coordinates-fov`).
      See also the `OGIP event list`_ standard.


Optional columns
----------------

.. note::
   None of the following columns is required to be part of an ``EVENTS``
   extension. Any software **using** these columns should first check whether the
   columns exist, and warn in case of their absence. Any software **ignoring**
   these columns should make sure that their presence does not detoriate the
   functioning of the software.

* ``EVENT_TYPE`` tform: ``32X``
    * Event quality partition.
* ``ALT`` tform: ``1E``, unit: deg
    * Reconstructed altitude coordinate of event
      (horizon system, see :ref:`sky-coordinates-altaz`)
* ``AZ`` tform: ``1E``, unit: deg
    * Reconstructed azimuth coordinate of event
      (horizon system, see :ref:`sky-coordinates-altaz`)
* ``THETA`` tform: ``1E``, unit: deg
    * Reconstructed offset from the observation pointing position
* ``PHI`` tform: ``1E``, unit: deg
    * Reconstructed position angle from the observation pointing position
      (position angles are counted counterclockwise from celestial North)
* ``MULTIP`` tform: ``1I``
    * Telescope multiplicity. Number of telescopes that have seen the event
* ``DIR_ERR`` tform: ``1E``, unit: deg
    * Direction error of reconstruction 
* ``ENERGY_ERR`` tform: ``1E``, unit: TeV
    * Error on reconstructed event energy
* ``COREX`` tform: ``1E``, unit: m
    * Core position X of shower
* ``COREY`` tform: ``1E``, unit: m
    * Core position Y of shower
* ``CORE_ERR`` tform: ``1E``, unit: m
    * Error on core position of shower    
* ``XMAX`` tform: ``1E``, unit: radiation lengths
    * First interaction depth 
* ``XMAX_ERR`` tform: ``1E``, unit: radiation lengths
    * Error on first interaction depth 
* ``HIL_MSW`` tform: ``1E``
    * Hillas mean scaled width
* ``HIL_MSW_ERR`` tform: ``1E``
    * Hillas mean scaled width error
* ``HIL_MSL`` tform: ``1E``
    * Hillas mean scaled length
* ``HIL_MSL_ERR`` tform: ``1E``
    * Hillas mean scaled length error


Mandatory header keywords
-------------------------

* ``HDUCLASS`` type: string
    * Signal conformance with HEASARC/OGIP conventions (option: 'OGIP').
      For more information, refer to the `OGIP standard
      <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/hduclas.html>`_.
* ``HDUDOC`` type: string
    * Reference to documentation where data format is documented.
      For more information, refer to the `OGIP standard
      <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/hduclas.html>`_.
* ``HDUVERS`` type: string
    * Version of the format (e.g. '1.0.0')
      For more information, refer to the `OGIP standard
      <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/hduclas.html>`_.
* ``HDUCLAS1`` type: string
    * Primary extension class (option: 'EVENTS').
      For more information, refer to the `OGIP standard
      <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/hduclas.html>`_.
* ``HDUCLAS2`` type: string
    * Secondary extension class (option: 'ACCEPTED').
      For more information, refer to the `OGIP standard
      <https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/ofwg_recomm/hduclas.html>`_.
* ``ORIGIN`` type: string
    * Organisation that created the FITS file.
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
* ``TELESCOP`` type: string
    * Telescope (e.g. 'CTA', 'HESS', 'VERITAS', 'MAGIC')
* ``INSTRUME`` type: string
    * Instrument used to aquire the data contained in the file
      (e.g. 'North', 'South')
* ``OBSERVER`` type: string
    * Name of observer (e.g. 'Joe Public'). This could be for example the PI
      of a proposal.
* ``OBJECT`` type: string
    * Observed object (e.g. 'Crab')
* ``OBS_MODE`` type: string
    * Observation mode (e.g. 'WOBBLE', 'SCAN', 'SLEW', or any mode that is
      supported by ``TELESCOP``; string should be upper case)
* ``OBS_ID`` type: int
    * Unique observation identifier (Run number)
* ``DATE-OBS`` type: string
    * Start date of observation in ISO standard date representation
      "ccyy-mm-ddThh:mm:ss" (UTC)
* ``DATE-END`` type: string
    * End date of observation in ISO standard date representation
      "ccyy-mm-ddThh:mm:ss" (UTC)
* ``TSTART`` type: float, unit: s
    * Start time of observation
      (given in instrument specific time reference, see below)
* ``TSTOP`` type: float, unit: s
    * End time of observation
      (given in instrument specific time reference, see below)
* ``MJDREFI`` type: int, unit: days
    * Integer part of instrument specific MJD time reference
* ``MJDREFF`` type: float, unit: days
    * Float part of instrument specific MJD time reference       
* ``TIMEUNIT`` type: string
    * Time unit (e.g. 's')
* ``TIMESYS`` type: string
    * Time system (e.g. 'TT', 'MJD', 'JD', 'TJD')
* ``TIMEREF`` type: string
    * Time reference frame, used for example for barycentric corrections
      (options: 'LOCAL', 'SOLARSYSTEM', 'HELIOCENTRIC', 'GEOCENTRIC')
* ``EQUINOX`` type: float
    * Equinox in years for the celestial coordinate system in which positions
      given in either the header or data are expressed (options: 2000.0).
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``RADECSYS`` type: string
    * Stellar reference frame used for the celestial coordinate system in
      which positions given in either the header or data are expressed.
      (options: 'ICRS', 'FK5').
      See also `HFWG Recommendation R3`_ for the OGIP standard.
* ``TELAPSE`` type: float, unit: s
    * Time interval between start and stop time (``TELAPSE=TSTOP-TSTART``).
      Any gaps due to bad weather, or high background counts and/or other
      anomalies, are included.
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
* ``EVENT_CLASS`` type: int
    * Event class (the 'cut' that has been used, e.g. 'STD', 'HARD', 'SOFT')'.


Optional header keywords
------------------------

* ``CREATED`` type: string
    * Time when file was created in ISO standard date representation
      "ccyy-mm-ddThh:mm:ss" (UTC)
* ``RA_OBJ`` type: float, unit: deg
    * Right ascension of ``OBJECT``
* ``DEC_OBJ`` type: float, unit: deg
    * Declination of ``OBJECT``                

.. warning::
   Keywords below seem to be pretty low-level and eventually instrument
   specific. It needs to be discussed whether a recommendation on these
   keywords should be made, or whether the definition should be left
   to the respective consortia.

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
    * TODO: define how muon efficiency is defined (it's very tricky to get a
      comparable number in HESS from HD and PA calibration)
* ``BROKPIX`` type: float
    * Fraction of broken pixels (0.15 means 15% broken pixels)
* ``AIRTEMP`` type: float, unit: deg C
   * Mean air temperature at ground during the observation.
* ``PRESSURE`` type: float, unit: hPa
   * Mean air pressure at ground during the observation.
* ``NSBLEVEL`` type: float, unit: a.u.
   * Measure for NSB level
   * TODO: how is this defined? at least leave a comment if it doesn't have
     a clear definition and can only be used in one chain.
* ``RELHUM`` type: float
   * Relative humidity
   * TODO: link to definition ... wikipedia?


Notes
-----

EVENT_ID column
~~~~~~~~~~~~~~~

This paragraph contains some explanatory notes concerning the requirements
and recommendations on ``EVENT_ID``.

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
at low data levels and is already fixed for existing IACTs, we propose here
to have an ``EVENT_ID`` that is simpler and works the same for all IACTs at
the DL3 level.

As an example: for H.E.S.S. we achive this by using an INT64 for ``EVENT_ID``
and to store ``EVENT_ID = (BUNCH_ID_HESS << 32) || (EVENT_ID_HESS)``, i.e.
use the upper bits to contain the low-level bunch ID and the lower bits
to contains the low-level event ID.
This encoding is unique and reversible, i.e. it's easy to go back to
``BUNCH_ID_HESS`` and ``EVENT_ID_HESS`` for a given ``EVENT_ID``,
and to low-level checks (e.g. look at the shower images for a given event
that behaves strangely in reconstructed high-level parameters).
