from pathlib import Path

import pandas as pd
from dysh.fits import GBTFITSLoad
from pandas.testing import assert_series_equal


def read_gbtidl_summary(filename, idx=1):
    """
    """
    with open(filename, "r") as log:
        lines = log.readlines()
    lines.pop(idx)
    tmp = Path(f"{filename}.tmp")
    with open(tmp, "w") as f:
        for line in lines:
            f.write(line)
    
    df = pd.read_fwf(f"{filename}.tmp")
    # Clean up.
    tmp.unlink()
    
    return df

cols = {"SCAN": "Scan",
        "OBJECT": "Source",
        "VELOCITY": "Vel",
        # "PROC": "Proc", # GBTIDL trims the names.
        "PROCSEQN": "Seq",
        "# IF": "nIF",
        "# INT": "nInt",
        "# FEED": "nFd"
       }

def test_summary():
    """
    """

    path = "/home/dysh/acceptance_testing/data"
    projs = ["AGBT13A_240_03",
             ]

    for proj in projs:
        try:
            sdf = GBTFITSLoad(f"{path}/{proj}/{proj}.raw.vegas/")
        except:
            sdf = GBTFITSLoad(f"{path}/{proj}/")
        dysh_df = sdf.summary()
        gbtidl_summary = read_gbtidl_summary(f"{path}/{proj}/gbtidl/{proj}.summary")

        for col in cols.items():
            assert_series_equal(dysh_df[col[0]], 
                                gbtidl_summary[col[1]], 
                                check_dtype=False, check_names=False)
