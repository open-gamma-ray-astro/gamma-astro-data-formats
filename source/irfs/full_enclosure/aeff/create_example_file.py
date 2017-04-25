"""Generate an example effective area file.
"""

from astropy.io import fits
from astropy.table import Table
import numpy as np

e_bins = 20
o_bins = 5
e_axis = np.logspace(-1,2,e_bins+1)
o_axis = np.linspace(0,3,o_bins+1)
effarea = np.ones([e_bins, o_bins]) * 3e5

table = Table([[e_axis[:-1]],[e_axis[1:]],
               [o_axis[:-1]],[o_axis[1:]],
               [effarea]],
              names=('ENERG_LO', 'ENERG_HI',
                     'THETA_LO', 'THETA_HI',
                     'EFFAREA'))

data = table.as_array()
header = fits.Header()
header['OBS_ID'] = 31415 , 'Observation ID'
header['LO_THRES'] = 0.1 , 'Low energy threshold [TeV]'
header['HI_THRES'] = 50 , 'High energy threshold [TeV]'
header['HDUDOC'] = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats', ''
header['HDUVERS'] = '0.2', ''
header['HDUCLASS'] = 'GADF', ''
header['HDUCLAS1'] = 'RESPONSE', ''
header['HDUCLAS2'] = 'EFF_AREA', ''
header['HDUCLAS3'] = 'FULL-ENCLOSURE', ''
header['HDUCLAS4'] = 'AEFF_2D', ''


tbhdu = fits.BinTableHDU(data, header, name='EFFECTIVE AREA')

for colname in table.colnames:
    tbhdu.columns[colname].unit = str(table[colname].unit)

table = Table([[e_axis[:-1]],[e_axis[1:]],
               [o_axis[:-1]],[o_axis[1:]],
               [effarea]],
              names=('ENERG_LO', 'ENERG_HI',
                     'THETA_LO', 'THETA_HI',
                     'EFFAREA'))
 
data = table.as_array()
header = fits.Header()
header['OBS_ID'] = 31415 , 'Observation ID'
header['LO_THRES'] = 0.1 , 'Low energy threshold [TeV]'
header['HI_THRES'] = 50 , 'High energy threshold [TeV]'
header['HDUDOC'] = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats', ''
header['HDUVERS'] = '0.2', ''
header['HDUCLASS'] = 'GADF', ''
header['HDUCLAS1'] = 'RESPONSE', ''
header['HDUCLAS2'] = 'EFF_AREA', ''
header['HDUCLAS3'] = 'FULL-ENCLOSURE', ''
header['HDUCLAS4'] = 'AEFF_2D_RECO', ''

tbrecohdu = fits.BinTableHDU(data, header, name='EFFECTIVE AREA (RECO)')

for colname in table.colnames:
    tbrecohdu.columns[colname].unit = str(table[colname].unit)

prihdu = fits.PrimaryHDU()

thdulist = fits.HDUList([prihdu, tbhdu, tbrecohdu])
filename = 'aeff_2d_full_example.fits'
print('Writing {}'.format(filename))
thdulist.writeto(filename, clobber=True)
