# ProdDMS
Production of Monte Carlo DM samples

## How to run

### Setup
I will assume that you are working at Imperial. I have tested the code on `lx03`
and `lx04`. 

For the initial setup read the following instructions. First of all, move to a 
directory where you'd like to work from and then get all the relevant code from 
the github repository:
```bash
git clone https://github.com/shane-breeze/ProdDMS.git
cd ProdDMS
```

Get all the relevant CMSSW versions for the necessary campaign. For 80X:
```bash
source /vols/grid/cms/setup.sh
cmsrel CMSSW_7_1_21
cmsrel CMSSW_8_0_3_patch2
cmsrel CMSSW_8_0_5_patch1
```

Now we have completed the initial setup. The following chain of commands can be
used to setup the environment each time you login. Simply move into the ProdDMS
directory first and then run (including after the initial setup):
```bash
git pull origin # only if you need to update your ProdDMS local repository
source setup.sh $STEP
voms-proxy-init -voms cms
```
where `$STEP` is the current MC step you're running over: LHE, GENSIM, PUMixing,
AODSIM or MINIAODSIM. This will update your local repository, setup the CMS 
environment, setup the ProdDMS environment, setup the CRAB environment and setup 
your GRID proxy.

### LHE Step
There are two methods to complete the LHE step: running a single job on the GRID
or running multiple jobs on the local Imperial batch. Both methods are discussed
below.

#### Batch
Running on the batch is necessary for jobs that take a long time running on a 
single job. Since it has been a struggle trying to get CRAB to run several LHE
jobs with different random seeds, I have resorted to running on the Imperial 
batch. 

Setup the correct CMSSW version with exactly the following command:
```bash
cd $CMSSW_LHE
cmsenv
cd $WORKDIR
```

Move into the `batchLHE` directory:
```bash
cd Step1-LHE/batchLHE
```
To generate LHE files from a gridpack, we must first locate the gridpack, for
example:
```bash
export GRIDPACK=/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/Dark_Matter/DMV_NNPDF30_13TeV_Axial_0p25/v2/POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10_tarball.tar.gz
```
This gridpack can be located anywhere. However, you may notice your jobs finish
faster if the gridpacks are located on the `/vols/build/` disk. However, `/cvmfs/`
is also ok.

Choose a output directory for your LHE files. I strongly suggest that you use 
`/vols/build/` for this one, for example:
```bash
export OUTDIR=/vols/buils/cms/${USER}/LHE-files
```

To submit the jobs run:
```bash
./batchSubmitLHE.py $GRIDPACK --maxEvents 300000 --nJobs 750 -o $OUTDIR -t 3:0:0
```
where `--maxEvents` is the total number of events to generate (default is 
300000), `--nJobs` is the number of jobs to split this up into (default is 750),
`-o` is the output directory and `-t` is the time allocated for each job 
(default is 3:0:0, i.e. 3 hours). For the time, I suggest you use 3 hours or less.
You can check that status of your jobs with the `qstat` command. To check and 
resubmit any failed jobs run:
```bash
./batchSubmitLHE.py $GRIDPACK --maxEvents 300000 --nJobs 750 -o $OUTDIR -t 6:0:0 --resubmit
```
with a longer time per job, while keeping all other parameters identical to the
original submission.

After all jobs have finished successfully we want to merge all the separate LHE
into one. To do this, we need the list of all lhe files:
```bash
export LHEDIR=${OUTDIR}/$(basename $GRIDPACK | sed 's/_tarball.tar.gz//g' | awk '{print "lheFiles_"$1}')
ls -d -1 $LHEDIR/*.lhe > lheList
./mergeLheFiles lheList
```
After it finishes merging the files move it to the relevant directory
```bash
export LHEFILE==$(echo $LHEDIR | sed 's/lheFiles_/cmsgrid_/g' | awk '{print $1".lhe"}')
mv out.lhe $LHEFILE
```
This output LHE file is typically quite large and hence we need to transfer it 
the T2 storage site at Imperial before we can run jobs over it. To do this run:
```bash
./transferICT2.py $LHEFILE $USERNAME
```
where `$USERNAME` is your GRID username. This will create a folder in your T2
storage site named `LHE-files` containing the merged LHE file. You can list the
contents of this directory like so:
```bash
xrd gfe02.grid.hep.ph.ic.ac.uk:1097 ls /store/user/$USERNAME/LHE-files
```
again with `$USERNAME` replace with your GRID username. After the transfer and 
if you're happy, you can delete the local LHE files since we now have it on the 
T2 site:
```bash
rm -rf $LHEDIR
rm $LHEFILE
```
The next step is to convert the LHE file into an EDM format. This is a fairly 
quick process and similar to generating the LHE file with a single job on the
grid, so I will discuss this below. However, move back into the main directory
```bash
cd $WORKDIR
```

#### GRID
Setup the correct environment:
```bash
source setup.sh LHE
```
Open up the file named `inputConfig_LHE.py` and make a new object for your
desired model, following the example given in this file, beginning with
```python
myobject = config()
```

`produceLHE` must be `True` if you want to generate the LHE files on the GRID
and `False` if you've already created them. `testEvents` is the number of events
to run over during the test. `lheFile` is the path on the T2 storage site to the
LHE file. `gridPack` is the path to the grid-pack. `outputRootFile` is the name
of the output root file. `xmlFile` is the name of the xml file from the test run.
`requestName` is the requested name in the CRAB config. `workArea` is the 
location of the output CRAB logs (no need to change). `maxEvents` is the total 
number of events to submit to the GRID, `outputPrimaryDataset` is a CRAB
parameter. `outputDatasetTag` is a CRAB parameter. All of these parameters must
be set.

To use the object you've created, at the end of the file make your object copy 
into `inputConfig`:
```python
inputConfig = myobject
```

Now we can run the test command:
```bash
./runMC.py --step LHE --test
```
take note of the output and make sure everything looks ok.

To submit to the GRID:
```bash
./runMC.py --step LHE
```
To check the status of the job
```bash
./runMC.py --step LHE --status
```
To kill the jobs
```bash
./runMC.py --step LHE --kill
```
To resubmit failed jobs
```bash
./runMC.py --step LHE --resubmit
```
