import yaml
import os

def read_yaml(pathtofile)-> dict:
    with open(pathtofile) as yaml_file:
        content=yaml.safe_load(yaml_file)

    return content

def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        print(f"directory has been created for {dir_path}")