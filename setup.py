import os
import os.path as osp
from setuptools import setup, find_packages

loc = os.path.dirname(os.path.abspath(__file__))

with open(osp.join(loc, 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    version="0.0.3",
    name="artifice.paper",
    author="@minelminel",
    url="https://www.github.com/minelminel/flask-boilerplate",
    description="Simple web app for testing deployment tools",
    install_requires=required,
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "artifice.paper=artifice.paper.core.manage:manager.run",
        ]
    }
)
