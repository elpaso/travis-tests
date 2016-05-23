#!/bin/bash
# Run a test inside QGIS
### Turn on debug mode ###
set -x

TEST_NAME=$1
echo "Running test $1"

cd /tests_directory
OUTPUT=`unbuffer qgis --optionspath /qgishome --nologo --code /usr/bin/qgis_testrunner.py $TEST_NAME`
if [ -n "$OUTPUT" ]; then
   echo "ERROR: No output from the test runner!!!"
   exit 1;
fi
echo $OUTPUT | grep -q FAILED
RETURN_CODE=$?
echo "$OUTPUT"
echo "End running test $1"
if [ $RETURN_CODE != 0 ];
    then exit 0;
fi
exit 1
