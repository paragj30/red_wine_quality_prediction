from mlproject import logger
from mlproject.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipelines.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipelines.stage_04_model_training import ModelTrainerTrainingPipeline
from mlproject.pipelines.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import sys
from mlproject.exception import CustomException

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.info("Error in stage {STAGE_NAME}")
    CustomException(e, sys)
        



STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_obj = DataValidationTrainingPipeline()
    data_validation_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.info("Error in stage {STAGE_NAME}")
    CustomException(e, sys)



STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transform_obj = DataTransformationTrainingPipeline()
    data_transform_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.info("Error in stage {STAGE_NAME}")
    CustomException(e, sys)



STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training_obj = ModelTrainerTrainingPipeline()
    model_training_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.info("Error in stage {STAGE_NAME}")
    CustomException(e, sys)


STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_eval_obj = ModelEvaluationTrainingPipeline()
    model_eval_obj .main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.info("Error in stage {STAGE_NAME}")
    CustomException(e, sys)