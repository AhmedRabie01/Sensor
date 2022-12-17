import sys,os
from Sensor_Fault_Detection.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging
from Sensor_Fault_Detection.entity.artifact_entity import DataIngestionArtifact
from Sensor_Fault_Detection.components.data_ingestion import DataIngestion

class TrainingPipeline:
    
    def __init__(self):
         self.training_pipeline_config = TrainingPipelineConfig()

        
         
    def start_data_ingestion(self)-> DataIngestionArtifact:

        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config = self.training_pipeline_config)
            logging.info("starting data ingestion")
            data_ingestion =DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact  = data_ingestion.initiate_data_ingestion()
            logging.info("data ingestion completed")
            
            logging.info(f"data ingestion completed and artifact: %s{data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
    
    
    def start_data_validation(self):

        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
 

    def start_data_transformation(self):

        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_trainer(self):

        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_evoluation(self):

        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_pusher(self):

        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def run_pipeline(self):

        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)