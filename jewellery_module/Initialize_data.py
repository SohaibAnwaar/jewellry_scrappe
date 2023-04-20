"""
Getting the category and attributes from the excel file and matching it with the data from the json file.
"""
import pandas as pd
from fuzzywuzzy import fuzz
from const import excel_file_path


class InitializeData():

    def __init__(self,excel_file_path) :
        self.excel_file_path = excel_file_path

    def post_process_attribute_df(self):
        df = pd.read_csv(self.excel_file_path)
        df = df.transpose()
        df.head()
        df = df.drop("ID")
        df.columns = df.iloc[0]
        df = df.drop(["ATTRIBUTE"])
        df.reset_index(drop=True, inplace=True)
        df.fillna("empty", inplace = True)
        print("dfsd")
        return df

    def df_to_dict(self,df=pd.DataFrame):
        category_dict = dict()
        df_dict = df.to_dict()
        for i in df_dict:
            category_dict[i] = list(df_dict[i].values())
        return category_dict
    
    def post_process_category_dict(self,category_dict=''):
        for i in category_dict:
            category_dict[i] =  [x for x in category_dict[i] if x != 'empty']
        return category_dict

    def run(self):
        print("calling post_process_attribute_df")
        df= self.post_process_attribute_df()
        print("caling df_to_dict")
        category_dict = self.df_to_dict(df)
        print("calling post_process_category_dict")
        category_dict = self.post_process_category_dict(category_dict)
        return category_dict


validation_obj = InitializeData(excel_file_path)