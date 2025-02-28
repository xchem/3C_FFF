# FFF_Template

To use this repository:

1. Use this template to create a new repository
1. Clone the newly repository on IRIS
1. Follow the steps indicated below

## 2. Setup the Target for FFF with HIPPO and BulkDock

- [x] Define merging opportunities by creating tags of LHS hits in Fragalysis
- [x] Download target from Fragalysis and place the .zip archive in the repo
- [x] Setup target in BulkDock 

```bash
cp -v D68EV3C.zip $BULK/TARGETS
cd $BULK
python -m bulkdock extract D68EV3C
python -m bulkdock setup D68EV3C
```

- [x] Copy the `aligned_files` directory from `$BULK/TARGETS/D68EV3C/aligned_files` into this repository

```bash
cd - 
cp -rv $BULK/TARGETS/D68EV3C/aligned_files .
```

## 3. Compound Design

- [x] run the notebook `hippo/1_merge_prep.ipynb`

### Fragmenstein

For each merging hypothesis (i.e. iter1)

- [x] go to the fragmenstein subdirectory `cd fragmenstein`
- [x] queue fragmenstein job 

```bash
sbatch --job-name "D68EV3C_iter1_fragmenstein" --mem 16000 $HOME2/slurm/run_bash_with_conda.sh run_fragmenstein.sh iter1
```

This will create outputs in the chosen iter1 subdirectory:

- **`iter1_fstein_bulkdock_input.csv`: use this for BulkDock placement**
- `output`: fragmenstein merge poses in subdirectories
- `output.sdf`: fragmenstein merge ligand conformers
- `output.csv`: fragmenstein merge metadata

- [ ] placement with bulkdock

```bash
cp -v iter1_fstein_bulkdock_input.csv $BULK/INPUTS/D68EV3C_iter1_fstein.csv
cd $BULK
python -m bulkdock place D68EV3C INPUTS/D68EV3C_iter1_fstein.csv
```

- [ ] monitor placements (until complete)

```bash
python -m bulkdock status
```

To loop indefinitely:

```bash
watch python -m bulkdock status
```

- [ ] export Fragalysis SDF

```bash
sbatch --job-name "D68EV3C_iter1_fstein_out" $HOME2/slurm/run_python.sh -m bulkdock to-fragalysis D68EV3C OUTPUTS/SDF_FILE iter1_fstein
```

- [ ] Copy back to this repository

```bash
cd - OUTPUTS/SDF_FILE
cp -v $BULK/OUTPUTS/D68EV3C_iter1*fstein*fragalysis.sdf .
```

### Fragment Knitwork

Running Fragment Knitting currently requires access to a specific VM known as `graph-sw-2`. If you don't have access, skip this section

- [ ] `git add`, `commit` and `push` the contents of `aligned_files` and `knitwork` to the repository
- [ ] `git clone` the repository on `graph-sw-2`
- [ ] navigate to the `knitwork` subdirectory

Then, for each merging hypothesis:

- [ ] Run the "fragment" step of FragmentKnitwork: `./run_fragment.sh iter1`
- [ ] Run the pure "knitting" step of FragmentKnitwork: `./run_knitwork_pure.sh iter1`
- [ ] Run the impure "knitting" step of FragmentKnitwork: `./run_knitwork_impure.sh iter1`
- [ ] Create the BulkDock inputs: `python to_bulkdock.py iter1`
- [ ] `git add`, `commit` and `push` the CSVs created by the previous step
- [ ] back on `cepheus-slurm` pull the latest changes
- [ ] Run BulkDock placement as for Fragmenstein above

```bash
cp -v iter1_knitwork_pure.csv $BULK/INPUTS/D68EV3C_iter1_knitwork_pure.csv
cp -v iter1_knitwork_impure.csv $BULK/INPUTS/D68EV3C_iter1_knitwork_impure.csv
cd $BULK
python -m bulkdock place D68EV3C INPUTS/D68EV3C_iter1_knitwork_pure.csv
python -m bulkdock place D68EV3C INPUTS/D68EV3C_iter1_knitwork_impure.csv
```

### Summary tables / figures

**CREATE NOTEBOOK**

- [ ] Export Fragalysis SDF as for Fragmenstein

## 4. Scaffold selection

### Syndirella retrosynthesis
### Review chemistry
### HIPPO filtering
### Fragalysis curation

## 5. Syndirella elaboration

**INCREASE MEMORY ALLOCATION**

## 6. HIPPO

### Load elaborations
### Quote reactants
### Solve routes
### Calculate interactions
### Generate random recipes
### Score random recipes
### Optimise best recipes
### Create proposal web page

## 7. Review & order

### Review chemistry
### Order reactants
