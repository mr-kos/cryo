import os, sys

min_quorum = sys.argv[1]
target_nresults = sys.argv[2]

os.system('bin/boinc2docker_create_work.py --min_quorum {} --target_nresults {} ozon67/cryo-client:test'
            .format(min_quorum, target_nresults))
