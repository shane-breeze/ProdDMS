#!/usr/bin/env python
import sys
import optparse
import os
import shutil

#_____________________________________________________________________________||
def parseArgs():
    parser = optparse.OptionParser()
    parser.add_option("--maxEvents",type=int,default=300000,
            help="Number of events to run over with the LHE step")
    parser.add_option("--nJobs",type=int,default=750,
            help="Number of jobs to submit")
    parser.add_option("-o","--outDir",type='string',default=".",
            help="Output directory of LHE files")
    parser.add_option("-t","--time",type='string',default="3:0:0",
            help="The time options for qsub")
    return parser.parse_args()

#_____________________________________________________________________________||
def defaultCommands(inputFile, maxEvents, nJobs, outDir):
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    if not "CMSSW_BASE" in os.environ:
        raise RuntimeError, "CMSSW_BASE not defined. Have you done cmsenv?"
    cmsswDir = os.path.join(os.environ['CMSSW_BASE'], "src")

    jobEvents = maxEvents/nJobs
    finalEvent = maxEvents - jobEvents*nJobs

    default =  "#!/bin/bash\n\n"

    default += "#_SET_ENVIRONMENT VARIABLES___________________________________________________||\n"
    default += "export OUTDIR={0}\n".format(outDir)
    default += "export GRIDPACK={0}\n".format(inputFile)
    default += "export CMSSW_DIR={0}\n".format(cmsswDir)
    default += "export JOBSEED=$(expr ${SGE_TASK_ID} - 1)\n\n"

    default += "#_SETUP_CMSSW_ENVIRONMENT_____________________________________________________||\n"
    default += "cd $CMSSW_DIR\n"
    default += "source /vols/grid/cms/setup.sh\n"
    default += "export SCRAM_ARCH=slc6_amd64_gcc530\n"
    default += "eval `scramv1 runtime -sh`\n\n"

    default += "#_RUN_SCRIPT__________________________________________________________________||\n"
    default += "mkdir -p $OUTDIR\n"
    default += "cd $OUTDIR\n"

    if finalEvent != 0:
        default += "if [ ${SGE_TASK_ID} != ${SGE_TASK_LAST} ]; then\n"
        default += "    ../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED\n"\
                .format(jobEvents)
        default += "else\n"
        default += "    ../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED"\
                .format(finalEvent+jobEvents)
    else:
        default += "../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED"\
                .format(jobEvents)
    return default

#_____________________________________________________________________________||
def batchSubmitLHE(inputFile, maxEvents, nJobs, outDir, time):
    shellPath = "submitScript_"+\
            inputFile.split('/')[-1].replace("_tarball.tar.gz","")

    if outDir == None:
        if not 'WORKDIR' in os.environ:
            raise RuntimeError, "WORKDIR environment variable is not set"
        outDir = os.path.join(os.environ['WORKDIR'],
                "CMSSW_7_1_21/src",
                "ProdDMS/StepLHE/test")
    else:
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        shutil.copyfile("runGenericTarballCvmfs.sh",
                os.path.join(outDir,"runGenericTarballCvmfs.sh"))
    os.system("chmod +x {0}".format(os.path.join(outDir,"runGenericTarballCvmfs.sh")))

    shellPath = os.path.join(outDir, shellPath)
    lheDir = shellPath.replace("submitScript","lheFiles")
    shellPath += ".sh"

    shellScript = defaultCommands(inputFile, maxEvents, nJobs, lheDir)
    shellFile = open(shellPath,'w')
    shellFile.write(shellScript)
    shellFile.close()

    command = " ".join(["chmod","+x",shellPath])
    os.system(command)
    command = " ".join(["qsub","-q","hep.q","-l","h_rt={0}".format(time),"-t",
        "1-{0}:1".format(nJobs),shellPath])
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
    batchSubmitLHE(sys.argv[1], 
            options.maxEvents, 
            options.nJobs, 
            options.outDir,
            options.time)
