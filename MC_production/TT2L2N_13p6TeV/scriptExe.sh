#!/bin/bash                                                                                                                                                                                       
set -e
BASE=$PWD
RELEASE_BASE=$CMSSW_BASE

export SCRAM_ARCH=slc7_amd64_gcc10
source /cvmfs/cms.cern.ch/cmsset_default.sh

echo "setting up CMSSW environment"
cd $RELEASE_BASE
eval `scram runtime -sh`
cd $BASE

echo "cmsRun -e -j FrameworkJobReport.xml gen_step.py jobNum="$1" "$2" "$3" outputName=genStep.root" $5
cmsRun -e -j FrameworkJobReport.xml gen_step.py jobNum=$1 $2 $3 outputName=genStep.root $5

echo "cmsRun -e -j FrameworkJobReport.xml sim_digi_premix_step.py "$3" inputName=genStep.root outputName=output.root"
cmsRun -e -j FrameworkJobReport.xml sim_digi_premix_step.py $3 inputName=genStep.root outputName=output.root
rm genStep*.root

# echo "cmsRun -e -j FrameworkJobReport.xml digi_raw_step.py "$3" inputName=simStep.root outputName=digirawStep.root"
# cmsRun -e -j FrameworkJobReport.xml digi_raw_step.py $3 inputName=simStep.root outputName=digirawStep.root
# rm simStep*.root

# scram p CMSSW CMSSW_10_2_16_UL
# cd CMSSW_10_2_16_UL/srco
# eval `scram runtime -sh`
# cd ../../

# echo "cmsRun -e -j FrameworkJobReport.xml hlt_step.py "$3" inputName=digirawStep.root outputName=hltStep.root"
# cmsRun -e -j FrameworkJobReport.xml hlt_step.py $3 inputName=digirawStep.root outputName=hltStep.root
# rm digirawStep.root

# cd $RELEASE_BASE
# eval `scram runtime -sh`
# cd $BASE

# echo "cmsRun -e -j FrameworkJobReport.xml reco_step.py "$3" inputName=hltStep.root outputName=recoStep.root"
# cmsRun -e -j FrameworkJobReport.xml reco_step.py $3 inputName=hltStep.root outputName=recoStep.root
# rm hltStep.root

# echo "cmsRun -e -j FrameworkJobReport.xml miniaod_step.py "$3" inputName=recoStep.root "$4
# cmsRun -e -j FrameworkJobReport.xml miniaod_step.py $3 inputName=recoStep.root $4
# rm recoStep.root
