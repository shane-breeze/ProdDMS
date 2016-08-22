# Modified auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --filein file:IC-RunIISpring16DR80-01180_step1.root --fileout file:IC-RunIISpring16DR80-01180.root --mc --eventcontent RAWAODSIM,DQM --runUnscheduled --datatier RAWAODSIM,DQMIO --conditions 80X_mcRun2_asymptotic_2016_v3 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --era Run2_25ns --python_filename IC-RunIISpring16DR80-01180_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 102
import FWCore.ParameterSet.Config as cms
from inputConfig_AODSIM import inputConfig

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_25ns)

#_import_of_standard_configurations___________________________________________||
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(inputConfig.testEvents)
)

#_Input_source________________________________________________________________||
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(inputConfig.testInputDataset),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

#_Production_Info_____________________________________________________________||
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:{0}'.format(inputConfig.testEvents)),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

#_Output_definition___________________________________________________________||

process.RAWAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RAWAODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:{0}'.format(inputConfig.outputRootFile)),
    outputCommands = process.RAWAODSIMEventContent.outputCommands
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:{0}'.format(inputConfig.outputRootFile.replace('.root','_inDQM.root'))),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

#_Additional_output_definition________________________________________________||

#_Other_statements____________________________________________________________||
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_v3', '')

#_Path_and_EndPath_definitions________________________________________________||
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.dqmoffline_step = cms.Path(process.DQMOfflinePOGMC)
process.dqmofflineOnPAT_step = cms.Path(process.DQMOfflinePOGMC)
process.RAWAODSIMoutput_step = cms.EndPath(process.RAWAODSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

#_Schedule_definition_________________________________________________________||
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.eventinterpretaion_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.RAWAODSIMoutput_step,process.DQMoutput_step)

#_customisation_of_the_process._______________________________________________||

#_Automatic_addition_of_the_customisation_function_from_______________________||
#_Configuration.DataProcessing.Utils__________________________________________||
from Configuration.DataProcessing.Utils import addMonitoring 

#_call_to_customisation_function_addMonitoring_imported_from__________________||
#_Configuration.DataProcessing.Utils__________________________________________||
process = addMonitoring(process)

#_End_of_customisation_functions______________________________________________||
#_do_not_add_changes_to_your_config_after_this_point_(unless_you_know_what____||
#_you_are_doing)______________________________________________________________||
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

