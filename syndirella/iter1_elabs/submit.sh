#!/bin/bash

for KEY in *"_syndirella_input.csv"; do
	KEY=${KEY:0:-21}
	echo $KEY

	sb.sh --job-name RdRp_syndirella_$KEY --ntasks=1 --cpus-per-task=1 --mem=10GB $HOME2/slurm/run_bash_with_conda.sh run_elaboration.sh $KEY

	# break

done
