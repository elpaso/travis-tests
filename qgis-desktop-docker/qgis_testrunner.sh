#!/bin/bash
# Run a test inside QGIS
### Turn on debug mode ###
#set -x

TEST_NAME=$1

pushd .
cd /tests_directory
unbuffer qgis --optionspath /qgishome --nologo --code /usr/bin/qgis_testrunner.py $TEST_NAME  2>/dev/null | grep FAILED
RETURN_CODE=$?
popd
if [ $RETURN_CODE != 0 ];
    then exit 0;
fi
exit 1
