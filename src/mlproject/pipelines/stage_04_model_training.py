from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_training import ModelTrainer
from mlproject import logger
import sys
from mlproject.exception import CustomException


STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.data_spliting()
        model_trainer_config.hyper_parameter_tunning()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.info("Error occurred while executing stage {STAGE_NAME}")
        CustomException(e, sys)