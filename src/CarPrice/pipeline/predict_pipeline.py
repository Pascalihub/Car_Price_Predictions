import sys
import numpy as np
import pandas as pd
import os
from src.CarPrice.exception import CustomException
from src.CarPrice.utils.common import load_object
from src.CarPrice.logger import logging

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model_path = 'artifacts/model.pkl'
            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.info('Exception occurred in prediction pipeline')
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 Present_Price: float,
                 Kms_Driven: int,
                 Owner: int,
                 car_age: int,
                 Fuel_Type: str,
                 Seller_Type: str,
                 Transmission: str):
      
        self.Present_Price = Present_Price
        self.Kms_Driven = Kms_Driven
        self.Owner = Owner
        self.car_age = car_age
        self.Fuel_Type = Fuel_Type
        self.Seller_Type = Seller_Type
        self.Transmission = Transmission
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Present_Price': [self.Present_Price],
                'Kms_Driven': [self.Kms_Driven],
                'Owner': [self.Owner],
                'car_age': [self.car_age],
                'Fuel_Type': [self.Fuel_Type],
                'Seller_Type': [self.Seller_Type],
                'Transmission': [self.Transmission]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occurred in prediction pipeline')
            raise CustomException(e, sys)


