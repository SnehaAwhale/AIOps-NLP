from src.util.all_utils import read_yaml,create_dir,save_loc_file
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib


def train(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifects_dir=config["artifacts"]["artifacts_dir"]
    test_train_splitdir=config["artifacts"]["split_data_dir"]
    train_dataFilename=config["artifacts"]["train_data"]
    test_dataFilename=config["artifacts"]["test_data"]

    train_data_path = os.path.join(artifects_dir, test_train_splitdir, train_dataFilename)
    test_data_path = os.path.join(artifects_dir, test_train_splitdir, test_dataFilename)

    alpha=params['model_params']['elasticNet']['alpha']
    l1_ratios=params['model_params']['elasticNet']['l1_ratio']
    random_state=params['model_params']['elasticNet']['random_state']

    train_data=pd.read_csv(train_data_path)
    test_data=pd.read_csv(test_data_path)

    train_y=train_data['quality']
    train_x=train_data.drop("quality",axis=1)

    lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratios,random_state=random_state)
    lr.fit(train_x,train_y)

    model_dir=config["artifacts"]['model_dir']
    model_file=config['artifacts']['model_file']

    model_file_path=os.path.join(artifects_dir,model_dir,model_file)


    joblib.dump(lr,model_file_path)



if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args=args.parse_args()
    train(config_path=parsed_args.config,params_path=parsed_args.params)