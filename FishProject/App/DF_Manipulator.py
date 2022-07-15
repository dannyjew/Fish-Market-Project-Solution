import pandas as pd


class DataManipulator:
    # Nothing needed in the init as only functions in this class
    def __init__(self):
        pass

    # Only static methods as this class doesn't actually contain any variables.
    # Takes in any number of dataframes and merges them all into one
    @staticmethod
    def appender(*args: pd.DataFrame):
        df_list = [x for x in args]
        returning_df = pd.concat(df_list)
        return returning_df

    @staticmethod
    def df_to_dict(dataframe: pd.DataFrame):
        return dataframe.to_dict()

    @staticmethod
    def avg_finder(dataframe: pd.DataFrame):
        return dataframe.groupby('Species').mean()
