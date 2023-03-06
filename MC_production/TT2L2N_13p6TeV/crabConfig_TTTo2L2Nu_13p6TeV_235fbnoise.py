from CRABClient.UserUtilities import config

config = config()

## General settings
config.General.requestName = 'dvalsecc_TT2L2Nu_13p5TeV_EcalNoise235fb'
config.General.transferOutputs = True
config.General.transferLogs = False
## PrivateMC type with a fake miniAOD step to circunvent crab requests (official data-tier for PrivateMC)
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'sim_digi_premix_step_fake.py'
config.JobType.pyCfgParams = ['nThreads=4','outputName=output.root']
## To be executed on node with Arguments
config.JobType.scriptExe   = 'scriptExe.sh'
config.JobType.scriptArgs  = ['nEvents=200','nThreads=4','outputName=output.root']
config.JobType.inputFiles  = ['scriptExe.sh','gen_step.py','pileup.py', "sim_digi_premix_step.py"]
## Output file to be collected
config.JobType.outputFiles = ["output.root"]
config.JobType.disableAutomaticOutputCollection = True
## Memory, cores, cmssw
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 5500
config.JobType.numCores    = 4

config.JobType.sendPythonFolder = True
## Data
config.Data.splitting   = 'EventBased'
config.Data.unitsPerJob = 200
config.Data.totalUnits  = 300000

config.Data.outputPrimaryDataset = 'TTTo2L2Nu_powheg_pythia8_13p6TeV_PremixRun3PU40'
config.Data.publication   = True
config.Data.publishDBS           = 'phys03'
#config.Data.ignoreLocality       = True
config.Data.outputDatasetTag     = '126X_mcRun3_2021_realistic_v9_Ecal235fbNoise'

## Site
config.Site.storageSite = 'T2_CH_CSCS'

