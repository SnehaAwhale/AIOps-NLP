from src.util.all_utils import read_yaml,create_dir
import argparse
import pandas as pd
import os

def get_data(config_path):
    config=read_yaml(config_path)
    remote_data=config["data_source"]
    data=pd.read_csv(remote_data,sep=";")
    artifects_dir=config["artifacts"]["artifacts_dir"]
    raw_local_dir=config["artifacts"]["raw_local_dir"]
    raw_local_file=config["artifacts"]["raw_local_file"]

    raw_local_dirPath=os.path.join(artifects_dir,raw_local_dir)
    create_dir(dirs=[raw_local_dirPath])
    raw_local_filePath=os.path.join(raw_local_dirPath,raw_local_file)

    data.to_csv(raw_local_filePath,sep=",",index=False)




if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    parsed_args=args.parse_args()
    get_data(config_path=parsed_args.config)