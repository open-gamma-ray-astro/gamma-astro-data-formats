.. include:: ../references.txt

.. _sky-coordinates:

Sky coordinates
===============

This section describes the sky coordinates in use by science tools.
It is referenced from the description of data formats to explain the
exact meaning of the coordinates stored.

We don't have a separate section for world coordinate systems (WCS),
pixel coordinates, projections, that is covered here as well
(see `here <http://fits.gsfc.nasa.gov/fits_wcs.html>`__ and
`here <http://www.atnf.csiro.au/people/mcalabre/WCS/>`__ for references).

We only discuss 2-dimensional sky and image coordinates here,
other coordinates like e.g. time or an energy axis aren't covered here.

Some conventions are adopted from `astropy.coordinates <http://astropy.readthedocs.org/en/latest/coordinates/index.html>`__,
which is a Python wrapper of the `IAU SOFA <http://www.iausofa.org/>`__ C time and coordinate library,
which can be considered the gold standard when it comes to coordinates.
In some cases code examples are given using `astropy.coordinates` to obtain a reference value that
can be used to check a given software package (in case it's not based on `astropy.coordinates`).

.. _sky-coordinates-radec:

RA / DEC
--------

The most common way to give sky coordinates is as right ascension (RA) and declination (DEC)
in the `equatorial coordinate system <https://en.wikipedia.org/wiki/Equatorial_coordinate_system>`__.

Actually there are several equatorial coordinate systems in use, the most common ones being FK4, FK5 and ICRS.
If you're interested to learn more about these and other astronomical coordinate systems, the references
`here <http://astropy.readthedocs.org/en/latest/coordinates/index.html#see-also>`__ are a good starting point.

But in practice it's pretty simple: when someone gives or talks about RA / DEC coordinates, they mean either
ICRS or FK5 J2000 coordinates. The difference between those two is at the sub-arcsecond level for the whole sky,
i.e. irrelevant for gamma-ray astronomy.

We recommend you by default assume RA / DEC is in the ICRS frame, which is the default in Astropy
`SkyCoord <http://astropy.readthedocs.org/en/latest/api/astropy.coordinates.SkyCoord.html>`__
and also the current standard celestial reference system adopted by the IAU
(see `here <https://en.wikipedia.org/wiki/International_Celestial_Reference_System>`__).

.. _sky-coordinates-galactic:

Galactic
--------

The `Galactic coordinate system <https://en.wikipedia.org/wiki/Galactic_coordinate_system>`__ is
often used by Galactic astronomers.

Unfortunately there are slightly different variants in use (usually with differences at the arcsecond level),
and there are no standard names for these slightly different Galactic coordinate frames.
See `here <https://github.com/astropy/astropy/issues/3344>`__ for an open discussion which Galactic coordinates
to support and what to call them in Astropy.

We recommend you use ICRS RA / DEC for precision coordinate computations. If you do use Galactic coordinates,
we recommend you compute them like Astropy does (which I think is the most frame in use in the literature
and in existing astronomy software).

Both ICRS and Galactic coordinates don't need the specification of an
`epoch <https://en.wikipedia.org/wiki/Epoch_(astronomy)>`__
or `equinox <https://en.wikipedia.org/wiki/Equinox_(celestial_coordinates)>`__

To check your software, you can use the `(l, b) = (0, 0)` position:

.. code-block:: python

    >>> from astropy.coordinates import SkyCoord
    >>> SkyCoord(0, 0, unit='deg', frame='galactic')
    <SkyCoord (Galactic): (l, b) in deg (0.0, 0.0)>
    >>> SkyCoord(0, 0, unit='deg', frame='galactic').icrs
    <SkyCoord (ICRS): (ra, dec) in deg (266.40498829, -28.93617776)>

.. _sky-coordinates-altaz:

Alt / Az
--------

The `horizontal coordinate system <https://en.wikipedia.org/wiki/Horizontal_coordinate_system>`__ is the
one connected to an observer at a given location on earth and point in time.

* Azimuth is oriented east of north (i.e. north is at 0 deg, east at 90 deg, south at 180 deg and west at 270 deg).
  This is the convention used by Astropy (see `here <http://astropy.readthedocs.org/en/latest/api/astropy.coordinates.AltAz.html>`__)
  and quoted as the most common convention in astronomy on Wikipedia (see `here <https://en.wikipedia.org/wiki/Horizontal_coordinate_system>`__)
* The zenith angle is defined as the angular separation from the `zenith <https://en.wikipedia.org/wiki/Zenith>`__,
  which is the direction defined by the line connecting the Earth's center and the observer.
  Altitude and elevation are the same thing, and are defined as 90 degree minus the zenith angle.
  The reason to define altitude like this instead of the angle above the horizon is that usually Earth models
  aren't perfect spheres, but ellipsoids, so the zenith angle as defined here isn't perfectly perpendicular
  with the horizon plane.
* Unless explicitly specified, Alt / Az should be assumed to not include any refraction corrections,
  i.e. be valid assuming no refraction. Usually this can be achived in coordinate codes by setting
  the atmospheric pressure to zero, i.e. turning the atmosphere off.

Here's some Astropy coordinates code that shows how to convert back and forth between ICRS and AltAz coordinates
(the default pressure is set to zero in Astropy, i.e. this is without refraction corrections):


.. code-block:: python

    import astropy.units as u
    from astropy.time import Time
    from astropy.coordinates import Angle, SkyCoord, EarthLocation, AltAz

    # Take any ICRS sky coordinate
    icrs = SkyCoord.from_name('crab')
    print('RA = {pos.ra.deg:10.5f}, DEC = {pos.dec.deg:10.5f}'.format(pos=icrs))
    # RA =   83.63308, DEC =   22.01450

    # Convert to AltAz for some random observation time and location
    # This assumes pressure is zero, i.e. no refraction
    time = Time('2010-04-26', scale='tt')
    location = EarthLocation(lon=42 * u.deg, lat=42 * u.deg, height=42 * u.meter)
    altaz_frame = AltAz(obstime=time, location=location)
    altaz = icrs.transform_to(altaz_frame)
    print('AZ = {pos.az.deg:10.5f}, ALT = {pos.alt.deg:10.5f}'.format(pos=altaz))
    # AZ =  351.88232, ALT =  -25.56281

    # Convert back to ICRS to make sure round-tripping is OK
    icrs2 = altaz.transform_to('icrs')
    print('RA = {pos.ra.deg:10.5f}, DEC = {pos.dec.deg:10.5f}'.format(pos=icrs2))
    # RA =   83.63308, DEC =   22.01450


.. _sky-coordinates-fov:

Field of view
-------------

Field of view coordinates for a given observation have the pointing position at `(0, 0)`.

At the moment they are only used for background modeling, where off runs are stacked
in the field of view coordinate system.
We are also discussing if we should use them for IRFs like effective area, where for
large field of views a gradient due to varying zenith angle can be present and we'd
like to store this dependency / use it in exposure computations.

In detail the definition of field of view coordinates is tricky and still under discussion.

The main questions are:

* How exactly are the field of view coordinates defined?
* Is a projection (e.g. the FITS TAN aka gnomonic projection) involved or are they spherical coordinates?
  I.e. are they angles or lengths?
* Are the field of view coordinate axes aligned with RA / DEC or ALT / AZ?
  (we probably need or at least want both for different applications / investigations, i.e. there are two field of view coordinates.)
* How should this be stored in FITS (e.g. axis info or even WCS object in background cube models)

Here's some useful links about the TAN projection:

* https://en.wikipedia.org/wiki/Gnomonic_projection
* http://mathworld.wolfram.com/GnomonicProjection.html
* http://bl.ocks.org/mbostock/3795048
* http://adsabs.harvard.edu/abs/2002A%26A...395.1077C

TODO: document what exactly is filled / assumed at the moment in the HESS exporters, Gammalib and Gammapy.
