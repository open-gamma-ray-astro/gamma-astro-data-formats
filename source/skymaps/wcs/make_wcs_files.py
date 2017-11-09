import numpy as np
import healpy as hp
from astropy.table import Column, Table
from astropy.io import fits
from astropy.wcs import WCS


def create_bands_table(emin, emax, npix=None, cdelt=None, crpix=None):

    cols = [Column(name='CHANNEL', data=np.arange(len(emin)), dtype='i8'),            
            Column(name='E_MIN', data=emin, dtype='f8', unit='keV'),
            Column(name='E_MAX', data=emax, dtype='f8', unit='keV')]
    if npix is not None:
        cols += [Column(name='NPIX', data=npix, dtype='i8'),
                 Column(name='CDELT', data=cdelt, dtype='f8'),
                 Column(name='CRPIX', data=crpix, dtype='f8'),]
            
    return Table(cols,meta={'EXTNAME' : 'BANDS', 'AXCOLS1' : 'E_MIN,E_MAX'})

def create_ebounds_table(emin, emax):

    cols = [Column(name='CHANNEL', data=np.arange(len(emin)), dtype='i8'),
            Column(name='E_MIN', data=emin, dtype='f8', unit='keV'),
            Column(name='E_MAX', data=emax, dtype='f8', unit='keV')]
    return Table(cols,meta={'EXTNAME' : 'EBOUNDS'})

def update_header(header, **kwargs):
    for k,v in kwargs.items():
        header[k.upper()] = v


np.random.seed(0)
        
lon = 260.05167
lat = 57.91528
npix = 10
cdelt = 0.1
nband = 4

hdr = dict(BANDSHDU = 'BANDS',)

data = np.random.poisson(1.0,(nband, npix, npix)).astype('float')
egy = 1E3*10**np.linspace(3.0,4.0,5)
emin = egy[:-1]
emax = egy[1:]

# Create EBOUNDS Table
tab_ebounds = create_ebounds_table(emin, emax)

# Create EBOUNDS Map Table
tab_ebounds_cmap = create_ebounds_table(emin[:1], emax[-1:])

wcs = WCS(naxis=2)
wcs.wcs.ctype[0] = 'RA---CAR'
wcs.wcs.ctype[1] = 'DEC--CAR'
wcs.wcs.crval[0] = lon
wcs.wcs.crval[1] = lat
wcs.wcs.crpix[0] = (npix+1)/2.
wcs.wcs.crpix[1] = (npix+1)/2.
wcs.wcs.cdelt[0] = -1.0*cdelt
wcs.wcs.cdelt[1] = cdelt

#################################
# WCS Cube Regular

hdu = fits.PrimaryHDU(data, header=wcs.to_header())

tab_bands = create_bands_table(emin, emax)
hdulist = [hdu, fits.table_to_hdu(tab_bands)]
update_header(hdulist[1].header, **{})
fits.HDUList(hdulist).writeto('wcs_ccube.fits', overwrite=True)

#################################
# WCS Cube Irregular

# Set data values outside the geometry to NaN
data_irreg = np.full((nband, 8, 8), np.nan)
for i, n in enumerate([2,4,6,8]):
    data_irreg[i, :n, :n] = np.random.poisson(1.0,(n, n)).astype('float')


hdu = fits.PrimaryHDU(data_irreg, header=wcs.to_header())

npix_irreg = np.vstack((np.arange(2,10,2),np.arange(2,10,2))).T
cdelt_irreg = cdelt*np.vstack((np.linspace(4.,1.,4),np.linspace(4.,1.,4))).T
crpix_irreg = (npix_irreg+1)/2.

tab_bands = create_bands_table(emin, emax, npix_irreg, cdelt_irreg, crpix_irreg)
hdulist = [hdu, fits.table_to_hdu(tab_bands)]
update_header(hdulist[1].header, **{})
fits.HDUList(hdulist).writeto('wcs_ccube_irregular.fits', overwrite=True)

#################################
# WCS Cube Sparse

from gammapy.maps import WcsMapND, WcsGeom

geom = WcsGeom.create(npix=npix, axes=[egy])
m = WcsMapND(geom, data)
m.write('test_sparse.fits',sparse=True)


data_flat = np.ravel(data).reshape(data.shape[:-2] + (data.shape[-1] * data.shape[-2],))
nonzero = np.where(data_flat > 0)
channel = np.ravel_multi_index(nonzero[:-1], data.shape[:-2])
cols = [Column(name='PIX', data=nonzero[1], dtype='i4'),
        Column(name='CHANNEL', data=nonzero[0], dtype='i2'),
        Column(name='VALUE', data=data_flat[nonzero], dtype='f8')]

tab_sparse = Table(cols, meta={'EXTNAME' : 'SKYMAP'})

# Write File
tab_bands = create_bands_table(emin, emax)
hdulist = [fits.PrimaryHDU(), fits.table_to_hdu(tab_sparse),
           fits.table_to_hdu(tab_bands)]

update_header(hdulist[1].header, **wcs.to_header())
hdr_sparse = hdr.copy()
hdr_sparse['WCSSHAPE'] = '(10,10,4)'
update_header(hdulist[1].header, **hdr_sparse)
fits.HDUList(hdulist).writeto('wcs_ccube_sparse.fits', overwrite=True)

