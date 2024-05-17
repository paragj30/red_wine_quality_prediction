import os
from mlproject import logger
from sklearn.model_selection import train_test_split
from mlproject.entity.config_entity import DataTransformationConfig
import pandas as pd

import pandas as pd
import numpy as np
from mlproject.utils.common import save_bin
from mlproject.exception import CustomException
import sys

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        try:
            logger.info("Started the Spliting the data into training and test sets")

            data = pd.read_csv(self.config.data_path)
            train, test = train_test_split(data, test_size = 0.2, random_state = 42)            
            logger.info("Successfully splited data into training and test sets")

            return train, test
        
        except Exception as e:
            raise CustomException(e, sys)
        
    
    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:

            logger.info("Starting Pipeline construction")
            features_column = self.config.features_column
            target_column = self.config.target_column

            categorical_columns = [col for col, dtype in features_column.items() if dtype == 'obj' and col !=  target_column]
            numerical_columns = [col for col, dtype in features_column.items() if dtype != 'obj' and col != target_column]


            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('scalar',StandardScaler()),
         #       ('TruncatedSVD', TruncatedSVD(5))
                ])
            
            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder(handle_unknown='ignore')),
                ("scaler",StandardScaler(with_mean=False)),
      #          ('TruncatedSVD', TruncatedSVD(5))
                ])

            logger.info(f"Before ColumnTransformer: Categorical Columns: {categorical_columns}")
            logger.info(f"Before ColumnTransformer: Numerical Columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
                )
            
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
    

    def initiate_data_transormation(self):
        try:
            logger.info("Started spliting data into X_train, y_train and X_test, y_test")
            train, test = self.train_test_spliting() 
            target_column = self.config.target_column
            

            X_train = train.drop(columns = [target_column], axis=1)
            y_train = train[target_column]

            X_test = test.drop(columns = [target_column], axis=1)
            y_test = test[target_column]

            logger.info("Successfully splited data into X_train, y_train and X_test, y_test")
            logger.info(f'Shape of X_train: {X_train.shape}')
            logger.info(f'Shape of y_train:  {y_train.shape}')
            logger.info(f'Shape of X_test:  {X_test.shape}')
            logger.info(f'Shape of y_test:  {y_test.shape}')

            
            logger.info("Reading the preprocessor pipeline object for training")
            preprocessing_obj=self.get_data_transformer_object()

            logger.info("Applying Preprocessing on training and test dataframe")
            input_feature_train_arr = preprocessing_obj.fit_transform(X_train)
            input_feature_test_arr = preprocessing_obj.transform(X_test)

            df_train = np.c_[input_feature_train_arr, np.array(y_train)]
            df_test = np.c_[input_feature_test_arr, np.array(y_test)]
            logger.info(f"df_train.shape: {df_train.shape}")
            logger.info(f"df_test.shape: {df_test.shape}")

            df_train = pd.DataFrame(df_train)
            df_test = pd.DataFrame(df_test)
            df_train.to_csv(os.path.join(self.config.root_dir, "df_train.csv"),index = False)
            df_test.to_csv(os.path.join(self.config.root_dir, "df_test.csv"),index = False)
            
            logger.info(f"Successfully saved the df_train and df_test after preprocessing") 
            logger.info(f'Shape of Training dataset df_train.shape: {df_train.shape}')
            logger.info(f'Shape of Testing dataset df_test.shape: {df_test.shape}')

            save_bin(preprocessing_obj, os.path.join(self.config.root_dir, self.config.preprocessor_name))
            logger.info(f"Saved preprocessing object")  
   
        except Exception as e:
            raise CustomException(e, sys)