import pandas as pd
import os
from mlproject import logger
from mlproject.entity.config_entity import ModelTrainerConfig
from sklearn.ensemble import RandomForestRegressor
import joblib

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from mlproject.utils.common import save_bin

from mlproject.exception import CustomException
import sys
from mlproject import logger


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def data_spliting(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        self.X_train = train_data.iloc[:, :-1]
        self.y_train = train_data.iloc[:, -1]
        self.X_test = test_data.iloc[:, :-1]
        self.y_test = test_data.iloc[:, -1]


    def hyper_parameter_tunning(self):
        
        try:
            models= self.config.ml_models
            for key in models.keys():
                models[key] = globals()[models[key]]()

            params = self.config.params
            X_train = self.X_train
            y_train = self.y_train.values.ravel()
            report = {}

            for i in range(len(list(models))):
                
                model = list(models.values())[i]
                para = params[list(models.keys())[i]]
                
                gs = GridSearchCV(model,para,cv=3, n_jobs=-1)
                gs.fit(X_train,y_train)
                model.set_params(**gs.best_params_)
                model.fit(X_train,y_train)
                
                y_train_pred = model.predict(X_train)
                train_model_score = r2_score(y_train, y_train_pred)
                report[list(models.keys())[i]] = train_model_score
                best_model_score = max(sorted(report.values()))
                best_model_name = list(report.keys())[list(report.values()).index(best_model_score)]
                
                best_model = models[best_model_name]
            
            #print(report)
            if best_model_score<0.6:
                raise CustomException("No best model found")
                
            logger.info(f"Best found model on both training and testing dataset")
                
            save_bin(best_model, os.path.join(self.config.root_dir, self.config.model_name))

        except Exception as e:
            raise CustomException(e, sys)