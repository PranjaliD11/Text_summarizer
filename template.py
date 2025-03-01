import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name="textSummarizer"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #inti.py is constructor file for a Python package
    f"src/{project_name}/conponents/__init__.py", #components.py is a module for components of the project
    f"src/{project_name}/utils/__init__.py",#utils.py is a utility module
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py", #logging.py is a module for logging
    f"src/{project_name}/config/__init__.py", #config.py is a module for configuration
    f"src/{project_name}/config/configuration.py", #configuration.py is a module for configuration
    f"src/{project_name}/pipeline/__init__.py", #pipeline.py is a module for pipeline
    f"src/{project_name}/entity/__init__.py", #entity.py is a module for entity
    f"src/{project_name}/constants/__init__.py", #constants.py is a module for constants
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reserch/trials.ipynb"
]

for file_path in list_of_files:
    filepath=Path(file_path)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #check if file is empty or not, so that we don't overwrite existing files
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already exists")

