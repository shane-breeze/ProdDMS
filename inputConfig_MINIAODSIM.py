################################################################################
# Config file for the MINIAODSIM step                                          #
#                                                                              #
################################################################################

from python.config import config 

testPath = 'Step5-MINIAODSIM/test/'
crabPath = 'Step5-MINIAODSIM/crabLogs/'

#_Axial_1750_400______________________________________________________________||
av_1750_400_cfg = config()
av_1750_400_cfg.testEvents       = 10
av_1750_400_cfg.testInputDataset = '/store/user/sbreeze/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-AODSIM/160818_005959/0000/ICL-RunIISpring16DR80-01180_1.root'
av_1750_400_cfg.xmlFile          = testPath+'ICL-Axial_1750_400-MINIAODSIMtest.xml'

av_1750_400_cfg.inputDataset     = '/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/sbreeze-ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-AODSIM-3289af86e5ac35ce101adf50782c2be1/USER'
av_1750_400_cfg.requestName      = 'NNPDF30_13TeV_Axial_1750_400-MINIAODSIM'
av_1750_400_cfg.workArea         = crabPath
av_1750_400_cfg.unitsPerJob      = 400
av_1750_400_cfg.totalUnits       = -1
av_1750_400_cfg.outputRootFile   = 'ICL-Axial_1750_400-MINIAODSIM.root'
av_1750_400_cfg.outputDatasetTag = 'ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-MINIAODSIM'

#_test________________________________________________________________________||
test_cfg = config()
test_cfg.testEvents       = 1
test_cfg.testInputDataset = '/store/user/sbreeze/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-AODSIM/160818_005959/0000/ICL-RunIISpring16DR80-01180_1.root'
test_cfg.xmlFile          = testPath+'ICL-Axial_1750_400-MINIAODSIMtest.xml'

test_cfg.inputDataset     = '/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/sbreeze-ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-AODSIM-3289af86e5ac35ce101adf50782c2be1/USER'
test_cfg.requestName      = 'test_Axial_1750_400-MINIAODSIM'
test_cfg.workArea         = crabPath
test_cfg.unitsPerJob      = 10
test_cfg.totalUnits       = 20
test_cfg.outputRootFile   = 'ICL-Axial_1750_400-MINIAODSIM.root'
test_cfg.outputDatasetTag = 'test_Axial_1750_400-MINIAODSIM'

#_____________________________________________________________________________||
inputConfig = test_cfg
