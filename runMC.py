#!/usr/bin/env python
import optparse
import subprocess
import os
from python.config import config

from inputConfig_LHE        import inputConfig as lhe_cfg
from inputConfig_GENSIM     import inputConfig as gen_cfg
from inputConfig_PUMixing   import inputConfig as pum_cfg
from inputConfig_AODSIM     import inputConfig as aod_cfg
from inputConfig_MINIAODSIM import inputConfig as min_cfg

#_____________________________________________________________________________||
def parseArgs():
    parser = optparse.OptionParser()
    parser.add_option("--step",type='string',
            help="MC step to run: LHE, GENSIM, PUMixing, AODSIM or MINIAODSIM")
    parser.add_option("--test",action='store_true',default=False,
            help="Run a test job")
    parser.add_option("--status",action='store_true',default=False,
            help="Report the status of the CRAB jobs")
    parser.add_option("--kill",action='store_true',default=False,
            help="Kill the CRAB jobs")
    return parser.parse_args()

#_____________________________________________________________________________||
def makeTestDir(test, testDir):
    if test:
        if not os.path.exists(testDir):
            os.makedirs(testDir)
        pass
    pass

#_____________________________________________________________________________||
def moveTestFile(test, testFile, testDir):
    if test:
        command = ["mv", testFile, os.path.join(testDir, testFile)]
        subprocess.call(command)
    pass

#_____________________________________________________________________________||
def checkCMSSW(cmsswName):
    if cmsswName not in os.environ["CMSSW_BASE"]:
        raise RuntimeError, "Please setup the correct CMSSW release: "+cmsswName
    pass

#_____________________________________________________________________________||
def mcStep(cfg, cfgFile, crabFile, test, status, kill):
    command = []
    if status:
        crabOutput = os.path.join(cfg.workArea, "crab_"+cfg.requestName)
        if not os.path.exists(crabOutput):
            raise RuntimeError, "Could not find crab output folder "+crabOutput
        command = ["crab","status","-d",crabOutput]
    elif kill:
        crabOutput = os.path.join(cfg.workArea, "crab_"+cfg.requestName)
        if not os.path.exists(crabOutput):
            raise RuntimeError, "Could not find crab output folder "+crabOutput
        command = ["crab","kill","-d",crabOutput]
    elif test:
        xmlFile = cfg.xmlFile
        command = ["cmsRun","-e","-j",xmlFile,cfgFile]
    else:
        command = ["crab","submit","-c",crabFile]
    subprocess.call(command)

    if test:
        checkTest = ["Scripts/testRun.sh",xmlFile]
        subprocess.call(checkTest)
    pass

#_____________________________________________________________________________||
def runMC(step, test, status, kill):
    if step.lower() == "lhe":
        checkCMSSW("CMSSW_7_1_21")
        mcStep(lhe_cfg, "Step1-LHE/cmsRunLHE_cfg.py", "Step1-LHE/crabLHE_cfg.py", test, status, kill)
        pass
    elif step.lower() == "gensim":
        checkCMSSW("CMSSW_7_1_21")
        mcStep(gen_cfg, "Step2-GENSIM/cmsRunGENSIM_cfg.py", "Step2-GENSIM/crabGENSIM_cfg.py", test, status, kill)
        pass
    elif step.lower() == "pumixing":
        checkCMSSW("CMSSW_8_0_3_patch2")
        makeTestDir(test, "/".join(pum_cfg.xmlFile.split('/')[:-1]))
        mcStep(pum_cfg, "Step3-PUMixing/cmsRunPU_cfg.py", "Step3-PUMixing/crabPU_cfg.py", test, status, kill)
        moveTestFile(test, pum_cfg.outputRootFile, "/".join(pum_cfg.xmlFile.split('/')[:-1]))
        pass
    elif step.lower() == "aodsim":
        checkCMSSW("CMSSW_8_0_3_patch2")
        makeTestDir(test, "/".join(aod_cfg.xmlFile.split('/')[:-1]))
        mcStep(aod_cfg, "Step4-AODSIM/cmsRunAOD_cfg.py", "Step4-AODSIM/crabAOD_cfg.py", test, status, kill)
        moveTestFile(test, aod_cfg.outputRootFile, "/".join(aod_cfg.xmlFile.split('/')[:-1]))
        moveTestFile(test, aod_cfg.outputRootFile.replace('.root','_inDQM.root'), "/".join(aod_cfg.xmlFile.split('/')[:-1]))
        pass
    elif step.lower() == "miniaodsim":
        checkCMSSW("CMSSW_8_0_5_patch1")
        makeTestDir(test, "/".join(min_cfg.xmlFile.split('/')[:-1]))
        mcStep(min_cfg, "Step5-MINIAODSIM/cmsRunMINIAOD_cfg.py", "Step5-MINIAODSIM/crabMINIAOD_cfg.py", test, status, kill)
        moveTestFile(test, min_cfg.outputRootFile, "/".join(min_cfg.xmlFile.split('/')[:-1]))
        pass
    else:
        raise RuntimeError, "step must be one of: LHE, GENSIM, PUMixing, AODSIM or MINIAODSIM"
        pass
    pass

#_____________________________________________________________________________||
if __name__ == "__main__":
    options,_ = parseArgs()
    if os.environ["PWD"]+":" not in os.environ["PYTHONPATH"]:
        raise RuntimeError, "Please source the setup file"
    if options.step == None:
        raise RuntimeError, "Please specify the MC step to run (\"--step\")"
    if options.test and options.status:
        raise RuntimeError, "Please call either test or status, not both"
    if options.status and options.kill:
        raise RuntimeError, "Please call either status or kill, not both"
    if options.kill and options.test:
        raise RuntimeError, "Please call either kill or test, not both"
    runMC(options.step, options.test, options.status, options.kill)
