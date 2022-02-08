import yaml
import os

def read_yaml(pathtofile)-> dict:
    with open(pathtofile) as yaml_file:
        content=yaml.safe_load(yaml_file)

    return content