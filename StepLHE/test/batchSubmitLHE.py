#!/usr/bin/env python
import sys
import optparse
import os
import shutil
import re
import glob
import subprocess

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
    parser.add_option("--resubmit",action='store_true',default=False,
            help="Resubmit failed jobs")
    return parser.parse_args()

#_____________________________________________________________________________||
def setupOutput(outDir):
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

#_____________________________________________________________________________||
def setupCommands(inputFile, cmsswDir, outDir):
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

    return default

#_____________________________________________________________________________||
def defaultCommands(inputFile, maxEvents, nJobs, outDir):
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    if not "CMSSW_BASE" in os.environ:
        raise RuntimeError, "CMSSW_BASE not defined. Have you done cmsenv?"
    cmsswDir = os.path.join(os.environ['CMSSW_BASE'], "src")

    jobEvents = maxEvents/nJobs
    finalEvent = maxEvents - jobEvents*nJobs

    default = setupCommands(inputFile, cmsswDir, outDir)
    if finalEvent != 0:
        default += "if [ ${SGE_TASK_ID} != ${SGE_TASK_LAST} ]; then\n"
        default += "    ../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED\n"\
                .format(jobEvents)
        default += "else\n"
        default += "    ../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED\n"\
                .format(finalEvent+jobEvents)
        default += "fi"
    else:
        default += "../runGenericTarballCvmfs.sh $GRIDPACK {0} $JOBSEED"\
                .format(jobEvents)
    return default

#_____________________________________________________________________________||
def resubmitCommands(inputFile, maxEvents, nJobs, outDir):
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    if not "CMSSW_BASE" in os.environ:
        raise RuntimeError, "CMSSW_BASE not defined. Have you done cmsenv?"
    cmsswDir = os.path.join(os.environ['CMSSW_BASE'], "src")

    jobEvents = maxEvents/nJobs
    finalEvent = maxEvents - jobEvents*nJobs

    default = setupCommands(inputFile, cmsswDir, outDir)

    totalJobs = 0
    for i in range(nJobs):
        nEvents = jobEvents
        if finalEvent != 0 and i == nJobs-1:
            nEvents = finalEvent+jobEvents
        lheFile = os.path.join(outDir, "cmsgrid_final_nevt-{0}_rnum-{1}.lhe"\
                .format(nEvents,i))
        if not isLheFileOK(lheFile):
            if totalJobs > 0: default += "el"
            totalJobs += 1
            default += "if [ ${SGE_TASK_ID} = "+"{0} ]; then\n".format(totalJobs)
            default += "    ../runGenericTarballCvmfs.sh $GRIDPACK {0} {1}\n"\
                    .format(nEvents, i)
        pass
    default += "fi"

    return default, totalJobs

#_____________________________________________________________________________||
def isLheFileOK(lheFile):
    if not os.path.exists(lheFile):
        return False

    # Get number of events
    if lheFile[-1] == '/':
        lheFile = lheFile[:-1]
    maxEvents = int(re.findall("(?<=nevt-)\d+",lheFile.split('/')[-1])[0])

    # Get number of "<event>"
    find = "<event>"
    procOut = subprocess.check_output("grep \"{0}\" {1}".format(find,lheFile),
            shell=True)
    startEventLength = len(procOut.splitlines())

    # Get number of "</event>"
    find = "</event>"
    procOut = subprocess.check_output("grep \"{0}\" {1}".format(find,lheFile),
            shell=True)
    endEventLength = len(procOut.splitlines())

    if startEventLength != endEventLength: return False
    if startEventLength < maxEvents: return False
    if endEventLength  < maxEvents: return False

    return True

#_____________________________________________________________________________||
def batchSubmitLHE(inputFile, maxEvents, nJobs, outDir, time, resubmit):
    setupOutput(outDir)

    shellPath = "submitScript_"+\
            inputFile.split('/')[-1].replace("_tarball.tar.gz","")
    shellPath = os.path.join(outDir, shellPath)
    lheDir = shellPath.replace("submitScript","lheFiles")
    shellPath += ".sh"

    totalJobs = nJobs
    if resubmit:
        if len(glob.glob(os.path.join(lheDir,"*.lhe"))) == 0:
            print "No LHE files found. Try running without --resubmit"; return
        shellScript, totalJobs = resubmitCommands(inputFile, maxEvents, nJobs, lheDir)
    else:
        shellScript = defaultCommands(inputFile, maxEvents, nJobs, lheDir)
    if totalJobs == 0:
        print "No jobs to submit"; return
    shellFile = open(shellPath,'w')
    shellFile.write(shellScript)
    shellFile.close()

    command = " ".join(["chmod","+x",shellPath])
    os.system(command)
    command = " ".join(["qsub","-q","hep.q","-l","h_rt={0}".format(time),"-t",
        "1-{0}:1".format(totalJobs),shellPath])
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
            options.time,
            options.resubmit)
