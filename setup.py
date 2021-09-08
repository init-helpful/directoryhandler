from setuptools import setup, find_packages

setup(
    name="directoryhandler",
    version="0.1.5",
    description="Local directory lookup and management",
    install_requires=["lxml", "jsondatahelper"],
    py_modules=["directoryhandler"],
    package_dir={"": "src"},
)
