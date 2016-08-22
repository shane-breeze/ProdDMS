# Modified auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:IC-RunIISummer15GS-06337.root --fileout file:IC-RunIISpring16DR80-01180_step1.root --pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-MCRUN2_71_V1-v2/GEN-SIM --mc --eventcontent RAWSIM --pileup 2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_v3 --customise_commands process.simHcalDigis.markAndPass = cms.bool(True) --step DIGI,L1,DIGI2RAW,HLT:@frozen25ns --era Run2_25ns --python_filename IC-RunIISpring16DR80-01180_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 102
import FWCore.ParameterSet.Config as cms
from inputConfig_PUMixing import inputConfig

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_25ns)

#_import_of_standard_configurations___________________________________________||
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(inputConfig.testEvents)
)

#_Input_source________________________________________________________________||
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(inputConfig.testInputDataset),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

#_Production_Info_____________________________________________________________||
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:{0}'.format(inputConfig.testEvents)),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

#_Output_definition___________________________________________________________||
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:{0}'.format(inputConfig.outputRootFile)),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

#_Additional_output_definition________________________________________________||

#_Other_statements____________________________________________________________||
import MinBiasPuFileList_cfi as pu_dataset
process.mix.input.fileNames = pu_dataset.readFiles

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_v3', '')

#_Path_and_EndPath_definitions________________________________________________||
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

#_Schedule_definition_________________________________________________________||
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

#_customisation_of_the_process._______________________________________________||

#_Automatic_addition_of_the_customisation_function_from_______________________||
#_Configuration.DataProcessing.Utils__________________________________________||
from Configuration.DataProcessing.Utils import addMonitoring 

#_call_to_customisation_function_addMonitoring_imported_from__________________|| 
#_Configuration.DataProcessing.Utils__________________________________________|| 
process = addMonitoring(process)

#_Automatic_addition_of_the_customisation_function_from_______________________|| 
#_HLTrigger.Configuration.customizeHLTforMC___________________________________|| 
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#_call_to_customisation_function_customizeHLTforFullSim_imported_from_________|| 
#_HLTrigger.Configuration.customizeHLTforMC___________________________________||
process = customizeHLTforFullSim(process)

#_End_of_customisation_functions______________________________________________||

#_Customisation_from_command_line_____________________________________________||
process.simHcalDigis.markAndPass = cms.bool(True)

#_Customisation_from_command_line_____________________________________________||
process.simHcalDigis.markAndPass = cms.bool(True)
