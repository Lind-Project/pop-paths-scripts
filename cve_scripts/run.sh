#!/bin/bash

python3 cve_scraper.py
python3 paths2json.py
python3 pop_paths_comparison.py
python3 report.py
