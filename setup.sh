#!/bin/bash
if [[ "$HOSTNAME" == *hep.ph.ic.ac.uk ]]; then
    . /vols/grid/cms/setup.sh
fi

export CMSSW_LHE=${PWD}/CMSSW_7_1_21/src
export CMSSW_GENSIM=${PWD}/CMSSW_7_1_21/src
export CMSSW_PUMixing=${PWD}/CMSSW_8_0_3_patch2/src
export CMSSW_AODSIM=${PWD}/CMSSW_8_0_3_patch2/src
export CMSSW_MINIAODSIM=${PWD}/CMSSW_8_0_5_patch1/src

export PYTHONPATH=${PYTHONPATH}:${PWD}
export PYTHONPATH=${PYTHONPATH}:${PWD}/python
export PYTHONPATH=${PYTHONPATH}:${PWD}/Step3-PUMixing
