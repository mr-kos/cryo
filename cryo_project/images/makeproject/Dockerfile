FROM boinc/server_makeproject:4.0.1-b2d

COPY --chown=1000 config.xml $PROJECT_ROOT

COPY --chown=1000 create_jobs.sh $PROJECT_ROOT

COPY --chown=1000 boinc2docker_out $PROJECT_ROOT/templates

COPY --chown=1000 boinc2docker_assimilator $PROJECT_ROOT/bin
