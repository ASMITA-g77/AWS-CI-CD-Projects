import os
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

import pandas as pd
import numpy as np

from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRFRegressor
from src.utils import evaluation_model, save_object

@dataclass 
class ModelTrainerConfig:
    model_trainer_obj_path:str=os.path.join('artifacts','model.pkl')

class ModelTrainerMain:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def training_initiate(self,training_arr,testing_arr):
        try:
            self.training_data=training_arr
            self.testing_data=testing_arr
            
            logging.info("Data spliting has initialize")
            X_train,y_train,X_test,y_test=(self.training_data[:,:-1],
                                           self.training_data[:,-1],
                                           self.testing_data[:,:-1],
                                           self.testing_data[:,-1]
                                            )
            models={
                "Linear Regression": LinearRegression(),
                "Logistic Regression": LogisticRegression(),
                "DecisionTree Regressor": DecisionTreeRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "GradientBoosting Regressor": GradientBoostingRegressor(),
                "RandomForest Regressor": RandomForestRegressor(),
                "KNeighbors Regressor": KNeighborsRegressor(),
                "XGBRF Regressor": XGBRFRegressor(),
            }
            
            model_report:dict=evaluation_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            
            best_model_score=max((model_report.values()))
            
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            
            best_model=models[best_model_name]
            
            if(best_model_score)<0.6:
                raise CustomException("No best model founddra")
            logging.info("Best found model on the both training and testing dataset")
            
            save_object(
                file_path=ModelTrainerConfig.model_trainer_obj_path,
                obj=best_model
            )
            
            y_pred=best_model.predict(X_test) 
            r2_squre=r2_score(y_test,y_pred)
            
            return r2_squre
            
        except Exception as e:
            raise CustomException(e,sys)           
            
            