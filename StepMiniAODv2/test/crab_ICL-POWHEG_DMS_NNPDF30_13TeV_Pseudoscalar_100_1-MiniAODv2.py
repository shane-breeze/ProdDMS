from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'NNPDF30_13TeV_Pseudoscalar_100_1-MINIAODv2'
config.General.workArea        = 'ICL-POWHEG_DMS'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'MiniAODv2_cfg.py'
config.JobType.outputFiles = ['ICL-RunIISpring16MiniAODv2-00842.root']

config.Data.inputDataset         = '/NNPDF30_13TeV_Pseudoscalar_100_1-LHE/sbreeze-ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_100_1-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-AODSIM-3289af86e5ac35ce101adf50782c2be1/USER' # Change inputDataset
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 400
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_100_1-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-MiniAODv2'

config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'
