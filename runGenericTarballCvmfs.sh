#!/bin/bash

#script to run generic lhe generation tarballs
#kept as simply as possible to minimize need
#to update the cmssw release
#(all the logic goes in the run script inside the tarball
# on frontier)
#J.Bendavid

#exit on first error
set -e

echo "   ______________________________________     "
echo "         Running Generic Tarball/Gridpack     "
echo "   ______________________________________     "

path=${1}
echo "gridpack tarball path = $path"

nevt=${2}
echo "%MSG-MG5 number of events requested = $nevt"

rnum=${3}
echo "%MSG-MG5 random seed used for the run = $rnum"

LHEWORKDIR=`pwd`
LHEDIR=lheevent_${nevt}_${rnum}

if [[ -d $LHEDIR ]]
    then
    echo 'lheevent directory found'
    echo 'Setting up the environment'
    rm -rf $LHEDIR
fi
mkdir $LHEDIR; cd $LHEDIR

#untar the tarball directly from cvmfs
tar -xaf ${path} 

#uncomment RNG seed and rand1/rand2
sed -i 's/#iseed/iseed/' powheg.input
sed -i 's/#rand1/rand1/' powheg.input
sed -i 's/#rand2/rand2/' powheg.input
sed -i "s/rand1\s\+[0-9]\+/rand1   456/" powheg.input
sed -i "s/rand2\s\+[0-9]\+/rand2   123/" powheg.input

#generate events (call for 1 core always for now until hooks to set number of cores are implemented upstream)
./runcmsgrid.sh $nevt $rnum 1

mv cmsgrid_final.lhe $LHEWORKDIR/cmsgrid_final_nevt-${nevt}_rnum-${rnum}.lhe

#clean up output directory
rm -rf $LHEDIR

cd $LHEWORKDIR

exit 0
