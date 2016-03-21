from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'NNPDF30_13TeV_Pseudoscalar_1000_50_v2'
config.General.workArea        = 'ICL-POWHEG_DMS'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'AODSIM_step1_cfg.py'
config.JobType.outputFiles = ['AODSIM_step1.root',]

config.Data.inputDataset         = '/NNPDF30_13TeV_Pseudoscalar_1000_50/pela-ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_1000_50_v2-GEN-SIM-dcabb2e2c5ba1f0553af7887c0a2de09/USER'
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 400
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_1000_50_v2-2015_25ns_Startup_PoissonOOTPU-GEN-SIM-RAW'

config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'
