"""Generate an example 3D effective area file.
"""
from astropy.io import fits
import astropy.units as u
from astropy.table import Table
import numpy as np

e_bins = 20
x_bins = 15
y_bins = 15
e_axis = np.logspace(-1, 2, e_bins + 1) * u.TeV
x_axis = np.linspace(-3, 3, x_bins + 1) * u.deg
y_axis = np.linspace(-3, 3, y_bins + 1) * u.deg
effarea = np.full([e_bins, x_bins, y_bins], 3e5) * u.m**2

table = Table({
    'ENERG_LO': e_axis[np.newaxis, :-1],
    'ENERG_HI': e_axis[np.newaxis, 1:],
    'DETX_LO': x_axis[np.newaxis, :-1],
    'DETX_HI': x_axis[np.newaxis, 1:],
    'DETY_LO': y_axis[np.newaxis, :-1],
    'DETY_HI': y_axis[np.newaxis, 1:],
    'EFFAREA': effarea[np.newaxis, :, :, :],
})

header = fits.Header()
header['OBS_ID'] = 31415, 'Observation ID'
header['LO_THRES'] = 0.1, 'Low energy threshold [TeV]'
header['HI_THRES'] = 50, 'High energy threshold [TeV]'
header['HDUDOC'] = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats', ''
header['HDUVERS'] = '0.4', ''
header['HDUCLASS'] = 'GADF', ''
header['HDUCLAS1'] = 'RESPONSE', ''
header['HDUCLAS2'] = 'EFF_AREA', ''
header['HDUCLAS3'] = 'FULL-ENCLOSURE', ''
header['HDUCLAS4'] = 'AEFF_3D', ''
header['FOVALIGN'] = 'ALTAZ', ''


aeff_hdu = fits.BinTableHDU(table, header, name='EFFECTIVE AREA')

primary_hdu = fits.PrimaryHDU()
hdulist = fits.HDUList([primary_hdu, aeff_hdu])

filename = 'aeff_3d_full_example.fits'
print('Writing {}'.format(filename))

hdulist.writeto(filename, overwrite=True)