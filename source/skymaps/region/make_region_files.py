import logging
import numpy as np
from regions import CircleSkyRegion, fits_region_objects_to_table
from astropy.table import Table
from astropy.io import fits
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def create_wcs():
    """Create wcs to project region"""
    # create wcs for regions
    wcs = WCS(naxis=2)
    wcs.wcs.crpix = [0, 0]
    wcs.wcs.cdelt = [-0.01, 0.01]
    wcs.wcs.crval = [83.63, 22.01]
    wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    return wcs


def create_region_table_hdu(region, hdu_name):
    """Create region table hdu"""
    wcs = create_wcs()
    region_pix = region.to_pixel(wcs)
    region_table = fits_region_objects_to_table([region_pix])

    header = wcs.to_header()
    header["WCSSHAPE"] = "(40, 40)"
    region_table.meta.update(header)
    return fits.BinTableHDU(region_table, name=hdu_name + "_REGION")


def create_data_table_hdu(data, energy_min, energy_max, hdu_name):
    """Create data tabel hdu"""
    # create data table
    data_table = Table()
    data_table["CHANNEL"] = np.arange(len(energy))
    data_table["E_MIN"] = energy_min
    data_table["E_MAX"] = energy_max
    data_table["DATA"] = data
    data_table.meta["AXCOLS1"] = "E_MIN,E_MAX"
    data_table.meta["INTERP1"] = "log"
    return fits.BinTableHDU(data_table, name=hdu_name)


def create_data_table_hdu_time(data, energy_min, energy_max, time_min, time_max, hdu_name):
    """Create data tabel hdu"""
    # create data table
    time_min, energy_min = np.meshgrid(time_min, energy_min)
    time_max, energy_max = np.meshgrid(time_max, energy_max)

    data_table = Table()
    data_table["CHANNEL"] = np.arange(len(energy) * len(time))
    data_table["E_MIN"] = energy_min.flatten()
    data_table["E_MAX"] = energy_max.flatten()
    data_table["TIME_MIN"] = time_min.flatten()
    data_table["TIME_MAX"] = time_max.flatten()
    data_table["DATA"] = data.flatten()

    # define meta data
    data_table.meta["AXCOLS1"] = "E_MIN,E_MAX"
    data_table.meta["INTERP1"] = "log"
    data_table.meta["AXCOLS2"] = "TIME_MIN,TIME_MAX"
    data_table.meta["INTERP2"] = "lin"
    return fits.BinTableHDU(data_table, name=hdu_name)


# create and write energy dependent counts
energy_edges = np.geomspace(1 * u.TeV, 100 * u.TeV, 30)
energy_min, energy_max = energy_edges[:-1], energy_edges[1:]
energy = np.sqrt(energy_min * energy_max)

data = (energy / (1 * u.TeV)).to("") ** -2.3

# create region
region = CircleSkyRegion(
    center=SkyCoord("83.63d", "22.01d"), radius=0.2 * u.deg
)

data_hdu = create_data_table_hdu(
    data=data,
    energy_min=energy_min,
    energy_max=energy_max,
    hdu_name="COUNTS"
)

region_hdu = create_region_table_hdu(region=region, hdu_name="COUNTS")

hdulist = fits.HDUList([fits.PrimaryHDU(), data_hdu, region_hdu])
filename = "region_map_1d.fits"
log.info(f"Writing {filename}")
hdulist.writeto(filename, overwrite=True)


# create and write time dependent counts
time_edges = np.linspace(0, 10, 10) * u.h
time_min, time_max = time_edges[:-1], time_edges[1:]
time = (time_min + time_max) / 2
time = time.reshape((-1, 1))

data = np.exp(-time / (5 * u.h)) * (energy / (1 * u.TeV)).to("") ** -2.3

data_hdu = create_data_table_hdu_time(
    data=data,
    energy_min=energy_min,
    energy_max=energy_max,
    time_min=time_min,
    time_max=time_max,
    hdu_name="COUNTS"
)

hdulist = fits.HDUList([fits.PrimaryHDU(), data_hdu, region_hdu])
filename = "region_map_2d.fits"
log.info(f"Writing {filename}")
hdulist.writeto(filename, overwrite=True)