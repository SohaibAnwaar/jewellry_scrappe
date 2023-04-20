import json
import pandas as pd
from datetime import datetime

now = datetime.now()
class GenerateFile():
    def initialized_file(self,resp):
        pd.read_json(json.dumps(resp)).to_csv(f'{now.strftime("%d")}_{now.strftime("%b")}_Results.csv')


GenerateFile_obj = GenerateFile()