from src.CarPrice.config.configuration import ConfigurationManager
from src.CarPrice.components.data_ingestion import DataIngestion
from src.CarPrice.components.data_validation import DataValidation
from src.CarPrice.logger import logging


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()