.. include:: ../references.txt

.. _coords:

Coordinates
===========

This section describes the sky coordinates in use by science tools. It is
referenced from the description of data formats to explain the exact meaning of
the coordinates stored.

We don't have a separate section for world coordinate systems (WCS), pixel
coordinates, projections, that is covered here as well (see `FITS WCS`_ and
`WCSLIB`_ for references).

We only discuss 2-dimensional sky and image coordinates here, other coordinates
like e.g. time or an energy axis aren't covered here.

Some conventions are adopted from `astropy.coordinates`_, which is a Python
wrapper of the `IAU SOFA`_ C time and coordinate library, which can be
considered the gold standard when it comes to coordinates. In some cases code
examples are given using `astropy.coordinates` to obtain a reference value that
can be used to check a given software package (in case it's not based on
`astropy.coordinates`).

.. _coords-radec:

RA / DEC
--------

The most common way to give sky coordinates is as right ascension (RA) and
declination (DEC) in the `equatorial coordinate system`_.

Actually there are several equatorial coordinate systems in use, the most common
ones being FK4, FK5 and ICRS. If you're interested to learn more about these and
other astronomical coordinate systems, the references in the `see also section
for astropy.coordinates`_ are a good starting point.

But in practice it's pretty simple: when someone gives or talks about RA / DEC
coordinates, they mean either ICRS or FK5 J2000 coordinates. The difference
between those two is at the sub-arcsecond level for the whole sky, i.e.
irrelevant for gamma-ray astronomy.

We recommend you by default assume RA / DEC is in the ICRS frame, which is the
default in `astropy.coordinates.SkyCoord`_ and also the current standard
celestial reference system adopted by the IAU (see `Wikipedia - ICRS`_).

.. _coords-galactic:

Galactic
--------

The `Galactic coordinate system`_ is often used by Galactic astronomers.

Unfortunately there are slightly different variants in use (usually with differences at the arcsecond level),
and there are no standard names for these slightly different Galactic coordinate frames.
See `here <https://github.com/astropy/astropy/issues/3344>`__ for an open discussion which Galactic coordinates
to support and what to call them in Astropy.

We recommend you use ICRS RA / DEC for precision coordinate computations. If you do use Galactic coordinates,
we recommend you compute them like Astropy does (which I think is the most frame in use in the literature
and in existing astronomy software).

Both ICRS and Galactic coordinates don't need the specification of an `epoch`_
or `equinox`_.

To check your software, you can use the ``(l, b) = (0, 0)`` position:

.. code-block:: python

    >>> from astropy.coordinates import SkyCoord
    >>> SkyCoord(0, 0, unit='deg', frame='galactic')
    <SkyCoord (Galactic): (l, b) in deg (0.0, 0.0)>
    >>> SkyCoord(0, 0, unit='deg', frame='galactic').icrs
    <SkyCoord (ICRS): (ra, dec) in deg (266.40498829, -28.93617776)>

.. _coords-altaz:

Alt / Az
--------

The `horizontal coordinate system`_ is the one connected to an observer at a
given location on earth and point in time.

* Azimuth is oriented east of north (i.e. north is at 0 deg, east at 90 deg,
  south at 180 deg and west at 270 deg). This is the convention used by
  `astropy.coordinates.AltAz`_ and quoted as the most common convention in
  astronomy on Wikipedia (see `horizontal coordinate system`_).
* The zenith angle is defined as the angular separation from the `zenith`_,
  which is the direction defined by the line connecting the Earth's center and the observer.
  Altitude and elevation are the same thing, and are defined as 90 degree minus the zenith angle.
  The reason to define altitude like this instead of the angle above the horizon is that usually Earth models
  aren't perfect spheres, but ellipsoids, so the zenith angle as defined here isn't perfectly perpendicular
  with the horizon plane.
* Unless explicitly specified, Alt / Az should be assumed to not include any refraction corrections,
  i.e. be valid assuming no refraction. Usually this can be achived in coordinate codes by setting
  the atmospheric pressure to zero, i.e. turning the atmosphere off.

Here's some Astropy coordinates code that shows how to convert back and forth
between ICRS and AltAz coordinates (the default pressure is set to zero in
Astropy, i.e. this is without refraction corrections):

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


.. _coords-fov:

Field of view
-------------

In Gamma-ray astronomy, sometimes field of view (FOV) coordinates are used.
Specifically some :ref:`background models <bkg>` are in the FOV coordinate system
and FOV coordinates can also be used for other IRFs.

The basic idea is to have a coordinate system that is centered on the array
pointing position. We define FOV coordinates here to be spherical coordinates,
there is no projection or WCS, only a spherical rotation.

Two versions of FOV coordinates are defined:

1. ``(LON, LAT)`` with the pointing position on the equator at ``(0, 0)``
     * ``LON`` range -180 deg to + 180 deg
     * ``LAT`` range -90 deg to + 90 deg
2. ``(THETA, PHI)`` with the pointing position at the pole ``THETA=0``
     * ``THETA`` range 0 deg to +180 deg
     * ``PHI`` range 0 deg to 360 deg
     * ``THETA`` is the angular separation wrt. the pointing position.
     * TODO: define PHI orientation
     * TODO: give example with numbers to make PHI orientation clear

Also, there are two versions of FOV coordinates defined:

1. Aligned with ``ALTAZ``
2. Aligned with ``RADEC``

To summarise, the following coordinates are defined:

===============  ==================================
Field            Description
===============  ==================================
FOV_ALTAZ_LON    Longitude in ALTAZ FOV system
FOV_ALTAZ_LAT    Latitude in ALTAZ FOV system
FOV_ALTAZ_THETA  Offset in ALTAZ FOV system
FOV_ALTAZ_PHI    Position angle in ALTAZ FOV system
---------------  ----------------------------------
FOV_RADEC_LON    Longitude in RADEC FOV system
FOV_RADEC_LAT    Latitude in RADEC FOV system
FOV_RADEC_THETA  Offset in RADEC FOV system
FOV_RADEC_PHI    Position angle in RADEC FOV system
===============  ==================================

.. _coords-location:

Earth location
--------------

When working with Alt-Az coordinates or very high-precision times,
an observatory Earth location is needed. However, note that high-level
analysis for most use cases does not need this information.

The FITS standard mentions ``OBSGEO-X``, ``OBSGEO-Y``, ``OBSGEO-Z``
header keys, and we might want to consider using those in the future.

For now, as of 2018, however, the existing IACT FITS data uses the
following header keys, so their use is encouraged:

* ``GEOLON`` type: float, unit: deg
    * Geographic longitude of array centre
* ``GEOLAT`` type: float, unit: deg
    * Geographic latitude of array centre
* ``ALTITUDE`` type: float, unit: m
    * Altitude of array center above sea level

While it is possible in principle to change this for each FITS file,
in practice the observatory or telescope array centre position is something
that is chosen once and then used consistently in the event reconstruction
and analysis. As an example, H.E.S.S. uses the following location and
FITS header keys::

  GEOLAT  = -23.2717777777778 / latitude of observatory (deg)
  GEOLON  =  16.5002222222222 / longitude of observatory (deg)
  ALTITUDE=             1835. / altitude of observatory (m)

