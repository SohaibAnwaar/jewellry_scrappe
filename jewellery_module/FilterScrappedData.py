import copy
from tqdm import tqdm
from PreProcess import PreProcess
from fuzzywuzzy import fuzz
class FilterScrappedData(PreProcess):
    def __init__(self):
        self.final_output = dict()
        self.response = []
        self.final_json = dict()
    def get_tags(self,data = None, category_dict = None):

        for index, chunk in tqdm(enumerate(data)):
            self.final_output = dict()
            description = chunk['SKU_SHORT_DESCRIPTION'] + chunk['SKU_LONG_DESCRIPTION'] + chunk['SKU_TITLE']
            description = self.preprocess(description)
            self.final_json["description"] = description
            self.final_json["SKU"] = chunk['SKU']
            for category in category_dict:
                values = category_dict[category]
                words = list(set(description.split(" ")))
                words = [word.lower() for word in words]
                for item in category_dict[category]:
                    item = str(item)
                    item = self.preprocess(item)
                    for word in words:

                        match_ratio = fuzz.ratio(item, word)
                        if ( match_ratio > 90):
                            if category in self.final_output and (word == 'vermeil' or word == 'Vermeil'):
                                self.final_output[Main_Material].append("Silver") 
                                self.final_output[Secondary_Material].append("Gold") 
                                self.final_output[Raw_Metal].append("Silver") 
                                self.final_output[Plating_Metal].append("Gold")
                            elif category in self.final_output and (word == 'Silver Vermeil' or word == 'silver vermeil'):
                                self.final_output[Main_Material].append("Silver") 
                                self.final_output[Secondary_Material].append("Gold") 
                                self.final_output[Raw_Metal].append("Silver") 
                                self.final_output[Plating_Metal].append("Gold")
                            elif word == 'vermeil' or word == 'Vermeil' or word == 'Silver Vermeil' or word == 'silver vermeil':
                                self.final_output[Main_Material] = "Silver"  
                                self.final_output[Secondary_Material] = "Gold" 
                                self.final_output[Raw_Metal] = "Silver" 
                                self.final_output[Plating_Metal] = "Gold"
                            elif category in self.final_output:
                                per=fuzz.ratio('GEMSTONE_', category)
                                if per>=67:
                                    category_splited=category.split('_')
                                    key=f"GEMSTONE_{category_splited[1]}_{category_splited[2]}"
                                    if int(category_splited[1]) > 1:  
                                        if item in self.final_output[f"GEMSTONE_{1}_{category_splited[2]}"]:
                                            continue
                                        else:
                                            self.final_output[category].append(item)
                                            continue
                                self.final_output[category].append(item)
                            else:
                                per=fuzz.ratio('GEMSTONE_', category)
                                if per>=67:
                                    category_splited=category.split('_')
                                    key=f"GEMSTONE_{category_splited[1]}_{category_splited[2]}"
                                    if int(category_splited[1]) > 1:  
                                        if item in self.final_output[f"GEMSTONE_{1}_{category_splited[2]}"]:
                                            continue
                                        else:
                                            self.final_output[category] = [item]
                                            continue
                                self.final_output[category] = [item]
                            if word == 'diameter':
                                diameter_li=words[words.index(word):(words.index(word)+3)]
                                if 'mm' in diameter_li:
                                    print(diameter_li[1]+" "+diameter_li[2])
                                    self.final_output[PRODUCT_OUTTER_DIAMETER] = diameter_li[1]+" "+diameter_li[2]
                            if word == 'Gold Plated':
                                if ('Silver' in description or 'silver' in description) and  category in self.final_output: 
                                    self.final_output[Main_Material].append("Silver") 
                                    self.final_output[Secondary_Material].append("Gold") 
                                    self.final_output[Raw_Metal].append("Silver") 
                                    self.final_output[Plating_Metal].append("Gold")
                                elif ('Silver' in description or 'silver' in description): 
                                    self.final_output[Main_Material] = "Silver"
                                    self.final_output[Secondary_Material] = "Gold"
                                    self.final_output[Raw_Metal] = "Silver"
                                    self.final_output[Plating_Metal] = "Gold"
                                elif ('Brass' in description or 'brass' in description) and  category in self.final_output: 
                                    self.final_output[Main_Material].append("Brass") 
                                    self.final_output[Secondary_Material].append("Gold") 
                                    self.final_output[Raw_Metal].append("Brass") 
                                    self.final_output[Plating_Metal].append("Gold")
                                elif ('Brass' in description or 'brass' in description): 
                                    self.final_output[Main_Material] = "Brass"
                                    self.final_output[Secondary_Material] = "Gold" 
                                    self.final_output[Raw_Metal] = "Brass"
                                    self.final_output[Plating_Metal] = "Gold"
                                elif ('Steel' in description or 'steel' in description) and  category in self.final_output: 
                                    self.final_output[Main_Material].append("Steel") 
                                    self.final_output[Secondary_Material].append("Gold") 
                                    self.final_output[Raw_Metal].append("Steel") 
                                    self.final_output[Plating_Metal].append("Gold")
                                elif ('Steel' in description or 'steel' in description): 
                                    self.final_output[Main_Material] = "Steel"
                                    self.final_output[Secondary_Material] = "Gold" 
                                    self.final_output[Raw_Metal] = "Steel"
                                    self.final_output[Plating_Metal] = "Gold"
                            if category in self.final_output and (word == 'Sterling Silver' or word == 'sterling silver'):
                                self.final_output[Main_Material].append("Silver") 
                                self.final_output[Raw_Material_Purity].append("925")
                            elif word == 'Sterling Silver' or word == 'sterling silver':
                                self.final_output[Main_Material] = "Silver"  
                                self.final_output[Raw_Material_Purity] = "925" 

            sizes = self.extract_weight_and_length(description)
            self.final_output.update(sizes)
            self.final_json["tags"] = self.final_output
            self.response.append(copy.deepcopy(self.final_json))
        return self.response

FilterScrappedData_obj = FilterScrappedData()
