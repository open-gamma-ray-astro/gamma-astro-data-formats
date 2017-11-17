"""Generate an example background rate file.
"""

from astropy.io import fits
from astropy.table import Table
import numpy as np

e_bins = 20
o_bins = 5
e_axis = np.logspace(-1,2,e_bins+1)
o_axis = np.linspace(0,3,o_bins+1)
rad_max = (np.ones([e_bins, o_bins]).T * np.linspace(0.1, 0.01, e_bins)).T

table = Table([[e_axis[:-1]],[e_axis[1:]],
               [o_axis[:-1]],[o_axis[1:]],
               [rad_max]],
              names=('ENERG_LO', 'ENERG_HI',
                     'THETA_LO', 'THETA_HI',
                     'RAD_MAX'))

data = table.as_array()
header = fits.Header()
header['HDUDOC'] = 'https://github.com/open-gamma-ray-astro/gamma-astro-data-formats', ''
header['HDUVERS'] = '0.2', ''
header['HDUCLASS'] = 'GADF', ''
header['HDUCLAS1'] = 'RESPONSE', ''
header['HDUCLAS2'] = 'RAD_MAX', ''
header['HDUCLAS3'] = 'POINT-LIKE', ''
header['HDUCLAS4'] = 'RAD_MAX_2D', ''


tbhdu = fits.BinTableHDU(data, header, name='RAD_MAX')

prihdu = fits.PrimaryHDU()

thdulist = fits.HDUList([prihdu, tbhdu])
filename = 'rad_max_2d_point-like_example.fits'
print('Writing {}'.format(filename))
thdulist.writeto(filename, clobber=True)
