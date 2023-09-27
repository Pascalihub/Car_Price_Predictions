from src.CarPrice.config.configuration import ConfigurationManager
from src.CarPrice.components.data_ingestion import DataIngestion
from src.CarPrice.components.data_validation import DataValidation
from src.CarPrice.components.data_transformation import DataTransformation
from src.CarPrice.components.model_trainer import ModelTrainer
from src.CarPrice.logger import logging


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        data_transformation = DataTransformation(model_trainer_config)
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation()

        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.initiate_model_trainer(train_arr, test_arr)