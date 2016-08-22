# Modified Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/IC-RunIIWinter15wmLHE-02602-fragment.py --filein file:data/lheFiles_POWHEG_DMV_NNPDF30_13TeV_Axial_1750_10/cmsgrid_final_nevt-400_rnum-0.lhe --fileout file:IC-RunIIWinter15wmLHE-02602.root --mc --eventcontent LHE --datatier LHE --conditions MCRUN2_71_V1::All --step LHE --python_filename testLHE2EDM.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
import FWCore.ParameterSet.Config as cms
from inputConfig_LHE import inputConfig

process = cms.Process('LHE')

#_import_of_standard_configurations___________________________________________||
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(inputConfig.testEvents)
)

#_Input_source________________________________________________________________||
if not inputConfig.produceLHE:
    process.source = cms.Source("LHESource",
        fileNames = cms.untracked.vstring(inputConfig.lheFile)
    )
else:
    process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

#_Output_definition___________________________________________________________||
import os
outDir = "/".join(inputConfig.outputRootFile.split('/')[:-1])
if not os.path.exists(outDir):
    os.makedirs(outDir)

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.LHEEventContent.outputCommands,
    fileName = cms.untracked.string('file:{0}'.format(inputConfig.outputRootFile)),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('LHE')
    )
)

process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(inputConfig.testEvents),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    args = cms.vstring(inputConfig.gridPack)
)

#_Other_statements____________________________________________________________||
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

#_Path_and_EndPath_definitions________________________________________________||
process.lhe_step = cms.Path(process.externalLHEProducer)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

#_Schedule_definition_________________________________________________________||
if inputConfig.produceLHE:
    process.schedule = cms.Schedule(process.lhe_step,process.endjob_step,process.LHEoutput_step)
else:
    process.schedule = cms.Schedule(process.endjob_step,process.LHEoutput_step)

#_Automatic_addition_of_the_customisation_function_from_______________________||
#_Configuration.DataProcessing.Utils__________________________________________||
from Configuration.DataProcessing.Utils import addMonitoring 

#_call_to_customisation_function_addMonitoring_imported_from__________________||
#_Configuration.DataProcessing.Utils__________________________________________||
process = addMonitoring(process)

#_End_of_customisation_functions______________________________________________||
