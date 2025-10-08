"""Convert pgadmin csv output to parquet (useful for data/plotting things)"""

import pandas as pd
from datetime import datetime
from pathlib import Path


# Specify directories
indir = Path("../data/pgadmin-dl")
outdir = Path(f"../../_backups/{datetime.now().strftime(r'%y%m%d')}_parquet")
outdir.mkdir(exist_ok=True, parents=True)


# Convert each file
files = sorted(indir.glob("*.csv"))
for i, file in enumerate(files, start=1):
    print(f"Working on file {file.name} ({i} of {len(files)})")
    print("... reading")
    data = pd.read_csv(file, escapechar="'")
    print("... saving")
    data.to_parquet(outdir / f"{file.stem}.parquet")

print("Done!")
