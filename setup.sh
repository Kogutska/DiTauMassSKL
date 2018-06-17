#!/bin/bash

function setup_venv()
{
    if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters";
	echo "Virtual Env name pls ?";
    fi
    source /home/sbahrase/WorkDesk/PythonPackages/VirtualEnvs/"$1"/bin/activate;
}

if [[ "$(uname -n)" == "lhcgpu02"* ]]; then
        rootsetup
	if [ "$1" == "BRT_GPU" ]
	then
	    # setup root
	    source /software/root-6.10.04/bin/thisroot.sh
	    setup_venv $1;
	    export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}};
	else
	    echo "Wrong Venv for GPU machine !";
	fi
# [[ "$(uname -n)" =~ lhc(0[1-9]|1[0-6]) ]];	    
else
        # fix for now (waiting for rootpy fix for root6)
	export ROOT_VERSION=5.34.14-x86_64-slc6-gcc48-opt
	source /home/sbahrase/WorkDesk/setup.sh
	
       # source /home/sbahrase/.local/virtualenv-15.0.1/BRT_Venv/bin/activate
       # source /home/sbahrase/WorkDesk/PythonPackages/VirtualEnvs/BRT_NewSKL/bin/activate;
	
	echo "-----------> Setting $1 venv";
	setup_venv $1;
	
        # # hdf5 setup
	export HDF5_DIR="/home/sbahrase/.local/hdf5"
	export LD_LIBRARY_PATH=${HDF5_DIR}/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
	export PYTHONUSERBASE=${VIRTUAL_ENV}
fi