#!/bin/bash

i=1

while [ $i -le $1 ]
do

echo "Job № "$i

bin/boinc2docker_create_work.py --target_nresults 1 --target_user $i ozon67/cryo-client:test

let "i=i+1"

done
