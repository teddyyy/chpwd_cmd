#!/bin/bash

if [[ ! -e src/layers ]]; then
    ln -s ../../../layers/lambda/src/python/layers ./src
fi

if [[ ! -e test/mock_dynamodb ]]; then
    ln -s ../../../layers/test/mock_dynamodb ./test
fi
