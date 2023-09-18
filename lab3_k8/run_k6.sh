#!/bin/bash
rm -rf ./k6_results.txt
k6 run load.js --quiet --log-output file=./k6_results.txt
cat ./k6_results.txt