# #!/bin/bash

# set -e

# KEY=$1

# echo --input $(pwd)/$KEY"_syndirella_input.csv"
# echo --hits_path $(pwd)/$KEY"_syndirella_inspiration_hits.sdf"
# echo --output $(pwd)/$KEY"_elabs"
# echo --metadata "/opt/xchem-fragalysis-2/maxwin/3C_FFF/metadata.csv"
# echo --templates "$(pwd)/templates"

# /opt/xchem-fragalysis-2/maxwin/conda/bin/syndirella \
# 	--input $(pwd)/$KEY"_syndirella_input.csv" \
# 	--hits_path $(pwd)/$KEY"_syndirella_inspiration_hits.sdf" \
# 	--output $(pwd)/$KEY"_elabs" \
# 	--templates "$(pwd)/templates" \
# 	--metadata "/opt/xchem-fragalysis-2/maxwin/3C_FFF/metadata.csv" \
# 	--no_scaffold_place
	

# sb.sh --job-name syndirella $HOME2/slurm/run_bash_with_conda.sh ./run_elaboration.sh

