import pytest
import numpy as np

from pathlib import Path

from astropy.io import fits
from dysh.fits import GBTFITSLoad


def test_onoff():
    """
    """


    path = "/home/dysh/acceptance_testing/data"
    projs = {"AGBT15B_228_08": 29,
             "AGBT16B_392_01": 24,
             "AGBT17B_004_14": 34,
             "AGBT18B_354_03": 6,
            }

    for proj,scan in projs.items():

        # Only test if GBTIDL produced a result.
        gbtidl_file = Path(f"{path}/{proj}/gbtidl/{proj}.getps.vegas.fits")
        if gbtidl_file.is_file():
            
            try:
                sdf = GBTFITSLoad(f"{path}/{proj}/{proj}.raw.vegas/")
            except:
                sdf = GBTFITSLoad(f"{path}/{proj}/")
            
            getps = sdf.getps(scan, plnum=0)
            ps = getps.timeaverage()[0]
            vals = ps.flux.value

            hdu = fits.open(gbtidl_file)
            table = hdu[1].data
            gbtidl_spec = table["DATA"][0]

            # Do not compare NaN values.
            mask = np.isnan(vals) | np.isnan(gbtidl_spec)

            # Compare data.
            assert np.all( (vals[~mask] - gbtidl_spec[~mask]) < 1e-3 )

            # Compare metadata.
            for col in table.names:
                if col not in ["DATA"]:
                    print(col)
                    try:
                        ps.meta[col]
                    except KeyError:
                        print(f"{col} not found -- {table[col][0]}")
                        continue
                    try:
                        assert ps.meta[col] == pytest.approx(table[col][0], 1e-3)
                    except AssertionError:
                        print(f"{col} fails: {ps.meta[col]}, {table[col][0]}")
