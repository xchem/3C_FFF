
import hippo
import mrich

animal = hippo.HIPPO("FFF", "../../BulkDock/TARGETS/D68EV3C/D68EV3C.sqlite")

gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="D68EV3C_rgen.json")

for budget in [5_000, 7_500, 10_000]:

    for i in range(100):
        mrich.header("budget=", budget, "i=", i)
        
        try:
            r = gen.generate(
                budget=budget,
                currency="EUR",
                max_products=3000,
                max_reactions=6000,
                debug=False,
                max_iter=len(gen.route_pool)+1,
                shuffle=True,
                balance_clusters=False,
                permitted_clusters=None,
            )
        except Exception as e:
            mrich.error(e)
            continue

animal.db.close()

# sb.sh --job-name 3C_rgen -pgpu --exclusive --no-requeue $HOME2/slurm/run_python.sh 9_rgen.py
