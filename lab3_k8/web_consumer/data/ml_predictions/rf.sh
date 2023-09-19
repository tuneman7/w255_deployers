#!/bin/bash

cd ./county_data_files/
. rf.sh
cd ./../
cd ./msa_data_files/
. rf.sh
cd ./../
cd ./files_for_drop_downs/
. rf.sh
cd ./../
cd ./ols_model_files/interest_rate_effect/
. rf.sh
cd ./../../
cd ./pytorch_files/
. rf.sh
cd ./../
cd ./pytorch_msa/
. rf.sh
cd ./../

