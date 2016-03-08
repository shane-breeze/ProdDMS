# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM --fileout file:AODSIM_step1.root --pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM --mc --eventcontent RAWSIM --pileup 2015_25ns_Startup_PoissonOOTPU --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions MCRUN2_74_V9 --step DIGI,L1,DIGI2RAW,HLT:@frozen25ns --magField 38T_PostLS1 --python_filename AODSIM_step1_cfg.py --no_exec -n 500
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2015_25ns_Startup_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_25ns14e33_v1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/000AA699-2766-E511-9EAA-001E67505105.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/0AC2662A-3766-E511-938F-0022195578C8.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/2C6ECA62-3166-E511-9029-20CF3019DF19.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/42C1F230-3B66-E511-AA9F-001EC9ADC0F0.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/5C31B349-6E66-E511-964B-20CF305616FF.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/5CCB1301-2666-E511-AFCB-20CF3019DEF2.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/64C8C545-3E66-E511-AC8B-901B0E542962.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/88E906FD-2866-E511-914D-001E67505105.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/BC6C52DA-2066-E511-9B53-00259022516E.root', 
        '/store/mc/RunIIWinter15GS/DMS_NNPDF30_Scalar_Mphi-1000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-powheg/GEN-SIM/MCRUN2_71_V1-v1/30000/C613E552-2366-E511-8EDC-002590207E3C.root'),
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

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:500'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:AODSIM_step1.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
import ProdDMS.Filelist.MinBias_TuneCUETP8M1_13TeV_pythia8_RunIIWinter15GS_MCRUN2_71_V1_v1_GEN_SIM_cfi as pu_dataset
process.mix.input.fileNames = pu_dataset.readFiles

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

