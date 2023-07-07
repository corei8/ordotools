from setuptools import find_packages
from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ordo",
    version="0.0.1",
    description="A set of tools for producing a traditional Catholic Ordo, given a year and diocese",
    package_dir={"": "ordo"},
    packages=find_packages(where="ordo"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/corei8/Ordo",
    author="corei8 (Fr. G.R.Barnes)",
    author_email="corei8.github@gmail.com",
    license="GNU",
    # classifiers=[]
    install_requires=[
        "dateutil"
    ],
    python_requires=">=3.7",
)

