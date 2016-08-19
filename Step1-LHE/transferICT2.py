#!/usr/bin/env python
import os
import sys
import glob
import subprocess
import optparse

#_____________________________________________________________________________||
def parseArgs():
    parser = optparse.OptionParser()
    parser.add_option("-v","--verbose",action="store_true",default=False,
            help="Print the commands that are run")
    return parser.parse_args()

#_____________________________________________________________________________||
def transferICT2(lheDir, username, verbose):
    if lheDir[-1] == '/': lheDir = lheDir[:-1]
    modelDir = lheDir.split('/')[-1].replace("lheFiles_","")

    # Create directories: /store/user/$USER/LHE-files/$MODEL
    ichost = "hep.ph.ic.ac.uk"
    icgrid = "gfe02.grid.{0}:8443".format(ichost)
    gridBasePath = "srm://{0}/srm/managerv2?SFN=/pnfs/{1}/data/cms//store/user/{2}"\
            .format(icgrid, ichost, username)
    # Command 1
    gridPath = os.path.join(gridBasePath, "LHE-files")
    if verbose: print " ".join(["srmmkdir",gridPath])
    subprocess.call(["srmmkdir",gridPath])
    # Command 2
    gridPath = os.path.join(gridPath, modelDir)
    if verbose: print " ".join(["srmmkdir",gridPath])
    subprocess.call(["srmmkdir",gridPath])

    # Copy commands
    lhePaths = glob.glob(os.path.join(lheDir,"*.lhe"))
    for path in lhePaths:
        if path[-1] == '/': path = path[:-1]
        filename = path.split('/')[-1]
        if verbose: print " ".join(["lcg-cp", path, os.path.join(gridPath, filename)])
        subprocess.call(["lcg-cp", path, os.path.join(gridPath, filename)])

#_____________________________________________________________________________||
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise RuntimeError, "Please provide the directory with the LHE files"+\
                " and your CERN GRID username"
    if not os.path.exists(sys.argv[1]):
        raise RuntimeError, "Could not find "+sys.argv[1]
    print "Using the username:", sys.argv[2]

    options, _ = parseArgs()
    transferICT2(sys.argv[1], sys.argv[2], options.verbose)
