#!/bin/bash

# making sure that if it fails or finishes early, it runs again
while [ 1 -eq 1 ]; 
do
    sudo /opt/ltp/runltp
done