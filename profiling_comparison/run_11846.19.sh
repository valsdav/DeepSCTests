
#11846.19 2021PU_ecalDeepSC+ZEE_14TeV_TuneCP5_GenSim+DigiPU+RecoNanoPU+HARVESTNanoPU [1]:

echo "step1 11846.19"
cmsDriver.py ZEE_14TeV_TuneCP5_cfi  -s GEN,SIM -n 100 --conditions auto:phase1_2021_realistic --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --datatier GEN-SIM --eventcontent FEVTDEBUG --geometry DB:Extended --era Run3 --relval 9000,100 

echo "step2 11846.19"
cmsDriver.py step2  -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2021 --conditions auto:phase1_2021_realistic --datatier GEN-SIM-DIGI-RAW -n 100 --eventcontent FEVTDEBUGHLT --geometry DB:Extended --era Run3 --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_12_0_0_pre4-120X_mcRun3_2021_realistic_v2-v1/GEN-SIM

echo "step3 11846.19"
cmsDriver.py step3  -s RAW2DIGI,L1Reco,RECO --conditions auto:phase1_2021_realistic --datatier AODSIM -n 100 --eventcontent FEVTDEBUGHLT,RECOSIM,MINIAODSIM,NANOEDMAODSIM,DQM --geometry DB:Extended --era Run3 --procModifiers run3_ecalclustering --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_12_0_0_pre4-120X_mcRun3_2021_realistic_v2-v1/GEN-SIM



echo "step3 IgProf conf"
cmsDriver.py step3  -s RAW2DIGI,L1Reco,RECO,RECOSIM --conditions auto:phase1_2021_realistic --datatier AODSIM, -n 100 --eventcontent RECOSIM --geometry DB:Extended --era Run3 --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_12_0_0_pre4-120X_mcRun3_2021_realistic_v2-v1/GEN-SIM --procModifiers run3_ecalclustering --customise Validation/Performance/IgProfInfo.customise --no_exec --python_filename step3_igprof.py &> step3_igprof_conf.txt



echo "step3 IgProf pp"
n=0
until [ "$n" -ge 5 ]
do
   echo "attempt $n"
   igprof -d -pp -z -o step3_igprofCPU.gz -t cmsRun cmsRun step3_igprof.py &> step3_igprof_cpu.txt && break
   n=$((n+1))
done

mv IgProf.1.gz step3_igprofCPU.1.gz
mv IgProf.200.gz step3_igprofCPU.200.gz
mv IgProf.399.gz step3_igprofCPU.399.gz

echo "step3 IgProf mp"
n=0
until [ "$n" -ge 5 ]
do
   echo "attempt $n"
   igprof -d -mp -z -o step3_igprofMEM.gz -t cmsRunGlibC cmsRunGlibC step3_igprof.py &> step3_igprof_mem.txt && break
   n=$((n+1))
done

mv IgProf.1.gz step3_igprofMEM.1.gz
mv IgProf.200.gz step3_igprofMEM.200.gz
mv IgProf.399.gz step3_igprofMEM.399.gz

