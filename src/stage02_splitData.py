from src.util.all_utils import read_yaml,create_dir,save_loc_file
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
def split_save_data(config_path,params_path):
    config=read_yaml(config_path)
    remote_data = config["data_source"]
    data = pd.read_csv(remote_data, sep=";")
    artifects_dir=config["artifacts"]["artifacts_dir"]
    raw_local_dir=config["artifacts"]["raw_local_dir"]
    raw_local_file=config["artifacts"]["raw_local_file"]

    raw_local_dirPath=os.path.join(artifects_dir,raw_local_dir)

    raw_local_filePath=os.path.join(raw_local_dirPath,raw_local_file)
    # read params file to get paramter for test size and randomState
    # param_file=read_yaml(params_path)
    # test_ratio=param_file["base"]["random_state"]
    # random_ratio=param_file["base"]["test_size"]
    # create directory to store test and train csv
    test_train_splitdir=config["artifacts"]["split_data_dir"]
    train_dataFilename=config["artifacts"]["train_data"]
    test_dataFilename=config["artifacts"]["test_data"]

    train_data_path=os.path.join(artifects_dir,test_train_splitdir,train_dataFilename)
    test_data_path=os.path.join(artifects_dir,test_train_splitdir,test_dataFilename)

    # create_dir(dirs=[train_data_path])
    # create_dir(dirs=[test_data_path])
    train, test = train_test_split(data, test_size=.3, random_state=43)
    print(train.head())
    print(test.head())


    #saving the test and train data csv to respective folders
    for data, data_path in (train, train_data_path), (test, test_data_path):
        save_loc_file(data, data_path)







if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args=args.parse_args()
    print("parmas_path is " + str(parsed_args.params))
    split_save_data(config_path=parsed_args.config,params_path=parsed_args.params)