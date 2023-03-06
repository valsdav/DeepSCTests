# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring,Validation/RecoParticleFlow/customize_pfanalysis.customize_ecalclustering --datatier GEN-SIM-RAW --fileout file:PPS-Run3Winter22DRPremix-00052_0.root --pileup_input dbs:/Ne --conditions 122X_mcRun3_2021_realistic_v9 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2021 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --filein file:step1.root --datamix PreMix --era Run3 --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('nThreads', 1, VarParsing.multiplicity.singleton,VarParsing.varType.int,"nThreads")
options.register('inputName',  "genStep.root", VarParsing.multiplicity.singleton,VarParsing.varType.string,"inputName")
options.register('outputName', "simStep.root", VarParsing.multiplicity.singleton,VarParsing.varType.string,"outputName")
options.register('pileupName', "pileup.py", VarParsing.multiplicity.singleton,VarParsing.varType.string,"pileupName")
options.parseArguments()


from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2

process = cms.Process('HLT',Run3,premix_stage2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDM_cff')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)


process.source = cms.Source("PoolSource",
               fileNames = cms.untracked.vstring('file:'+options.inputName),
               secondaryFileNames = cms.untracked.vstring()
)


    # Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    inputCommands = cms.untracked.vstring(
        'keep *', 
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
        'drop *_genMetIC5GenJs_*_*'

    ),
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring("file:" + options.inputName)
                            
)



process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(options.nThreads),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--eventcontent nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:'+options.outputName),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements

# import random
# process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(options.seed1)
# random.seed(process.RandomNumberGeneratorService.generator.initialSeed.value())
# random.shuffle(process.mixData.input.fileNames)

# process.mixData.input.seed = cms.untracked.uint32(options.seed2)

from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, '122X_mcRun3_2021_realistic_v9', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '126X_mcRun3_2022_realistic_v2', '')
# Pileup premix
# Pileup mixing
import os,random
random.seed = os.urandom(1000)
puListFull = [];
with open(options.pileupName,'r') as pileup:
    for element in pileup:
        puListFull.append(element);
random.shuffle(puListFull)
process.mixData.input.fileNames = cms.untracked.vstring(puListFull)
           


# 235fb noise pedestals
process.myNoise = cms.ESSource("PoolDBESSource",
     connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
     toGet = cms.VPSet(
         cms.PSet(
             record = cms.string('EcalPedestalsRcd'),
             tag = cms.string('EcalPedestals_mid2021_235fb_mc')
         )
     )
)
process.es_prefer_pedestals = cms.ESPrefer("PoolDBESSource","myNoise")

process.my_laser = cms.ESSource("PoolDBESSource",
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
     toGet = cms.VPSet(
         cms.PSet(
             record = cms.string('EcalLaserAPDPNRatiosRcd'),
             tag = cms.string('EcalLaserAPDPNRatios_UL_2018_mc_3sigma_v2')
         )
     )
)
process.es_prefer_ecallaser = cms.ESPrefer("PoolDBESSource", "my_laser")




# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.PREMIXRAWoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from Validation.RecoParticleFlow.customize_pfanalysis
from Validation.RecoParticleFlow.customize_pfanalysis import customize_ecalclustering 

#call to customisation function customize_ecalclustering imported from Validation.RecoParticleFlow.customize_pfanalysis
process = customize_ecalclustering(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
