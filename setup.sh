#!/bin/sh

sudo apt install build-essential git python2 -y
sudo apt install g++-9 g++-10 g++-11 -y
sudo apt install clang-9 clang-11 clang-12 clang-13 -y
sudo apt install libopenmpi-dev -y
sudo ln /usr/bin/python2 /usr/bin/python
