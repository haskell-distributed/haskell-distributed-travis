#!/bin/bash

./travis/scripts/install-deps.sh\
  && echo "============================================================"\
  && echo "Installing"\
  && make -j BRANCH=`cat HEAD_BRANCH` install-deps
