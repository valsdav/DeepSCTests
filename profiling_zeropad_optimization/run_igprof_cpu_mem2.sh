#!/bin/sh -e 

echo "Running $1"

BASEDIR=igprof_run_$1_correct
mkdir $BASEDIR
cd $BASEDIR 

echo "step3 IgProf pp"
n=0
until [ "$n" -ge 5 ]
do
   echo "attempt $n"
   igprof -d -pp -z -o step3_igprofCPU.gz -t cmsRun cmsRun ../$1.py inputFile=file:$2 &> step3_igprof_cpu.txt && break
   n=$((n+1))
done

mv IgProf.1.gz step3_igprofCPU.1.gz
mv IgProf.50.gz step3_igprofCPU.50.gz
mv IgProf.99.gz step3_igprofCPU.99.gz

echo "step3 IgProf mp"
n=0
until [ "$n" -ge 5 ]
do
   echo "attempt $n"
   igprof -d -mp -z -o step3_igprofMEM.gz -t cmsRunGlibC cmsRunGlibC ../$1.py inputFile=file:$2 &> step3_igprof_mem.txt && break
   n=$((n+1))
done

mv IgProf.1.gz step3_igprofMEM.1.gz
mv IgProf.50.gz step3_igprofMEM.50.gz
mv IgProf.99.gz step3_igprofMEM.99.gz

