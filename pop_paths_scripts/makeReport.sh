sudo lcov --capture --output-file $1/kernel.info
genhtml $1/kernel.info