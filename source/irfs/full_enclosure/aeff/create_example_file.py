"""Generate an example effective area file.
"""
from astropy.io import fits
import astropy.units as u
from astropy.table import Table
import numpy as np

e_bins = 20
o_bins = 5
e_axis = np.logspace(-1, 2, e_bins + 1) * u.TeV
o_axis = np.linspace(0, 3, o_bins + 1) * u.deg
effarea = np.full([e_bins, o_bins], 3e5) * u.m**2

# we have to add one dimension, so we only have one row in the binary table
# and each column is an array of the correct dimension
table = Table({
    'ENERG_LO': e_axis[np.newaxis, :-1],
    'ENERG_HI': e_axis[np.newaxis, 1:],
    'THETA_LO': o_axis[np.newaxis, :-1],
    'THETA_HI': o_axis[np.newaxis, 1:],
    'EFFAREA': effarea[np.newaxis, :, :],
})

header = fits.Header()
header['OBS_ID'] = 31415, 'Observation ID'
header['LO_THRES'] = 0.1, 'Low energy threshold [TeV]'
header['HI_THRES'] = 50, 'High energy threshold [TeV]'
header['HDUDOC'] = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats', ''
header['HDUVERS'] = '0.2', ''
header['HDUCLASS'] = 'GADF', ''
header['HDUCLAS1'] = 'RESPONSE', ''
header['HDUCLAS2'] = 'EFF_AREA', ''
header['HDUCLAS3'] = 'FULL-ENCLOSURE', ''
header['HDUCLAS4'] = 'AEFF_2D', ''


aeff_hdu = fits.BinTableHDU(table, header, name='EFFECTIVE AREA')

primary_hdu = fits.PrimaryHDU()
hdulist = fits.HDUList([primary_hdu, aeff_hdu])

filename = 'aeff_2d_full_example.fits'
print('Writing {}'.format(filename))

hdulist.writeto(filename, overwrite=True)
