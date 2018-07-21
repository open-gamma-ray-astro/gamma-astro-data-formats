#! /usr/bin/env python
# ==========================================================================
# Create a DL3 template event file
#
# Copyright (C) 2016 Juergen Knoedlseder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ==========================================================================
import math
import gammalib


# ======================= #
# Write HDUCLASS keywords #
# ======================= #
def write_hduclass_keywords(hdu, hduclas1, hduclas2, version='0.1.0'):
    """
    Write HDUCLASS keywords

    Parameters
    ----------
    hdu : `~gammalib.GFitsHDU`
        Header Data Unit
    hduclas1 : str
        Primary extension class
    hduclas2 : str
        Secondary extension class
    """
    # Write keywords
    hdu.card('HDUCLASS', 'OGIP', 'Format conforms to OGIP standard')
    hdu.card('HDUDOC',   'http://gamma-astro-data-formats.readthedocs.org',
             'Document defining the format')
    hdu.card('HDUVERS',  version, 'Version of format')
    hdu.card('HDUCLAS1', hduclas1, 'Primary extension class')
    hdu.card('HDUCLAS2', hduclas2, 'Secondary extension class')

    # Return
    return


# ============================== #
# Write OGIP provenance keywords #
# ============================== #
def write_provenance_keywords(hdu):
    """
    Write OGIP provenance keywords

    Parameters
    ----------
    hdu : `~gammalib.GFitsHDU`
        Header Data Unit
    """
    # Write keywords
    hdu.card('ORIGIN',   'DL3 WG',            'Organisation that created the file')
    hdu.card('CREATOR',  'create_event_file', 'Program which created the file')
    hdu.card('TELESCOP', 'CTA',               'Name of IACT')
    hdu.card('INSTRUME', 'NORTH',             'Name of (sub-)array')

    # Return
    return


# ======================== #
# Write OGIP time keywords #
# ======================== #
def write_time_keywords(hdu, tstart, tstop):
    """
    Write OGIP time keywords

    Parameters
    ----------
    hdu : `~gammalib.GFitsHDU`
        Header Data Unit
    tstart : float
        Start time of time interval (sec)
    tstop : float
        Stop time of time interval (sec)
    """
    # Get UTC time strings
    utc_obs =  gammalib.GTime(tstart, 's').utc();
    utc_end  = gammalib.GTime(tstop,  's').utc();
    date_obs = utc_obs[0:10]
    time_obs = utc_obs[11:19]
    date_end = utc_end[0:10]
    time_end = utc_end[11:19]

    # Write keywords
    hdu.card('DATE-OBS', date_obs,          'Observation start date (UTC)')
    hdu.card('TIME-OBS', time_obs,          'Observation start time (UTC)')
    hdu.card('DATE-END', date_end,          'Observation end date (UTC)')
    hdu.card('TIME-END', time_end,          'Observation end time (UTC)')
    hdu.card('TSTART',   tstart,            '[s] Time of start of observation')
    hdu.card('TSTOP',    tstop,             '[s] Time of end of observation')
    hdu.card('MJDREFI',  55197,             '[days] Integer part of time reference MJD')
    hdu.card('MJDREFF',  0.000766018518519, '[days] Fractional part of time reference MJD')
    hdu.card('TIMEUNIT', 's',               'Time unit')
    hdu.card('TIMESYS',  'TT',              'Time system')
    hdu.card('TIMEREF',  'LOCAL',           'Time reference')

    # Return
    return


# ==================================== #
# Write OGIP observation time keywords #
# ==================================== #
def write_obstime_keywords(hdu, tstart, tstop, ontime, deadc=0.95):
    """
    Write OGIP observation time keywords

    Parameters
    ----------
    hdu : `~gammalib.GFitsHDU`
        Header Data Unit
    tstart : float
        Start time of time interval (sec)
    tstop : float
        Stop time of time interval (sec)
    ontime : float
        Total good time (sec)
    deadc : float, optional
        Deadtime correction
    """
    # Compute elapsed time and livetime
    telapse  = tstop - tstart
    livetime = ontime * deadc

    # Write keywords
    hdu.card('TELAPSE',  telapse,  '[s] Elapsed time')
    hdu.card('ONTIME',   ontime,   '[s] Total good time')
    hdu.card('LIVETIME', livetime, '[s] Total livetime on target')
    hdu.card('DEADC',    deadc,    'Deadtime correction')

    # Return
    return


