
import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s: %(levelname)s]: %(message)s')

while True:
    project_name = input("Project name")
    if project_name!="":
        break

logging.info(f"creating project:->  {project_name}")

# file tree
pack_tree = [
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    f"init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "tox.ini",
    "pyproject.toml",
]

for filepath in pack_tree:
    filepath = Path(filepath)
    filedir,filename =os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory at: {filedir} for file: {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w')as f:
            pass
        logging.info(f"Created new file: {filename} at path: {filepath}")
    else:
        logging.info(f"Already have file at path {filepath}")