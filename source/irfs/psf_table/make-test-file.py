import numpy as np
from astropy.io import fits
from astropy.table import Table
fermi_hdus = fits.open('psf-fermi.fits')

table = Table()
table['Theta'] = np.atleast_2d(fermi_hdus['THETA'].data['Theta'])
table['Energy'] = np.atleast_2d(fermi_hdus['PSF'].data['Energy'])
table['Exposure'] = np.atleast_2d(fermi_hdus['PSF'].data['Exposure'])
table['Offset'] = np.atleast_2d(np.linspace(0, 2, 10))
shape = (table['Offset'].size, table['Theta'].size, table['Energy'].size)
# TODO: put a better example so that people can test their
# axis order / interpolation
# for now we just fill zeros.
# data = fermi_hdus['PSF'].data['Psf']
# print(data.shape)
# data = np.tile(data, table['Offset'].size)
# print(data.shape)
# print(shape)
# print(fermi_hdus['PSF'].data['Psf'].shape)
data = np.ones(shape)
print(data.shape)
data = np.expand_dims(data, 0)
print(data.shape)
# data = np.reshape(data, shape)
table['Psf'] = data

filename = 'psf-histo-offset-energy.fits.gz'
print('Writing {}'.format(filename))
table.write(filename, overwrite=True)
