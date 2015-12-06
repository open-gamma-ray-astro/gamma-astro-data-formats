.. include:: ../references.txt

.. _fits-arrays:

FITS Multidimensional datasets
==============================

As described e.g. `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/general/ogip_94_006/ogip_94_006.html>`__
or `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_003/cal_gen_92_003.html#tth_sEc4>`__
or in the `FITS standard document <http://adsabs.harvard.edu/abs/2010A%26A...524A..42P>`__,
there are several ways to serialise multi-dimensional arrays and corresponding axis information in FITS files.

Here we describe the schemes in use in gamma-ray astronomy and give examples.

.. _fits-arrays-image-hdu:

IMAGE HDU
---------

* Data array is stored in an IMAGE HDU.
* Axis information is either stored in the IMAGE HDU header or in extra BINTABLE HDUs, sometimes a mix.
* Advantage: IMAGE HDUs can be opened up in image viewers like ds9.
* Disadvantage: axis information is not self contained, an extra HDU is needed.

Example
+++++++

E.g. the Fermi-LAT counts cubes or diffuse model spectral cubes are stored in an IMAGE HDU,
with the information about the two celestial axes in WCS header keywords,
and the information about the energy axis in ENERGIES (for spectral cube) or EBOUNDS (for counts cube) BINTABLE HDU extensions.

.. code-block:: bash

    $ ftlist gll_iem_v02.fit H

            Name               Type       Dimensions
            ----               ----       ----------
    HDU 1   Primary Array      Image      Real4(720x360x30)
    HDU 2   ENERGIES           BinTable     1 cols x 30 rows

Let's have a look at the header of the primary IMAGE HDU.

As you can see, there's three axes.

The first two are Galactic longitude and latitude and the pixel to sky coordinate mapping
is specified by header keywords according to the `FITS WCS standard <http://fits.gsfc.nasa.gov/fits_wcs.html>`__.

I think the energy axis isn't a valid FITS WCS axis specification.
ds9 uses the `C????3` keys to infer a WCS mapping of pixels to energies, but it is incorrect.
Software that's supposed to work with this axis needs to know to look at the `ENERGIES` table instead.

