import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluation_model(X_train,X_test,y_train,y_test,models):
    try:
        report={}
        for i in range(len(list(models))):
            
            model=list(models.values())[i]
            model_fit=model.fit(X_train,y_train)

            train_data_predict=model_fit.predict(X_train)
            test_data_predict=model_fit.predict(X_test)
            
            train_r2_score=r2_score(y_train,train_data_predict)
            test_r2_score=r2_score(y_test,test_data_predict)
            
            report[list(models.keys())[i]]=test_r2_score
            
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
          
     
