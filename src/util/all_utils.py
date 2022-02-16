import yaml
import os
import json

def read_yaml(pathtofile)-> dict:
    with open(pathtofile) as yaml_file:
        content=yaml.safe_load(yaml_file)

    return content

def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        print(f"directory has been created for {dir_path}")

def save_loc_file(data,data_path):
    data.to_csv(data_path,index=False)

def save_report(report : dict, report_path: str):
    with open(report_path,'w') as f:
        json.dump(report,f , indent=4)
    print(f"report has been save {report_path}")