# ==================================== #
# Write OGIP celestial system keywords #
# ==================================== #
def write_celsys_keywords(hdu):
    """
    Write OGIP celestial system keywords

    Parameters
    ----------
    hdu : `~gammalib.GFitsHDU`
        Header Data Unit
    """
    # Write keywords
    hdu.card('EQUINOX',  2000.0, '[years] Equinox for celestial coordinate system')
    hdu.card('RADECSYS', 'ICRS', 'Reference frame for celestial coordinate system')

    # Return
    return


# ================= #
# Create events HDU #
# ================= #
def create_events_hdu(tstart, tstop):
    """
    Create EVENTS HDU

    Parameters
    ----------
    tstart : float
        Start time of time interval (sec)
    tstop : float
        Stop time of time interval (sec)

    Returns
    -------
    hdu : `~gammalib.GFitsBinTable`
        Pointing binary table
    """
    # Define number of rows
    nrows = 147

    # Create binary table
    hdu = gammalib.GFitsBinTable(nrows)

    # Set extension name
    hdu.extname("EVENTS")

    # Write HDU keywords
    write_hduclass_keywords(hdu, 'EVENTS', 'ACCEPTED')
    write_provenance_keywords(hdu)
    write_time_keywords(hdu, 0.0, 1800.0)
    write_celsys_keywords(hdu)
    write_obstime_keywords(hdu, 0.0, 1800.0, 1700.0)

    # Write events specific keywords
    hdu.card('OBSERVER', 'Joe Public', 'PI of observation')
    hdu.card('OBJECT',   'Crab',       'Observed target')
    hdu.card('OBS_MODE', 'WOBBLE',     'Observation mode')
    hdu.card('OBS_ID',   1,            'Observation identifier')
    hdu.card('EVTCLASS', 'STD',        'Event class')

    # Create columns
    col_eid    = gammalib.GFitsTableULongCol('EVENT_ID', nrows)
    col_time   = gammalib.GFitsTableDoubleCol('TIME',    nrows)
    col_ra     = gammalib.GFitsTableFloatCol('RA',       nrows)
    col_dec    = gammalib.GFitsTableFloatCol('DEC',      nrows)
    col_energy = gammalib.GFitsTableFloatCol('ENERGY',   nrows)
    col_detx   = gammalib.GFitsTableFloatCol('DETX',     nrows)
    col_dety   = gammalib.GFitsTableFloatCol('DETY',     nrows)

    # Set units
    col_time.unit('s')
    col_ra.unit('deg')
    col_dec.unit('deg')
    col_energy.unit('TeV')
    col_detx.unit('deg')
    col_dety.unit('deg')

    # Get random number generator
    ran = gammalib.GRan()

    # Precompute some stuff
    telapse       = tstop - tstart
    cosrad        = math.cos(3.0 * gammalib.deg2rad)
    mc_emin       =   0.1
    mc_emax       = 300.0
    mc_exponent   = -2.5 + 1.0
    mc_pow_emin   = math.pow(mc_emin, mc_exponent)
    mc_pow_ewidth = math.pow(mc_emax, mc_exponent) - mc_pow_emin

    # Fill columns
    for i in range(nrows):

        # Generate random sky position
        skydir  = gammalib.GSkyDir()
        instdir = gammalib.GSkyDir()
        skydir.radec_deg(83.6331, 22.0145)
        instdir.radec_deg(0.0, 0.0)
        phi   = 360.0 * ran.uniform()
        theta =  math.acos(1.0 - ran.uniform() * (1.0 - cosrad)) * gammalib.rad2deg
        skydir.rotate_deg(phi, theta)
        instdir.rotate_deg(phi, theta)

        # Generate random energy
        energy = math.exp(math.log(ran.uniform() * mc_pow_ewidth + mc_pow_emin) /
                          mc_exponent)


        # Set columns
        col_eid[i]    = i
        col_time[i]   = tstart + telapse * ran.uniform()
        col_ra[i]     = skydir.ra_deg()
        col_dec[i]    = skydir.dec_deg()
        col_energy[i] = energy
        col_detx[i]   = instdir.ra_deg()
        col_dety[i]   = instdir.dec_deg()

    # Append columns to binary table
    hdu.append(col_eid)
    hdu.append(col_time)
    hdu.append(col_ra)
    hdu.append(col_dec)
    hdu.append(col_energy)
    hdu.append(col_detx)
    hdu.append(col_dety)

    # Return HDU
    return hdu


