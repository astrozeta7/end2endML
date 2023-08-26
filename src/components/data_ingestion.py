import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn import model_selection
from dataclasses import dataclass

@dataclass
class DataIngestionConfig():
    raw_data_path: str = os.path.join('artifact', 'data.csv')
    train_data_path: str = os.path.join('artifact', 'train.csv')
    test_data_path: str = os.path.join('artifact', 'test.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_Data_Ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            df=pd.read_csv('src/notebook/Data/stud.csv')
            
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train Test split initiated")
            train_set, test_set = model_selection.train_test_split(df, test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )            
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_Data_Ingestion()

