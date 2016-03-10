from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'NNPDF30_13TeV_Pseudoscalar_1000_50_v1'
config.General.workArea        = 'ICL-POWHEG_DMS'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'AODSIM_step2_cfg.py'
config.JobType.outputFiles = ['AODSIM_step2.root',]

config.Data.inputDataset         = '/NNPDF30_13TeV_Pseudoscalar_1000_50/pela-ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_1000_50_v1-2015_25ns_Startup_PoissonOOTPU-GEN-SIM-RAW-a545037419a6c9acf651cdcc5cc6843f/USER'
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_1000_50_v1-2015_25ns_Startup_PoissonOOTPU-AODSIM'

config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'
