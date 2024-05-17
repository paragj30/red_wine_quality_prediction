import joblib 
from pathlib import Path
from mlproject.utils.common import load_bin
from mlproject.exception import CustomException
import sys
from mlproject import logger
from dataclasses import dataclass
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        pass

    
    def predict(self, data):
        try:
            preprocessor = load_bin(Path('artifacts/data_transformation/preprocessor.joblib'))
            logger.info(f'Preprocessor object has been loaded{preprocessor}')

            model = load_bin(Path('artifacts/model_trainer/model.joblib'))
            logger.info(f'model object has been loaded{model}')

            logger.info('Test live data transformation begin')
            data_scaled = preprocessor.transform(data)
            logger.info(f'Data After Preprocessing by preprocessor obect {data_scaled}')

            prediction = model.predict(data_scaled)
            print('Test live data prediction ended')

        except Exception as e:
            CustomException(e, sys)

        return prediction
    

@dataclass
class CustomData:
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "fixed acidity": [self.fixed_acidity],
                "volatile acidity": [self.volatile_acidity],
                "citric acid": [self.citric_acid],
                "residual sugar": [self.residual_sugar],
                "chlorides": [self.chlorides],
                "free sulfur dioxide": [self.free_sulfur_dioxide],
                "total sulfur dioxide": [self.total_sulfur_dioxide],
                "density": [self.density],
                "pH": [self.pH],
                "sulphates": [self.sulphates],
                "alcohol": [self.alcohol],
            }

            live_data = pd.DataFrame(custom_data_input_dict)
            logger.info(f'Live data: {live_data}')
            return live_data

        except Exception as e:
            raise CustomException(e, sys)