#!/bin/bash

i=1

while [ $i -le $1 ]
do

echo "Job "$i

bin/boinc2docker_create_work.py --min_quorum 2 --target_nresults 2 ozon67/cryo-client:test

let "i=i+1"

done
