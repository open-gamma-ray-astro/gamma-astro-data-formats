"""Generate an example PSF file."""

from astropy.io import fits
import astropy.units as u
from astropy.table import Table
import numpy as np

e_bins = 20
r_bins = 20
x_bins = 15
y_bins = 15
e_axis = np.logspace(-1, 2, e_bins + 1) * u.TeV
r_axis = np.linspace(0, 2, r_bins + 1) * u.deg
x_axis = np.linspace(-3, 3, x_bins + 1) * u.deg
y_axis = np.linspace(-3, 3, y_bins + 1) * u.deg
# Normalize the PSF values
solid_angle = np.diff(2 * np.pi * (1 - np.cos(r_axis.to_value(u.rad))) * u.sr)
rpsf = np.ones([e_bins, x_bins, y_bins, r_bins])
rpsf = rpsf / rpsf.sum(axis=-1)[..., np.newaxis] / solid_angle
# we have to add one dimension, so we only have one row in the binary table
# and each column is an array of the correct dimension
table = Table(
    {
        "ENERG_LO": e_axis[np.newaxis, :-1],
        "ENERG_HI": e_axis[np.newaxis, 1:],
        "DETX_LO": x_axis[np.newaxis, :-1],
        "DETX_HI": x_axis[np.newaxis, 1:],
        "DETY_LO": y_axis[np.newaxis, :-1],
        "DETY_HI": y_axis[np.newaxis, 1:],
        "RAD_LO": r_axis[np.newaxis, :-1],
        "RAD_HI": r_axis[np.newaxis, 1:],
        # transpose as FITS uses opposite dimension order
        "RPSF": rpsf.T[np.newaxis, ...],
    }
)

header = fits.Header()
header["OBS_ID"] = 31415, "Observation ID"
header["LO_THRES"] = 0.1, "Low energy threshold [TeV]"
header["HI_THRES"] = 50, "High energy threshold [TeV]"
header["HDUDOC"] = (
    "https://github.com/open-gamma-ray-astro/gamma-astro-data-formats",
    "",
)
header["HDUVERS"] = "0.4", ""
header["HDUCLASS"] = "GADF", ""
header["HDUCLAS1"] = "RESPONSE", ""
header["HDUCLAS2"] = "PSF", ""
header["HDUCLAS3"] = "FULL-ENCLOSURE", ""
header["HDUCLAS4"] = "PSF_3D", ""


edisp_hdu = fits.BinTableHDU(table, header)

primary_hdu = fits.PrimaryHDU()
hdulist = fits.HDUList([primary_hdu, edisp_hdu])

filename = "psf_table_3d_full_example.fits"
print("Writing {}".format(filename))

hdulist.writeto(filename, overwrite=True)
