from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

from inputConfig_AODSIM import inputConfig

config.General.requestName     = inputConfig.requestName
config.General.workArea        = inputConfig.workArea
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'Step4-AODSIM/cmsRunAOD_cfg.py'
config.JobType.outputFiles = [inputConfig.outputRootFile,]

config.Data.inputDataset         = inputConfig.inputDataset
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = inputConfig.unitsPerJob
config.Data.totalUnits           = inputConfig.totalUnits
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = inputConfig.outputDatasetTag

config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'
