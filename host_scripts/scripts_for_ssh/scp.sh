#!/bin/bash
sudo sshpass -p "password" sudo scp -P 2222 -r 'ubuntu@localhost:/home/ubuntu/GCOV_DATA' /hdd/GCOV_DATA/$(date --iso-8601="minutes")
