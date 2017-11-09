import numpy as np
import healpy as hp
from astropy.table import Column, Table
from astropy.io import fits

def coords_to_vec(lon, lat):
    """ Converts longitute and latitude coordinates to a unit 3-vector

    return array(3,n) with v_x[i],v_y[i],v_z[i] = directional cosines
    """
    phi = np.radians(lon)
    theta = (np.pi / 2) - np.radians(lat)
    sin_t = np.sin(theta)
    cos_t = np.cos(theta)

    xVals = sin_t * np.cos(phi)
    yVals = sin_t * np.sin(phi)
    zVals = cos_t

    # Stack them into the output array
    out = np.vstack((xVals, yVals, zVals)).swapaxes(0, 1)
    return out

def create_bands_table(nside, npix, emin, emax):

    cols = [Column(name='CHANNEL', data=np.arange(len(nside)), dtype='i8'),
            Column(name='NSIDE', data=nside, dtype='i8'),
            Column(name='NPIX', data=npix, dtype='i8'),
            Column(name='E_MIN', data=emin, dtype='f8', unit='keV'),
            Column(name='E_MAX', data=emax, dtype='f8', unit='keV')]
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
rad = 20.0
v = coords_to_vec(lon,lat)

nband = 4
order0 = 5
nside0 = 2**order0

hdr = dict(HPX_REG = 'DISK(%f,%f,%f)'%(lon,lat,rad),
           COORDSYS = 'GAL',
           NSIDE = nside0,
           ORDER = order0,
           HPX_CONV = 'GADF',
           BANDSHDU = 'BANDS',
           PIXTYPE = 'HEALPIX',
           ORDERING = 'NESTED')

ipix0 = hp.query_disc(nside0, v[0], np.radians(rad), nest=True)
vals0 = np.random.poisson(0.1,(nband, 12*nside0**2))
emin = 1E3*10**np.linspace(3.0,4.0,5)[:-1]
emax = 1E3*10**np.linspace(3.0,4.0,5)[1:]

# Create EBOUNDS Table
tab_ebounds = create_ebounds_table(emin, emax)

# Create EBOUNDS Map Table
tab_ebounds_cmap = create_ebounds_table(emin[:1], emax[-1:])

#################################
# IMPLICIT Cube

# Create Table
order = 4
nside = 2**order
npix_imp = np.ones(4)*12*nside**2
cols = []
for i in range(4):
    cols += [Column(name='CHANNEL%i'%i, data=hp.ud_grade(vals0[i], nside_out=nside, power=-2.0), dtype='f8')]
tab_imp = Table(cols, meta={'EXTNAME' : 'SKYMAP'})
hdr_imp = hdr.copy()
hdr_imp['ORDER'] = order
hdr_imp['NSIDE'] = nside
hdr_imp['INDXSCHM'] = 'IMPLICIT'
hdr_imp['AXCOLS1'] = 'E_MIN,E_MAX'

# Write File
tab_bands_imp = create_bands_table(np.ones(4)*nside, npix_imp, emin, emax)
hdulist = [fits.PrimaryHDU(), fits.table_to_hdu(tab_imp),
           fits.table_to_hdu(tab_bands_imp)]
update_header(hdulist[1].header, **hdr_imp)
fits.HDUList(hdulist).writeto('hpx_ccube_implicit.fits', overwrite=True)

#################################
# EXPLICIT Cube

# Create Table
order = 4
nside = 2**order
ipix = hp.query_disc(nside, v[0], np.radians(rad), nest=True)
vals_exp = np.zeros((4,len(ipix)))
for i in range(nband):
    vals_exp[i] = hp.ud_grade(vals0[i], nside_out=nside, power=-2.0)[ipix]

npix_exp_ccube = np.ones(nband)*len(ipix)
cols = [Column(name='PIX', data=ipix, dtype='i8')]
for i in range(4):
    cols += [Column(name='CHANNEL%i'%i, data=vals_exp[i], dtype='f8')]
tab_exp_ccube = Table(cols, meta={'EXTNAME' : 'SKYMAP'})
hdr_exp = hdr.copy()
hdr_exp['ORDER'] = order
hdr_exp['NSIDE'] = nside
hdr_exp['INDXSCHM'] = 'EXPLICIT'
hdr_exp['AXCOLS1'] = 'E_MIN,E_MAX'

# Write File
tab_bands_exp_ccube = create_bands_table(np.ones(4)*nside, npix_exp_ccube, emin, emax)
hdulist = [fits.PrimaryHDU(), fits.table_to_hdu(tab_exp_ccube),
           fits.table_to_hdu(tab_bands_exp_ccube)]
