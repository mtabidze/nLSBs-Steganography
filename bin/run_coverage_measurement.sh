#!/usr/bin/env bash
# Copyright (c) 2023 Mikheil Tabidze
# This script performs coverage measurement.

echo -e "\nCoverage measurement has begun\n"

# Perform coverage measurement
coverage report --data-file=cover/unit-testing.coverage --fail-under=75
COVERAGE_MEASUREMENT_RESULT=$?

# Display results
echo -e "\nCoverage measurement has completed with exit code ${COVERAGE_MEASUREMENT_RESULT}\n"

# Return the exit code
if [ $COVERAGE_MEASUREMENT_RESULT -ne 0 ];
then
  return 1
fi
