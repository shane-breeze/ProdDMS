################################################################################
# Config file for the LHE step                                                 #
#                                                                              #
# 1) If produceLHE is False, will use the lheFile parameter and run the LHE to #
#    EDM conversion in one job. Need to generate the LHE files separately      #
# 2) If produceLHE is True, will use the gridPack parameter and produce the    #
#    files and handle the LHE to EDM conversion in a single job                #
#                                                                              #
################################################################################

from python.config import config 

testPath = 'Step1-LHE/test/'
crabPath = 'Step1-LHE/crabLogs/'

#_Axial_1750_10_______________________________________________________________||
av_1750_10_cfg = config()
av_1750_10_cfg.produceLHE     = False
av_1750_10_cfg.testEvents     = 10
av_1750_10_cfg.lheFile        = '/store/user/sbreeze/LHE-files/cmsgrid_POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10.lhe'
av_1750_10_cfg.gridPack       = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/Dark_Matter/DMV_NNPDF30_13TeV_Axial_0p25/v2/POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10_tarball.tar.gz'
av_1750_10_cfg.outputRootFile = testPath+'ICL-Axial_1750_10-LHE.root'
av_1750_10_cfg.xmlFile        = testPath+'ICL-Axial_1750_10-LHEtest.xml'

av_1750_10_cfg.requestName          = 'NNPDF30_13TeV_Axial_1750_10-LHE'
av_1750_10_cfg.workArea             = crabPath
av_1750_10_cfg.maxEvents            = 300000
av_1750_10_cfg.outputPrimaryDataset = 'NNPDF30_13TeV_Axial_1750_10-LHE'
av_1750_10_cfg.outputDatasetTag     = 'ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10-LHE'

#_test________________________________________________________________________||
test_cfg = config()
test_cfg.produceLHE     = False
test_cfg.testEvents     = 10
test_cfg.lheFile        = '/store/user/sbreeze/LHE-files/cmsgrid_POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10.lhe'
test_cfg.gridPack       = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/Dark_Matter/DMV_NNPDF30_13TeV_Axial_0p25/v2/POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10_tarball.tar.gz'
test_cfg.outputRootFile = testPath+'ICL-Axial_1750_10-LHE.root'
test_cfg.xmlFile        = testPath+'ICL-Axial_1750_10-LHEtest.xml'

test_cfg.requestName          = 'test_Axial_1750_10-LHE'
test_cfg.workArea             = crabPath
test_cfg.maxEvents            = 10
test_cfg.outputPrimaryDataset = 'test_Axial_1750_10-LHE'
test_cfg.outputDatasetTag     = 'test_Axial_1750_10-LHE'

#_____________________________________________________________________________||
inputConfig = test_cfg
