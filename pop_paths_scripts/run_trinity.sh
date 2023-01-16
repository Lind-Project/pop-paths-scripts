#!/bin/bash

# making sure that if it fails or finishes early, it runs again
while [ 1 -eq 1 ]; 
do
    ./trinity/trinity -qq -l off -C16 --dropprivs
done