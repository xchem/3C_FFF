import hippo
import mrich

animal = hippo.HIPPO("FFF", "../../BulkDock/TARGETS/D68EV3C/D68EV3C.sqlite")

# gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="2A_i2_1_rgen.json")
# poses = gen.route_pool.products.poses

compounds = animal.db.get_route_products()
poses = compounds.poses

mrich.var("poses", poses)

for pose in mrich.track(poses):

    try:
        pose.calculate_interactions()
    except Exception as e:
        mrich.error(e)
        mrich.error("Could not fingerprint pose")
        continue
    
animal.db.close()

# sb.sh --job-name 3C_interactions -pgpu --exclusive --no-requeue $HOME2/slurm/run_python.sh 7_interactions.py