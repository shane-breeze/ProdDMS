################################################################################
# Config file for the PU Mixing step                                           #
#                                                                              #
################################################################################

from python.config import config 

testPath = 'Step3-PUMixing/test/'
crabPath = 'Step3-PUMixing/crabLogs/'

#_Axial_1750_400______________________________________________________________||
av_1750_400_cfg = config()
av_1750_400_cfg.testEvents       = 10
av_1750_400_cfg.testInputDataset = '/store/user/sbreeze/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-GEN-SIM/160816_154431/0000/ICL-RunIISummer15GS-06337_1.root'
av_1750_400_cfg.xmlFile          = testPath+'ICL-Axial_1750_400-PUMixingtest.xml'

av_1750_400_cfg.inputDataset     = '/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/sbreeze-ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-GEN-SIM-RAW-f224a7ed86ef559783ccfee162c85c5f/USER'
av_1750_400_cfg.requestName      = 'NNPDF30_13TeV_Axial_1750_400-PUMixing'
av_1750_400_cfg.workArea         = crabPath
av_1750_400_cfg.unitsPerJob      = 400
av_1750_400_cfg.totalUnits       = -1
av_1750_400_cfg.outputRootFile   = 'ICL-Axial_1750_400-PUMixing.root'
av_1750_400_cfg.outputDatasetTag = 'ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-PUMixing'

#_test________________________________________________________________________||
test_cfg = config()
test_cfg.testEvents       = 1
test_cfg.testInputDataset = '/store/user/sbreeze/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-GEN-SIM/160816_154431/0000/ICL-RunIISummer15GS-06337_1.root'
test_cfg.xmlFile          = testPath+'ICL-Axial_1750_400-PUMixingtest.xml'

test_cfg.inputDataset     = '/DMV_NNPDF30_Axial_Mphi-1750_Mchi-400_gSM-0p25_gDM-1p0_v2_13TeV-powheg/sbreeze-ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_400-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-GEN-SIM-RAW-f224a7ed86ef559783ccfee162c85c5f/USER'
test_cfg.requestName      = 'test_Axial_1750_400-PUMixing'
test_cfg.workArea         = crabPath
test_cfg.unitsPerJob      = 10
test_cfg.totalUnits       = 20
test_cfg.outputRootFile   = 'ICL-Axial_1750_400-PUMixing.root'
test_cfg.outputDatasetTag = 'test_Axial_1750_400_PUMix'

#_____________________________________________________________________________||
inputConfig = test_cfg
