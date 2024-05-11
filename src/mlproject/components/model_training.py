import pandas as pd
import os
from src.mlproject import logger
from src.mlproject.entity.config_entity import ModelTrainerConfig
from sklearn.ensemble import RandomForestRegressor
import joblib



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        X_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[[self.config.target_column]]
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]



        model = RandomForestRegressor(n_estimators = self.config.n_estimators,
                                      min_samples_split = self.config.min_samples_split,
                                      max_features = self.config.max_features,
                                      max_depth = self.config.max_depth,
                                      criterion = self.config.criterion,
                                      random_state=42)
        model.fit(X_train, y_train)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))