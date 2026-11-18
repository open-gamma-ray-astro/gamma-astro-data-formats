"""Generate an example energy dispersion file."""

from astropy.io import fits
import astropy.units as u
from astropy.table import Table
import numpy as np

e_bins = 20
m_bins = 10
o_bins = 5
e_axis = np.logspace(-1, 2, e_bins + 1) * u.TeV
m_axis = np.geomspace(2e-1, 5, m_bins + 1) * u.dimensionless_unscaled
o_axis = np.linspace(0, 3, o_bins + 1) * u.deg
# Normalize EDISP
edisp = np.ones([e_bins, m_bins, o_bins])
edisp = (
    edisp
    / edisp.sum(axis=1)[:, np.newaxis, :]
    / np.diff(m_axis)[np.newaxis, :, np.newaxis]
)

# we have to add one dimension, so we only have one row in the binary table
# and each column is an array of the correct dimension
table = Table(
    {
        "ENERG_LO": e_axis[np.newaxis, :-1],
        "ENERG_HI": e_axis[np.newaxis, 1:],
        "MIGRA_LO": m_axis[np.newaxis, :-1],
        "MIGRA_HI": m_axis[np.newaxis, 1:],
        "THETA_LO": o_axis[np.newaxis, :-1],
        "THETA_HI": o_axis[np.newaxis, 1:],
        "MATRIX": edisp.T[np.newaxis, ...],
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
header["HDUVERS"] = "0.3", ""
header["HDUCLASS"] = "GADF", ""
header["HDUCLAS1"] = "RESPONSE", ""
header["HDUCLAS2"] = "EDISP", ""
header["HDUCLAS3"] = "FULL-ENCLOSURE", ""
header["HDUCLAS4"] = "EDISP_2D", ""


edisp_hdu = fits.BinTableHDU(table, header, name="ENERGY DISPERSION")

primary_hdu = fits.PrimaryHDU()
hdulist = fits.HDUList([primary_hdu, edisp_hdu])

filename = "edisp_2d_full_example.fits"
print("Writing {}".format(filename))

hdulist.writeto(filename, overwrite=True)
