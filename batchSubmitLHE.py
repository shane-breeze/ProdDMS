#!/usr/bin/env python
import sys
import optparse
import os

#_____________________________________________________________________________||
def parseArgs():
    parser = optparse.OptionParser()
    parser.add_option("--maxEvents",type=int,default=300000,
            help="Number of events to run over with the LHE step")
    parser.add_option("--nJobs",type=int,default=750,
            help="Number of jobs to submit")
    return parser.parse_args()

#_____________________________________________________________________________||
def defaultCommands(inputFile, maxEvents, nJobs, outDir):
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    jobEvents = maxEvents/nJobs
    finalEvent = maxEvents - jobEvents*nJobs

    default =  "#!/bin/bash\n"
    default += "export OUTDIR={0}\n".format(outDir)
    default += "export GRIDPACK={0}\n".format(inputFile)
    default += "export JOBSEED=$(expr ${SGE_TASK_ID} - 1)\n"
    default += "mkdir -p $OUTDIR\n"
    default += "cd $OUTDIR\n"
    default += "source /vols/grid/cms/setup.sh\n"
    default += "export SCRAM_ARCH=slc6_amd64_gcc530\n"
    default += "eval `scramv1 runtime -sh`\n"
    if finalEvent != 0:
        default += "if [ ${SGE_TASK_ID} != ${SGE_TASK_LAST} ]; then\n"
        default += "    ../../../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED\n"\
                .format(jobEvents)
        default += "else\n"
        default += "    ../../../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED"\
                .format(finalEvent+jobEvents)
    else:
        default += "../../../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED"\
                .format(jobEvents)
    return default

#_____________________________________________________________________________||
def batchSubmitLHE(inputFile, maxEvents, nJobs):
    shellPath = "submitScript_"+inputFile.split('/')[-1].replace("_tarball.tar.gz","")
    if not 'WORKDIR' in os.environ:
        raise RuntimeError, "WORKDIR environment variable is not set"
    outDir = os.path.join(os.environ['WORKDIR'],
            "CMSSW_7_1_21/src",
            "ProdDMS/StepLHE/test")
    shellPath = os.path.join(outDir, shellPath)
    lheDir = shellPath.replace("submitScript","lheFiles")
    shellPath += ".sh"

    shellScript = defaultCommands(inputFile, maxEvents, nJobs, lheDir)
    shellFile = open(shellPath,'w')
    shellFile.write(shellScript)
    shellFile.close()

    command = " ".join(["chmod","+x",shellPath])
    os.system(command)
    command = " ".join(["qsub","-q","hep.q","-l","h_rt=3:0:0","-t","1-{0}:1".format(nJobs),shellPath])
    os.system(command)

    print "Shell script:\n\t", shellPath
    print "Outdir:\n\t", lheDir

#_____________________________________________________________________________||
if __name__ == "__main__":
    options,_ = parseArgs()
    if len(sys.argv) < 2:
        raise RuntimeError, "Please provide the input gridpack"
    if not os.path.exists(sys.argv[1]):
        raise RuntimeError, "Could not find "+sys.argv[1]
    batchSubmitLHE(sys.argv[1], options.maxEvents, options.nJobs)
