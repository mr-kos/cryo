FROM boinc/server_makeproject:4.0.1-b2d

COPY --chown=1000 config.xml $PROJECT_ROOT

COPY --chown=1000 create_jobs.sh $PROJECT_ROOT

COPY --chown=1000 work_unit_generator $PROJECT_ROOT

COPY --chown=1000 boinc2docker_out $PROJECT_ROOT/templates

COPY --chown=1000 cryo_assimilator $PROJECT_ROOT/bin

COPY --chown=1000 cryo_validator $PROJECT_ROOT/bin

COPY --chown=1000 true $PROJECT_ROOT/bin

COPY --chown=1000 cryo-client $PROJECT_ROOT/cryo-client

COPY --chown=1000 config_aux.xml $PROJECT_ROOT

RUN mkdir -m 777 $PROJECT_ROOT/tmp_models && mkdir -m 777 $PROJECT_ROOT/tmp_models/models && mkdir -m 777 $PROJECT_ROOT/tmp_models/logs

COPY --chown=1000 iter_num.txt $PROJECT_ROOT/tmp_models

COPY --chown=1000 max_iter.txt $PROJECT_ROOT/tmp_models

RUN chmod ugo+x $PROJECT_ROOT/work_unit_generator $PROJECT_ROOT/bin/cryo_assimilator $PROJECT_ROOT/bin/cryo_validator

RUN chmod ugo+wr $PROJECT_ROOT/download

