#!/bin/bash

# fix for now (waiting for rootpy fix for root6)
export ROOT_VERSION=5.34.14-x86_64-slc6-gcc48-opt
source /cluster/warehouse/qbuat/htautau_install/setup.sh
source /home/sbahrase/WorkDesk/PythonPackages/virtualenv-13.1.1/AtlasVenv/bin/activate

## hdf5 setup
export HDF5_DIR="/home/sbahrase/.local/hdf5"
export LD_LIBRARY_PATH=${HDF5_DIR}/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export PYTHONUSERBASE= ${VIRTUAL_ENV}

