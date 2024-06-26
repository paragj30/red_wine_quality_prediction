import os
import pandas as pd
from mlproject.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
from pathlib import Path
from mlproject.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    
    def save_results(self):

        df_test = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = df_test.iloc[:, :-1]
        y_test = df_test.iloc[:, -1]
        
        y_predict = model.predict(X_test)

        (rmse, mae, r2) = self.eval_metrics(y_test, y_predict)
        
        # Saving metrics as local
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        save_json(path=Path(self.config.metric_file_name), data=scores)