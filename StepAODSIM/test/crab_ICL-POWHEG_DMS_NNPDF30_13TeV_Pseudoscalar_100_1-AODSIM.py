from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'NNPDF30_13TeV_Pseudoscalar_100_1-AODSIM'
config.General.workArea        = 'ICL-POWHEG_DMS'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'AODSIM_step2_cfg.py'
config.JobType.outputFiles = ['ICL-RunIISpring16DR80-01180.root',]

config.Data.inputDataset         = '/NNPDF30_13TeV_Pseudoscalar_100_1-LHE/sbreeze-ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_100_1-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-GEN-SIM-RAW-f224a7ed86ef559783ccfee162c85c5f/USER' # change inputDataset
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_100_1-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-AODSIM'

config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'