.. code-block:: bash

    $ ftlist gll_iem_v02.fit K
    SIMPLE  =                    T / Written by IDL:  Tue Jul  7 15:25:03 2009
    BITPIX  =                  -32 /
    NAXIS   =                    3 / number of data axes
    NAXIS1  =                  720 / length of data axis 1
    NAXIS2  =                  360 / length of data axis 2
    NAXIS3  =                   30 / length of data axis 3
    EXTEND  =                    T / FITS dataset may contain extensions
    COMMENT   FITS (Flexible Image Transport System) format is defined in 'Astronomy
    COMMENT   and Astrophysics', volume 376, page 359; bibcode: 2001A&A...376..359H
    FLUX    =        8.29632317174 /
    CRVAL1  =                   0. / Value of longitude in pixel CRPIX1
    CDELT1  =                  0.5 / Step size in longitude
    CRPIX1  =                360.5 / Pixel that has value CRVAL1
    CTYPE1  = 'GLON-CAR'           / The type of parameter 1 (Galactic longitude in
    CUNIT1  = 'deg     '           / The unit of parameter 1
    CRVAL2  =                   0. / Value of latitude in pixel CRPIX2
    CDELT2  =                  0.5 / Step size in latitude
    CRPIX2  =                180.5 / Pixel that has value CRVAL2
    CTYPE2  = 'GLAT-CAR'           / The type of parameter 2 (Galactic latitude in C
    CUNIT2  = 'deg     '           / The unit of parameter 2
    CRVAL3  =                  50. / Energy of pixel CRPIX3
    CDELT3  =    0.113828620540137 / log10 of step size in energy (if it is logarith
    CRPIX3  =                   1. / Pixel that has value CRVAL3
    CTYPE3  = 'photon energy'      / Axis 3 is the spectra
    CUNIT3  = 'MeV     '           / The unit of axis 3
    CHECKSUM= '3fdO3caL3caL3caL'   / HDU checksum updated 2009-07-07T22:31:18
    DATASUM = '2184619035'         / data unit checksum updated 2009-07-07T22:31:18
    HISTORY From Ring/Hybrid fit with GALPROP 54_87Xexph7S extrapolation
    HISTORY Integrated flux (m^-2 s^-1) over all sky and energies:    8.30
    HISTORY Written by rings_gll.pro
    DATE    = '2009-07-07'         /
    FILENAME= '$TEMPDIR/diffuse/gll_iem_v02.fit' /File name with version number
    TELESCOP= 'GLAST   '           /
    INSTRUME= 'LAT     '           /
    ORIGIN  = 'LISOC   '           /LAT team product delivered from the LISOC
    OBSERVER= 'MICHELSON'          /Instrument PI
    END


.. _fits-arrays-bintable-hdu:

BINTABLE HDU
------------

* Data array and axis information is stored in a BINTABLE HDU with one row.
* See `here <http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_003/cal_gen_92_003.html#tth_sEc4>`__
  for further information on this format, e.g. on axis order.
* Advantage: everything is contained in one HDU. (as many axes and data arrays as you like)
* Disadvantage: format is a bit unintuitive / header is quite complex / can't be opened directly in ds9.


Example
+++++++

Let's look at an example file in this format, the :download:`aeff_P6_v1_diff_back.fits` which
represents the Fermi-LAT effective area (an old version) as a function of energy and offset.

The data array and axis information are stored in one BINTABLE HDU called "EFFECTIVE AREA",
with 5 columns and one row:

.. code-block:: bash

    $ ftlist aeff_P6_v1_diff_back.fits H

            Name               Type       Dimensions
            ----               ----       ----------
    HDU 1   Primary Array      Null Array
    HDU 2   EFFECTIVE AREA     BinTable     5 cols x 1 rows

There five columns contain arrays of different length that represent:

* First axis is energy (`ENERG_LO` and `ENERG_HI` columns) with 60 bins.
* Second axis is cosine of theta (`CTHETA_LO` and `CTHETA_HI` columns) with 32 bins.
* First and only data array is effective area (`EFFAREA`) at the given energy and cosine theta values.

.. code-block:: bash

    $ ftlist aeff_P6_v1_diff_back.fits C
    HDU 2

      Col  Name             Format[Units](Range)      Comment
        1 ENERG_LO           60E [MeV]
        2 ENERG_HI           60E [MeV]
        3 CTHETA_LO          32E
        4 CTHETA_HI          32E
        5 EFFAREA            1920E [m2]

The part that's most difficult to understand / remember is how the relevant information
is encoded in the BINTABLE FITS header.

But note the `HDUDOC  = 'CAL/GEN/92-019'` key. If you Google `CAL/GEN/92-019` you will
find that it points to the `OGIP spec for effective area files <https://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/docs/memos/cal_gen_92_019/cal_gen_92_019.html>`__,
which explains in detail what all the other keys mean.

There's some software (e.g. `fv`) that understands this way of encoding n-dimensional arrays
and axis information in FITS BINTABLEs.

.. code-block:: bash

    $ ftlist aeff_P6_v1_diff_back.fits[1] K
    XTENSION= 'BINTABLE'           / binary table extension
    BITPIX  =                    8 / 8-bit bytes
    NAXIS   =                    2 / 2-dimensional binary table
    NAXIS1  =                 8416 / width of table in bytes
    NAXIS2  =                    1 / number of rows in table
    PCOUNT  =                    0 / size of special data area
    GCOUNT  =                    1 / one data group (required keyword)
    TFIELDS =                    5 / number of fields in each row
    TTYPE1  = 'ENERG_LO'           /
    TFORM1  = '60E     '
    TTYPE2  = 'ENERG_HI'           /
    TFORM2  = '60E     '
    TTYPE3  = 'CTHETA_LO'          /
    TFORM3  = '32E     '           /
    TTYPE4  = 'CTHETA_HI'          /
    TFORM4  = '32E     '           /
    TTYPE5  = 'EFFAREA '           /
    TFORM5  = '1920E   '
    ORIGIN  = 'LISOC   '           / name of organization making this file
    DATE    = '2008-05-06T08:56:19.9999' / file creation date (YYYY-MM-DDThh:mm:ss U
    EXTNAME = 'EFFECTIVE AREA'     / name of this binary table extension
    TUNIT1  = 'MeV     '           /
    TUNIT2  = 'MeV     '           /
    TUNIT3  = '        '
    TUNIT4  = '        '
    TUNIT5  = 'm2      '           /
    TDIM5   = '(60, 32)'
    TELESCOP= 'GLAST   '           /
    INSTRUME= 'LAT     '           /
    DETNAM  = 'BACK    '
    HDUCLASS= 'OGIP    '           /
    HDUDOC  = 'CAL/GEN/92-019'     /
    HDUCLAS1= 'RESPONSE'           /
    HDUCLAS2= 'EFF_AREA'           /
    HDUVERS = '1.0.0   '           /
    EARVERSN= '1992a   '           /
    1CTYP5  = 'ENERGY  '           / Always use log(ENERGY) for interpolation
    2CTYP5  = 'COSTHETA'           / Off-axis angle cosine
    CREF5   = '(ENERG_LO:ENERG_HI,CTHETA_LO:CTHETA_HI)' /
    CSYSNAME= 'XMA_POL '           /
    CCLS0001= 'BCF     '           /
    CDTP0001= 'DATA    '           /
    CCNM0001= 'EFF_AREA'           /
    CBD10001= 'VERSION(P6_v1_diff)'
    CBD20001= 'CLASS(P6_v1_diff_back)'
    CBD30001= 'ENERG(18-560000)MeV'
    CBD40001= 'CTHETA(0.2-1)'
    CBD50001= 'PHI(0-360)deg'
    CBD60001= 'NONE    '
    CBD70001= 'NONE    '
    CBD80001= 'NONE    '
    CBD90001= 'NONE    '
    CVSD0001= '2007-01-17'         / Dataset validity start date (UTC)
    CVST0001= '00:00:00'           /
    CDES0001= 'GLAST LAT effective area' /
    EXTVER  =                    1 / auto assigned by template parser
    CHECKSUM= 'IpAMIo5LIoALIo5L'   / HDU checksum updated 2008-05-06T08:56:20
    DATASUM = '340004495'          / data unit checksum updated 2008-05-06T08:56:20
    END
