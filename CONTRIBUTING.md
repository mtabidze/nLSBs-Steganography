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
