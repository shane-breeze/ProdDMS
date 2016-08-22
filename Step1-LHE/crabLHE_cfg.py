from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

from inputConfig_LHE import inputConfig

config.General.requestName     = inputConfig.requestName
config.General.workArea        = inputConfig.workArea
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'Step1-LHE/cmsRunLHE_cfg.py'

config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = inputConfig.maxEvents
config.Data.totalUnits           = inputConfig.maxEvents
config.Data.publication          = True
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outputPrimaryDataset = inputConfig.outputPrimaryDataset
config.Data.outputDatasetTag     = inputConfig.outputDatasetTag
if inputConfig.produceLHE:
    config.Data.inputDBS         = 'global'

config.Site.whitelist   = ['T2_UK_London_IC']
config.Site.storageSite = 'T2_UK_London_IC'
if not inputConfig.produceLHE:
    config.Site.blacklist   = ['T2_UK_London_Brunel']
