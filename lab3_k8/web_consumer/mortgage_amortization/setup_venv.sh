#!/bin/bash
#setup the virtual environment.
deactivate 
rm -rf ./data_engineering_venv
python3 -m venv data_engineering_venv
source ./data_engineering_venv/bin/activate
. ir.sh

pip install git+https://github.com/b3mery/AmortaPy.git

#python3 two_series_to_graph_1.py

#deactivate

#rm -rf ./data_engineering_venv