update_header(hdulist[1].header, **hdr_exp)
fits.HDUList(hdulist).writeto('hpx_ccube_explicit.fits', overwrite=True)

#################################
# EXPLICIT Image

# Create Table
npix_exp_cmap = len(ipix)
cols = [Column(name='PIX', data=ipix, dtype='i8')]
cols += [Column(name='CHANNEL0', data=np.sum(vals_exp,axis=0), dtype='f8')]
tab_exp_cmap = Table(cols, meta={'EXTNAME' : 'SKYMAP'})

# Write File
tab_bands_exp_cmap = create_bands_table(np.array([nside]), npix_exp_ccube[:1], emin[:1], emax[-1:])
hdulist = [fits.PrimaryHDU(), fits.table_to_hdu(tab_exp_cmap),
           fits.table_to_hdu(tab_bands_exp_cmap)]
hdr['INDXSCHM'] = 'EXPLICIT'
update_header(hdulist[1].header, **hdr)
fits.HDUList(hdulist).writeto('hpx_cmap_explicit.fits', overwrite=True)

#################################
# SPARSE Cube (Fixed NSIDE)

# Create Table

order = 4
nside = 2**order
ipix = hp.query_disc(nside, v[0], np.radians(rad), nest=True)
ibnd = np.linspace(0,nband-1,nband,dtype='int8')[:,None]*np.ones((nband, len(ipix)),dtype='int8')
ipix_sparse = np.ravel(ipix[None,:]*np.ones(nband,dtype=int)[:,None])
ibnd_sparse = np.ravel(ibnd)
vals_sparse = np.concatenate([hp.ud_grade(vals0[i], nside_out=nside, power=-2.0)[ipix] for i in range(nband)])
idx = vals_sparse.nonzero()
npix_sparse = np.array([np.sum(vals_exp.nonzero()[0]==i) for i in range(nband)])

cols = [Column(name='PIX', data=ipix_sparse[idx], dtype='i8'),
        Column(name='CHANNEL', data=ibnd_sparse[idx], dtype='i2'),
        Column(name='VALUE', data=vals_sparse[idx], dtype='f8')]
tab_sparse0 = Table(cols, meta={'EXTNAME' : 'SKYMAP'})
                   
# Write File
tab_bands_sparse0 = create_bands_table(np.ones(4)*nside, npix_sparse, emin, emax)
hdulist = [fits.PrimaryHDU(), fits.table_to_hdu(tab_sparse0),
           fits.table_to_hdu(tab_bands_sparse0)]
hdr_sparse = hdr.copy()
hdr_sparse['INDXSCHM'] = 'SPARSE'
hdr_sparse['AXCOLS1'] = 'E_MIN,E_MAX'
hdr_sparse.pop('ORDER',None)
hdr_sparse.pop('NSIDE',None)
update_header(hdulist[1].header, **hdr_sparse)
fits.HDUList(hdulist).writeto('hpx_ccube_sparse0.fits', overwrite=True)

#################################
# SPARSE Cube (Variable NSIDE)

order = np.array([2,3,4,5])
nside = 2**order
ipix = [hp.query_disc(t, v[0], np.radians(rad), nest=True) for t in nside]
vals = [hp.ud_grade(vals0[i], nside_out=t, power=-2.0)[ipix[i]] for i, t in enumerate(nside)]

ibnd_sparse = np.concatenate([np.ones(len(t),dtype='i8')*i for i, t in enumerate(ipix)])
vals_sparse = np.concatenate(vals)
ipix_sparse = np.concatenate(ipix)

idx = vals_sparse.nonzero()
npix_sparse = np.array([np.count_nonzero(vals[i]) for i in range(nband)])

cols = [Column(name='PIX', data=ipix_sparse[idx], dtype='i8'),
        Column(name='CHANNEL', data=ibnd_sparse[idx], dtype='i2'),
        Column(name='VALUE', data=vals_sparse[idx], dtype='f8')]
tab_sparse1 = Table(cols, meta={'EXTNAME' : 'SKYMAP'})

# Write File
tab_bands_sparse1 = create_bands_table(nside, npix_sparse, emin, emax)
hdulist = [fits.PrimaryHDU(), fits.table_to_hdu(tab_sparse1),
           fits.table_to_hdu(tab_bands_sparse1)]
hdr_sparse = hdr.copy()
hdr_sparse['INDXSCHM'] = 'SPARSE'
hdr_sparse['AXCOLS1'] = 'E_MIN,E_MAX'
hdr_sparse.pop('ORDER',None)
hdr_sparse.pop('NSIDE',None)
update_header(hdulist[1].header, **hdr_sparse)
fits.HDUList(hdulist).writeto('hpx_ccube_sparse1.fits', overwrite=True)
