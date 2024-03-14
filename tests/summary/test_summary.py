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
             "AGBT14B_480_06",
             "AGBT15B_228_08",
             "AGBT16B_392_01",
             "AGBT17B_004_14",
             "AGBT18A_503_02",
             "AGBT18B_354_03",
             "AGBT19A_080_01",
             "AGBT19A_473_41",
             "AGBT19B_096_08",
             "AGBT20B_336_01",
             "AGBT22A_325_15"
             ]

    for proj in projs:
        try:
            sdf = GBTFITSLoad(f"{path}/{proj}/{proj}.raw.vegas/")
        except:
            sdf = GBTFITSLoad(f"{path}/{proj}/")
        dysh_df = sdf.summary()
        gbtidl_summary = read_gbtidl_summary(f"{path}/{proj}/gbtidl/{proj}.summary")

        for col in cols.items():
            assert_series_equal(dysh_df[col[0]], #.sort_values(), 
                                gbtidl_summary[col[1]], #.sort_values(), 
                                check_dtype=False, 
                                check_names=False,
                                check_index=False)
