# n-Least Significant Bit(s) Steganography

[![GitHub Last Commit](https://img.shields.io/github/last-commit/mtabidze/nLSBs-Steganography.svg?branch=main)](https://github.com/mtabidze/nLSBs-Steganography/commits/main)
[![Testing Workflow Status](https://github.com/mtabidze/nLSBs-Steganography/actions/workflows/testing-flow.yml/badge.svg?branch=main)](https://github.com/mtabidze/llm-co-writer/actions/workflows/testing-flow.yml)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/mtabidze/nLSBs-Steganography.svg)](https://github.com/mtabidze/nLSBs-Steganography/pulls)
[![GitHub Release](https://img.shields.io/github/release/mtabidze/nLSBs-Steganography.svg)](https://github.com/mtabidze/nLSBs-Steganography/releases)

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=flat&logo=macos&logoColor=F0F0F0)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=flat&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Atom](https://img.shields.io/badge/Atom-%2366595C.svg?style=flat&logo=atom&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat&logo=githubactions&logoColor=white)
![Dependabot](https://img.shields.io/badge/dependabot-025E8C?style=flat&logo=dependabot&logoColor=white)

---

## Introduction

n-Least Significant Bit(s) Steganography is a versatile Python library designed for seamless message insertion and extraction within images using the n-Least Significant Bits technique. This library empowers users to embed confidential information into images while maintaining visual integrity, and subsequently retrieve hidden messages with ease. 

---

## Example
### Message
The message to be inserted into the image: 

>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Images
The input image and resulting image with the message inserted.
![The input and resulting images](tools/SampleImages.png?raw=true)

---

## Dependency Management

This project is built using Python 3.11 and poetry.

### Specifying Dependencies
To add a new package to your project, run the following command:
```shell
poetry add <package name>
```
To remove a package, use this command:
```shell
poetry remove <package name>
```
### Specifying Development Dependencies
For development-specific packages, use the following commands.
To add a development package:
```shell
poetry add <package name> --group dev
```
To remove a development package:
```shell
poetry remove <package name> --group dev 
```
### Lock File Update
To update the lock file, execute this command:
```shell
poetry lock
```
### Exporting Lock File to requirements.txt
To export the lock file to a requirements.txt file, use this command:
```shell
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
### Installing Dependencies
To install project dependencies (excluding the root package), run:
```shell
poetry install --no-root 
```
### Building Package
To build and package project, run:
```shell
poetry build
```
### Publish Package
To publish package, run:
```shell
poetry publish
```
---

## Testing
You can run various tests and code analysis tools using the provided scripts
### All Tests
To run all tests, execute:
```shell
./bin/run_all_tests.sh
```
### Unit Testing
For unit tests, use:
```shell
./bin/run_unit_testing.sh
```
### Coverage Measurement
Measure code coverage with:
```shell
./bin/run_coverage_measurement.sh
```
### Static Code Analysis
Conduct static code analysis with:
```shell
./bin/run_static_code_analysis.sh
```
