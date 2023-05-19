
import json
from Initialize_data import validation_obj
from FilterScrappedData import FilterScrappedData_obj
from SubSequential import SubSequential_obj
from generate_file import GenerateFile_obj

with open('test.json', encoding='utf-8') as f:
    data = json.load(f)

if __name__ == '__main__':
    category_dict = validation_obj.run()
    resp = FilterScrappedData_obj.get_tags(data, category_dict)
    resp = SubSequential_obj.stamping(resp)
    resp = SubSequential_obj.category_taxonomy(resp)
    GenerateFile_obj.initialized_file(resp)
    print(resp)
