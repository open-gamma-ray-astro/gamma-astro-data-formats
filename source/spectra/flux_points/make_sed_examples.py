from fermipy.spectrum import PowerLaw
import numpy as np
from astropy.table import Table, Column

np.random.seed(1)

s = PowerLaw([1E-12, -2.2], scale=1E3)
sref = PowerLaw([1E-12, -2.0], scale=1E3)

ebins = np.linspace(2.0, 5.0, 3 * 8 + 1)


emin = ebins[:-1]
emax = ebins[1:]
ectr = 0.5 * (emin + emax)

flux = s.flux(10**emin, 10**emax)
dnde = s.dnde(10**ectr)

ref_flux = sref.flux(10**emin, 10**emax)
ref_eflux = sref.eflux(10**emin, 10**emax)
ref_dnde = sref.dnde(10**ectr)


exp = 1.1E12
npred = exp * flux
ref_npred = exp * ref_flux

nmeas = np.random.poisson(npred).astype(float)

meas_flux = nmeas / npred * flux
meas_flux_err = nmeas**0.5 / npred * flux
meas_flux_ul = 1.644853 * meas_flux_err + meas_flux
meas_dnde = nmeas / npred * dnde
meas_dnde_err = nmeas**0.5 / npred * dnde
meas_dnde_ul = 1.644853 * meas_dnde_err + meas_dnde

m = meas_flux_err == 0

meas_flux_err[m] = 1.0 / npred[m] * flux[m]
meas_dnde_err[m] = 1.0 / npred[m] * dnde[m]

norm = flux / ref_flux
norm_err = meas_flux_err / ref_flux
norm_ul = 1.644853 * norm_err + norm

stephi = np.linspace(0, 1, 11)
steplo = -np.linspace(0, 1, 11)[1:][::-1]

loscale = 3 * norm_err
hiscale = 3 * norm_err
loscale[loscale > norm] = norm[loscale > norm]

norm_vals_hi = norm[:, np.newaxis] + \
    stephi[np.newaxis, :] * hiscale[:, np.newaxis]
norm_vals_lo = norm[:, np.newaxis] + \
    steplo[np.newaxis, :] * loscale[:, np.newaxis]

norm_vals = np.hstack((norm_vals_lo, norm_vals_hi))
dll_vals = -0.5 * (norm_vals - norm[:, np.newaxis]) ** 2 / \
    norm_err[:, np.newaxis] ** 2

norm_vals *= norm[:, None]
loglike = 0.5 * (norm / norm_err)**2.0
loglike_null = np.zeros_like(loglike)

ts = 2.0 * (loglike - loglike_null)

dll_vals += loglike[:, None]

meas_flux[ts < 9] = np.nan
meas_flux_err[ts < 9] = np.nan
meas_flux_ul[ts > 9] = np.nan

ul = np.empty(len(meas_flux), dtype=bool)
ul.fill(True)
ul[ts > 9] = False

# Flux Points

cols = [Column(name='e_min', unit='MeV', data=10**emin, format='%.2f'),
        Column(name='e_max', unit='MeV', data=10**emax, format='%.2f'),
        Column(name='flux', unit='1 / (cm2 s)', data=meas_flux, format='%8.4g'),
        Column(name='flux_err', unit='1 / (cm2 s)', data=meas_flux_err, format='%8.4g'),
        Column(name='flux_ul', unit='1 / (cm2 s)', data=meas_flux_ul, format='%8.4g'),
        Column(name='is_ul', data=ul)]

tab = Table(cols)
tab.meta['SED_TYPE'] = 'flux'
tab.meta['UL_CONF'] = 0.95

tab.write('flux_points.fits', overwrite=True)
tab.write('flux_points.ecsv', format='ascii.ecsv', overwrite=True)
tab.write('flux_points.h5', format='hdf5', path='/sed', overwrite=True)

meas_dnde[ts < 9] = np.nan
meas_dnde_err[ts < 9] = np.nan
meas_dnde_ul[ts > 9] = np.nan

# Differential Flux Points

cols = [Column(name='e_ref', unit='MeV', data=10**ectr, format='%.2f'),
        Column(name='dnde', unit='1 / (MeV cm2 s)', data=meas_dnde, format='%8.4g'),
        Column(name='dnde_err', unit='1 / (MeV cm2 s)', data=meas_dnde_err, format='%8.4g'),
        Column(name='dnde_ul', unit='1 / (MeV cm2 s)', data=meas_dnde_ul, format='%8.4g')]

tab = Table(cols)
tab.meta['SED_TYPE'] = 'dnde'
tab.meta['UL_CONF'] = 0.95

tab.write('diff_flux_points.fits', overwrite=True)
tab.write('diff_flux_points.ecsv', format='ascii.ecsv', overwrite=True)
tab.write('diff_flux_points.h5', format='hdf5', path='/sed', overwrite=True)

# Likelihood

cols = [Column(name='e_min', unit='MeV', data=10**emin, format='%.2f'),
        Column(name='e_ref', unit='MeV', data=10**ectr, format='%.2f'),
        Column(name='e_max', unit='MeV', data=10**emax, format='%.2f'),
        Column(name='norm', data=norm, format='%8.4g'),
        Column(name='norm_err', data=norm_err, format='%8.4g'),
        Column(name='norm_ul', data=norm_ul, format='%8.4g'),
        Column(name='ts', data=ts, format='%.2f'),
        Column(name='loglike', data=loglike, format='%.2f'),
        Column(name='loglike_null', data=loglike_null, format='%8.4g'),
        Column(name='dloglike_scan', data=dll_vals, format='%.2f'),
        Column(name='norm_scan', data=norm_vals, format='%8.4g'),
        Column(name='ref_flux', unit='1 / (cm2 s)', data=ref_flux, format='%8.4g'),
        Column(name='ref_eflux', unit='MeV / (cm2 s)', data=ref_eflux, format='%8.4g'),
        Column(name='ref_dnde', unit='1 / (MeV cm2 s)', data=ref_dnde, format='%8.4g'),
        Column(name='ref_npred', data=ref_npred, format='%8.4g'),
        ]

tab = Table(cols)
tab.meta['SED_TYPE'] = 'likelihood'
tab.meta['UL_CONF'] = 0.95

tab.write('binlike.fits', overwrite=True)
tab.write('binlike.h5', format='hdf5', path='/sed', overwrite=True)

# ECSV doesn't support multi-dimensional columns
tab2 = tab.copy()
tab2.remove_columns(['dloglike_scan', 'norm_scan'])
tab2.write('binlike.ecsv',format='ascii.ecsv', overwrite=True)


tab = Table.read('1es0229_hess_spectrum.ecsv',format='ascii.ecsv')
tab.write('1es0229_hess_spectrum.fits', overwrite=True)

