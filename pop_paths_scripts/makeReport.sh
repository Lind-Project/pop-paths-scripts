sudo lcov --capture --output-file $1/kernel.info
sudo genhtml $1/kernel.info