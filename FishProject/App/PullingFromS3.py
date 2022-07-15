import pandas as pd
import boto3

import FishProject.config_manager as conf


class PullingClass:
    # Init only sets up strings needed to pull the data, doesn't actually pull it (efficiency over last project)
    def __init__(self):
        self.__s3_client = boto3.client('s3')
        self.__fish_db = conf.TARTARE + '.csv'
        self.__fish_db_mon = conf.TARTARE + '.csv'
        self.__fish_db_tues = conf.TARTARE + '.csv'
        self.__bucket_name = conf.BUCKETNAME

    @property
    def get_client(self):
        return self.__s3_client

    # Only getter of note - returns a list containing strings, saves space and easier to add to instead of needing
    # a new getter for each new list
    @property
    def get_fish_string_list(self):
        return [self.__fish_db, self.__fish_db_mon, self.__fish_db_tues]

    @property
    def get_bucket_name(self):
        return self.__bucket_name

    # Takes in strings (from list above) and returns the dataframes that will actually be used
    def pull_data_set(self, bucket_name: str, key: str):
        bucket_contents = self.get_client.get_object(Bucket=bucket_name, Key=key)
        csv_body = pd.read_csv(bucket_contents["Body"])
        return csv_body

