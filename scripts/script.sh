#! /bin/bash

if [[ $GHCVER == "head" || -n "$SKIP_HADDOCK" ]]
  then
    DOCBUILD="echo 'Skipping docs...'"
  else
    DOCBUILD="$CABAL haddock"
fi

make BRANCH=`cat HEAD_BRANCH` test
  && $DOCBUILD\
  && $CABAL check\
  && $CABAL sdist
