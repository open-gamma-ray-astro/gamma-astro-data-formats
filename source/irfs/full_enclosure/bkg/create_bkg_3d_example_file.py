"""Generate an example background rate file.
"""

from astropy.io import fits
from astropy.table import Table
import numpy as np

e_bins = 20
x_bins = 15
y_bins = 15
e_axis = np.logspace(-1,2,e_bins+1)
x_axis = np.linspace(-3,3,x_bins+1)
y_axis = np.linspace(-3,3,y_bins+1)
bkg = np.ones([e_bins, x_bins, y_bins]) * 100

table = Table([[e_axis[:-1]],[e_axis[1:]],
               [x_axis[:-1]],[x_axis[1:]],
               [y_axis[:-1]],[y_axis[1:]],
               [bkg]],
              names=('ENERG_LO', 'ENERG_HI',
                     'DETX_LO', 'DETX_HI',
                     'DETY_LO', 'DETY_HI',
                     'BKG'))

data = table.as_array()
header = fits.Header()
header['OBS_ID'] = 31415 , 'Observation ID'
header['LO_THRES'] = 0.1 , 'Low energy threshold [TeV]'
header['HI_THRES'] = 50 , 'High energy threshold [TeV]'
header['HDUDOC'] = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats', ''
header['HDUVERS'] = '0.3', ''
header['HDUCLASS'] = 'GADF', ''
header['HDUCLAS1'] = 'RESPONSE', ''
header['HDUCLAS2'] = 'BKG', ''
header['HDUCLAS3'] = 'FULL-ENCLOSURE', ''
header['HDUCLAS4'] = 'BKG_3D', ''


tbhdu = fits.BinTableHDU(data, header, name='BACKGROUND')

prihdu = fits.PrimaryHDU()

thdulist = fits.HDUList([prihdu, tbhdu])
filename = 'bkg_3d_full_example.fits'
print('Writing {}'.format(filename))
thdulist.writeto(filename, clobber=True)
