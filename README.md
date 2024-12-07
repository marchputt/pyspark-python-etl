# pyspark-python-etl

Boilerplate ETL project using a framework based on PySpark

- In this example repository, we are going to use `simplepyetl` as an example project name.

# Development setup

For developers to develop some ETL processing with this starter repository, PySpark must be instlalled.

- Follow this guide to install PySpark: https://www.datacamp.com/tutorial/installation-of-pyspark
- Create virtual environment
- Install the framework using editable mode: `pip install -e .`
- (Optionally, for VS Code) Take advantage of test discovery functionality: https://code.visualstudio.com/docs/python/testing#_configure-tests

## GitHub Actions for Unit Testing

The repository is configured to use GitHub Actions to run unit tests automatically. This ensures that the codebase remains stable and that new changes do not introduce any regressions. The workflow is defined in a YAML file located in the `.github/workflows` directory.
