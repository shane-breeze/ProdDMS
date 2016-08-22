################################################################################
# Config file for the GENSIM step                                              #
#                                                                              #
################################################################################

from python.config import config 

testPath = 'Step2-GENSIM/test/'
crabPath = 'Step2-GENSIM/crabLogs/'

#_Axial_1750_10_______________________________________________________________||
av_1750_10_cfg = config()
av_1750_10_cfg.testEvents       = 10
av_1750_10_cfg.testInputDataset = '/store/user/sbreeze/NNPDF30_13TeV_Axial_1750_10-LHE/ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10-LHE/160818_030604/0000/IC-RunIIWinter15wmLHE-02602_1.root'
av_1750_10_cfg.outputRootFile   = testPath+'ICL-Axial_1750_10-GENSIM.root'
av_1750_10_cfg.xmlFile          = testPath+'ICL-Axial_1750_10-GENSIMtest.xml'

av_1750_10_cfg.privateLHE       = True
av_1750_10_cfg.inputDataset     = '/NNPDF30_13TeV_Axial_1750_10-LHE/sbreeze-ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10-LHE-f9b6814bcbabd1708b438956799ee060/USER'
av_1750_10_cfg.requestName      = 'NNPDF30_13TeV_Axial_1750_10-GENSIM'
av_1750_10_cfg.workArea         = crabPath
av_1750_10_cfg.unitsPerJob      = 400
av_1750_10_cfg.totalUnits       = -1
av_1750_10_cfg.outputDatasetTag = 'ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10-GENSIM'

#_test________________________________________________________________________||
test_cfg = config()
test_cfg = config()
test_cfg.testEvents       = 10
test_cfg.testInputDataset = '/store/user/sbreeze/NNPDF30_13TeV_Axial_1750_10-LHE/ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10-LHE/160818_030604/0000/IC-RunIIWinter15wmLHE-02602_1.root'
test_cfg.outputRootFile   = testPath+'ICL-Axial_1750_10-GENSIM.root'
test_cfg.xmlFile          = testPath+'ICL-Axial_1750_10-GENSIMtest.xml'

test_cfg.privateLHE       = True
test_cfg.inputDataset     = '/NNPDF30_13TeV_Axial_1750_10-LHE/sbreeze-ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10-LHE-f9b6814bcbabd1708b438956799ee060/USER'
test_cfg.requestName      = 'test_Axial_1750_10-GENSIM'
test_cfg.workArea         = crabPath
test_cfg.unitsPerJob      = 10
test_cfg.totalUnits       = 20
test_cfg.outputDatasetTag = 'test_Axial_1750_10-GENSIM'

#_____________________________________________________________________________||
inputConfig = test_cfg
