from setuptools import setup, find_packages

setup(
    name="datacleaner",
    version="0.1.0",
    description="A simple data cleaning package for CSV files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    packages=find_packages(),
    install_requires=["pandas"],
    python_requires=">=3.6",
)
