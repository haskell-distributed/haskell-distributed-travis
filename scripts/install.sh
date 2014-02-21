#!/bin/bash

CB=`cat HEAD_BRANCH`
./travis/scripts/install-deps.sh\
  && echo "============================================================"\
  && echo "Installing to $CB"\
  && make -j BRANCH=$CB BASE_DIR=`pwd` CABAL_EXTRA=--force-reinstalls install-deps
