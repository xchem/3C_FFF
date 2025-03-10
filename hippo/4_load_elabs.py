from pathlib import Path
import hippo
import mrich

mrich.var("hippo", hippo.__file__)

animal = hippo.HIPPO("3C_FFF", "../../BulkDock/TARGETS/D68EV3C/D68EV3C.sqlite")
animal.db.backup()

output_root = Path("../syndirella/iter1_elabs/")

files = list(output_root.glob("*/*-*-?/*to_hippo*"))

for i,file in enumerate(files):
    mrich.h2(f"{i+1}/{len(files)}")
    try:
        animal.add_syndirella_elabs(file)
    except Exception as e:
        mrich.error(file)
        mrich.error(e)
        continue
    
animal.db.close()

# sb.sh --job-name 3C_load_elabs --exclusive --no-requeue $HOME2/slurm/run_python.sh 4_load_elabs.py
