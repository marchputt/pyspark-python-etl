from setuptools import setup, find_packages

setup(
    name="simplepyetl",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pyspark",
        "pandas",
        "chispa",
    ],
    python_requires=">=3.11",
    author="Pargorn Puttapirat",
    description="Example ETL project with PySpark",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/marchputt/pyspark-python-etl",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)