from src.util.all_utils import read_yaml,create_dir,save_loc_file, save_report
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import numpy as np

def evalutate_model(actual_value,Predicted_value):
    rmse=mean_squared_error(actual_value,Predicted_value)
    mae=mean_absolute_error(actual_value,Predicted_value)
    r2_scores=r2_score(actual_value,Predicted_value)
    return rmse,mae,r2_scores

def evaluate(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifects_dir=config["artifacts"]["artifacts_dir"]
    test_train_splitdir=config["artifacts"]["split_data_dir"]
    train_dataFilename=config["artifacts"]["train_data"]
    test_dataFilename=config["artifacts"]["test_data"]
    reportPath=config["artifacts"]["report"]
    scores=config["artifacts"]["scores"]

    train_data_path = os.path.join(artifects_dir, test_train_splitdir, train_dataFilename)
    test_data_path = os.path.join(artifects_dir, test_train_splitdir, test_dataFilename)

    alpha=params['model_params']['elasticNet']['alpha']
    l1_ratios=params['model_params']['elasticNet']['l1_ratio']
    random_state=params['model_params']['elasticNet']['random_state']

    # train_data=pd.read_csv(train_data_path)
    test_data=pd.read_csv(test_data_path)

    test_y=test_data['quality']
    test_x=test_data.drop("quality",axis=1)



    model_dir=config["artifacts"]['model_dir']
    model_file=config['artifacts']['model_file']

    model_file_path=os.path.join(artifects_dir,model_dir,model_file)
    model = joblib.load(model_file_path)

    predicted_value=model.predict(test_x)
    rmse,mae,r2_score=evalutate_model(test_y,predicted_value)
    print(rmse,mae,r2_score)

    # report_file_path=os.path.join(artifects_dir,reportPath,scores)
    report_dir=config['artifacts']['report']
    scores_file=config['artifacts']['scores']

    report_file_path = os.path.join(artifects_dir, report_dir)
    score_file_path=os.path.join(report_file_path,scores_file)

    create_dir([report_file_path])

    score={
        "rmse": rmse,
        "mae" : mae,
        "r2_score" : r2_score,
    }


    save_report(report=score, report_path=score_file_path)






if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args=args.parse_args()
    evaluate(config_path=parsed_args.config,params_path=parsed_args.params)