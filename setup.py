from pathlib import Path
from setuptools import setup
from setuptools_scm import ScmVersion

def version_for_project(version: ScmVersion) -> str:
   return str(version.tag)


setup(
    packages=["pointcept"],
    package_dir={"pointcept": "pointcept"},
)


