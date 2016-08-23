#!/bin/bash
source /vols/grid/cms/setup.sh

export WORKDIR=${PWD}
export CMSSW_LHE=${PWD}/CMSSW_7_1_21/src
export CMSSW_GENSIM=${PWD}/CMSSW_7_1_21/src
export CMSSW_PUMixing=${PWD}/CMSSW_8_0_3_patch2/src
export CMSSW_AODSIM=${PWD}/CMSSW_8_0_3_patch2/src
export CMSSW_MINIAODSIM=${PWD}/CMSSW_8_0_5_patch1/src

export PYTHONPATH=${PYTHONPATH}:${PWD}
export PYTHONPATH=${PYTHONPATH}:${PWD}/python
export PYTHONPATH=${PYTHONPATH}:${PWD}/Step3-PUMixing

if [ $1 = LHE ]; then
    cd $CMSSW_LHE
    eval `scramv1 runtime -sh`
    cd $WORKDIR
elif [ $1 = GENSIM ]; then
    cd $CMSSW_GENSIM
    eval `scramv1 runtime -sh`
    cd $WORKDIR
elif [ $1 = PUMixing ]; then
    cd $CMSSW_PUMixing
    eval `scramv1 runtime -sh`
    cd $WORKDIR
elif [ $1 = AODSIM ]; then
    cd $CMSSW_AODSIM
    eval `scramv1 runtime -sh`
    cd $WORKDIR
elif [ $1 = MINIAODSIM ]; then
    cd $CMSSW_MINIAODSIM
    eval `scramv1 runtime -sh`
    cd $WORKDIR
fi

source /cvmfs/cms.cern.ch/crab3/slc6_amd64_gcc493/cms/crabclient/3.3.1602/etc/profile.d/init.sh
