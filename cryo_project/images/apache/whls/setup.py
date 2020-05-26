#!/usr/bin/env python3

print('Installing whls...')

import os

whls = ['numpy-1.18.4-cp35-cp35m-manylinux1_x86_64.whl',
	'pandas-0.25.1-cp35-cp35m-manylinux1_x86_64.whl',
	'scipy-1.4.1-cp35-cp35m-manylinux1_x86_64.whl',
	'tensorflow_estimator-2.2.0-py2.py3-none-any.whl',
	'grpcio-1.29.0-cp35-cp35m-manylinux2010_x86_64.whl',
	'protobuf-3.12.1-cp35-cp35m-manylinux1_x86_64.whl',
	'h5py-2.10.0-cp35-cp35m-manylinux1_x86_64.whl',
	'setuptools-46.4.0-py3-none-any.whl',
	'tensorboard_plugin_wit-1.6.0.post3-py3-none-any.whl',
	'certifi-2020.4.5.1-py2.py3-none-any.whl',
	'urllib3-1.25.9-py2.py3-none-any.whl',
	'pyasn1_modules-0.2.8-py2.py3-none-any.whl',
	'oauthlib-3.1.0-py2.py3-none-any.whl',
	'chardet-3.0.4-py2.py3-none-any.whl',
	'pytz-2020.1-py2.py3-none-any.whl',
	'python_dateutil-2.8.1-py2.py3-none-any.whl',
	'tensorflow_cpu-2.2.0-cp35-cp35m-manylinux2010_x86_64.whl',
	'tensorboard-2.2.1-py3-none-any.whl',
	'Werkzeug-1.0.1-py2.py3-none-any.whl']

for whl in whls:
	os.system('pip install /home/whls/'+whl)