# ============== #
# Create GTI HDU #
# ============== #
def create_gti_hdu(tstart, tstop):
    """
    Create GTI HDU

    Parameters
    ----------
    tstart : float
        Start time of time interval (sec)
    tstop : float
        Stop time of time interval (sec)

    Returns
    -------
    hdu : `~gammalib.GFitsBinTable`
        Pointing binary table
    """
    # Define number of rows
    nrows = 2

    # Create binary table
    hdu = gammalib.GFitsBinTable(nrows)

    # Set extension name
    hdu.extname("GTI")

    # Write HDU keywords
    write_hduclass_keywords(hdu, 'GTI', 'STANDARD')
    write_provenance_keywords(hdu)
    write_time_keywords(hdu, 0.0, 1800.0)

    # Create columns
    col_start = gammalib.GFitsTableDoubleCol('START', nrows)
    col_stop  = gammalib.GFitsTableDoubleCol('STOP',  nrows)

    # Set units
    col_start.unit('s')
    col_stop.unit('s')

    # Fill columns
    col_start[0] = tstart + 10.0
    col_stop[0]  = col_start[0] + 1000.0
    col_start[1] = col_stop[0] + 30.0
    col_stop[1]  = col_start[1] + 700.0
 
    # Append columns to binary table
    hdu.append(col_start)
    hdu.append(col_stop)

    # Return HDU
    return hdu


# =================== #
# Create pointing HDU #
# =================== #
def create_pointing_hdu(tstart, tstop):
    """
    Create POINTING HDU

    Parameters
    ----------
    tstart : float
        Start time of time interval (sec)
    tstop : float
        Stop time of time interval (sec)

    Returns
    -------
    hdu : `~gammalib.GFitsBinTable`
        Pointing binary table
    """
    # Define number of rows
    trow  = 60.0
    nrows = int((tstop - tstart)/trow)+1

    # Create binary table
    hdu = gammalib.GFitsBinTable(nrows)

    # Set extension name
    hdu.extname("POINTING")

    # Write HDU keywords
    write_hduclass_keywords(hdu, 'TEMPORALDATA', 'ASPECT')
    write_provenance_keywords(hdu)
    write_time_keywords(hdu, tstart, tstop)
    write_celsys_keywords(hdu)
    hdu.card('GEOLON', -23.27, '[deg] Geographic longitude of IACT centre')
    hdu.card('GEOLAT', -16.50, '[deg] Geographic latitude of IACT centre')
    hdu.card('GEOALT', 1835.0, '[m] Altitude of IACT centre above sea level')

    # Create columns
    col_time    = gammalib.GFitsTableDoubleCol('TIME',   nrows)
    col_ra_pnt  = gammalib.GFitsTableFloatCol('RA_PNT',  nrows)
    col_dec_pnt = gammalib.GFitsTableFloatCol('DEC_PNT', nrows)
    col_alt_pnt = gammalib.GFitsTableFloatCol('ALT_PNT', nrows)
    col_az_pnt  = gammalib.GFitsTableFloatCol('AZ_PNT',  nrows)

    # Set units
    col_time.unit('s')
    col_ra_pnt.unit('deg')
    col_dec_pnt.unit('deg')
    col_alt_pnt.unit('deg')
    col_az_pnt.unit('deg')

    # Fill columns
    for i in range(nrows):
        col_time[i]    = tstart + i*trow
        col_ra_pnt[i]  = 83.6331
        col_dec_pnt[i] = 22.0145
        skydir = gammalib.GSkyDir()
        skydir.radec_deg(col_ra_pnt[i], col_dec_pnt[i])
        skydir.rotate_deg(45.0, 30.0+(15.0/3600.0*i*trow))
        col_alt_pnt[i] = skydir.ra_deg()
        col_az_pnt[i]  = skydir.dec_deg()

    # Append columns to binary table
    hdu.append(col_time)
    hdu.append(col_ra_pnt)
    hdu.append(col_dec_pnt)
    hdu.append(col_alt_pnt)
    hdu.append(col_az_pnt)

    # Return HDU
    return hdu


# ================= #
# Create event file #
# ================= #
def create_event_file(filename):
    """
    Create template event file

    Parameters
    ----------
    filename : str
        Name of event FITS file
    """
    # Create a FITS file
    fits = gammalib.GFits()

    # Append EVENTS HDU
    fits.append(create_events_hdu(0.0, 1800.0))

    # Append GTI HDU
    fits.append(create_gti_hdu(0.0, 1800.0))

    # Append POINTING HDU
    fits.append(create_pointing_hdu(0.0, 1800.0))

    # Save FITS file
    fits.saveto(filename, True)

    # Return
    return


# ======================== #
# Main routine entry point #
# ======================== #
if __name__ == '__main__':

    # Dump header
    print('***************************************')
    print('* Create IACT DL3 event file template *')
    print('***************************************')

    # Create the file
    create_event_file('events.fits')

    # We are done
    print('... done.')
