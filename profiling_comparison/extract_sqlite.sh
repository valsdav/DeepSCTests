#!/bin/sh -e

FILE=step3_igprof

igprof-analyse --sqlite -v --demangle --gdb ${FILE}CPU.gz > ${FILE}CPU.txt
wget https://raw.githubusercontent.com/cms-sw/cms-bot/master/fix-igprof-sql.py

python fix-igprof-sql.py ${FILE}CPU.txt | sqlite3 ${FILE}CPU.sql3


igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE ${FILE}MEM.99.gz > ${FILE}MEM.99.txt
python fix-igprof-sql.py ${FILE}MEM.99.txt | sqlite3 ${FILE}MEM.99.sql3
