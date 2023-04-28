#!/bin/bash

source vars.env

python3 ./cve_scripts/cve_scraper.py $KERNEL_NUMBER
python3 ./cve_scripts/paths2json.py
python3 ./cve_scripts/pop_paths_comparison.py
python3 ./cve_scripts/report.py
