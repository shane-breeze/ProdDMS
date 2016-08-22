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

#_Axial_1750_10_______________________________________________________________||
av_1750_10_cfg = config()
av_1750_10_cfg.produceLHE     = False
av_1750_10_cfg.testEvents     = 100
av_1750_10_cfg.lheFile        = '/store/user/sbreeze/LHE-files/cmsgrid_POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10.lhe'
av_1750_10_cfg.gridPack       = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/Dark_Matter/DMV_NNPDF30_13TeV_Axial_0p25/v2/POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10_tarball.tar.gz'
av_1750_10_cfg.outputRootFile = 'Step1-LHE/test/ICL-Axial_1750_10-LHE.root'
av_1750_10_cfg.xmlFile        = 'Step1-LHE/test/ICL-Axial_1750_10-LHEtest.xml'

av_1750_10_cfg.requestName          = 'NNPDF30_13TeV_Axial_1750_10-LHE'
av_1750_10_cfg.workArea             = 'crab_Axial_1750_10-LHE'
av_1750_10_cfg.maxEvents            = 300000
av_1750_10_cfg.outputPrimaryDataset = 'NNPDF30_13TeV_Axial_1750_10-LHE'
av_1750_10_cfg.outputDatasetTag     = 'ICL-POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10-LHE'

#_____________________________________________________________________________||
inputConfig = av_1750_10_cfg
