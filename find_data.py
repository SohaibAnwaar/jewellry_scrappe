import json
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

df = pd.read_excel('NER_Attributes.xlsx')
  
# Opening JSON file
f = open('test.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
# Closing file
f.close()
# Iterating through the json
# list
items = []
final_output={}
category=['jewelry','bracelet','brooches','earrings','necklaces','pendants','rings', 'rack & sets','accesories','ankle',
          'bracelet chain','bangle','bolo','bracelet-charm','cuff','identification','tennis','friendship','brooches','dress-clips','fur-clips','jewelry-clips','ball','button','dangle','ear-jacket','ear-climber','huggie','linear	','hoop','drop','ear-cuffs',
          'ear-pins','ear-wraps','half-ball','stud','necklace Chain','charm-necklace','multi-strand','choker','collar','pearl-strands','pendant-necklaces(wihchain)','pendants(withoutchain)','pendant-enhancers','pendant_slides',
          'anniversary','bands','claddagh','class','engagement','promise','right-hand','signet','thumb','toe','wedding-bands','Cocktail',
          'DoubleBand','Two-finger','Wrap','Earring-sets','Bracelet-sets','Necklace-sets','Ring-set','Jewel extension','Earring pressure',
          ]
for chunck in data:

    print(chunck['SKU_SHORT_DESCRIPTION'])
    
    for index, rows in df.iterrows():
      for item in rows:
         
         if isinstance(item, float):
            pass
         elif isinstance(item, int):
            pass
         else:
            # items[index]=item["ATTRIBUTE"]
            print(item)
            if fuzz.ratio(item, chunck['SKU_SHORT_DESCRIPTION']) > 40 or fuzz.ratio(item, chunck['SKU_LONG_DESCRIPTION']) > 40 or fuzz.ratio(item, chunck['SKU_TITLE']) > 40 or item in category:
               items.append(f"{rows['ATTRIBUTE']} {item} , ")


      if len(items)> 0:
         final_output[index]=items
      items=[]

print("final output",final_output)


# final output {31: ['PRODUCT_SHAPE_MOTIFF Celestial Symbols , ', 'PRODUCT_SHAPE_MOTIFF Good Luck Symbols , '], 3: ['MAIN_MATERIAL Silver , ', 'MAIN_MATERIAL Stainless Steel , '], 6: ['SECONDARY_MATERIAL Silver , ', 'SECONDARY_MATERIAL Stainless Steel , '], 21: ['RAW_METAL Silver , ', 'RAW_METAL Stainless Steel , '], 26: ['PLATING_METAL Silver , ', 'PLATING_METAL Stainless Steel , '], 20: ['MANUFACTURING_ORIGIN United States , '], 19: ['MANUFACTURING_TECHNIQUE Sinterizado , '], 105: ['CHAIN_TYPE half-round-gooseneck , '], 33: ['PEARL_SHAPE elongated , '], 110: ['EARRING_BACK_FINDING lever-back , '], 111: ['CLASP_TYPE Fold over , '], 7: ['SIZE Medium , '], 4: ['MATERIAL_FINISHING Two-tone , '], 46: ['GEMSTONE_1_TREATMENT Color_treated , '], 60: ['GEMSTONE_2_TREATMENT Color_treated , '], 73: ['GEMSTONE_3_TREATMENT Color_treated , '], 86: ['GEMSTONE_4_TREATMENT Color_treated , '], 99: ['GEMSTONE_5_TREATMENT Color_treated , '], 25: ['IF_GOLD_VARIATION Gold  , '], 30: ['JEWELRY_SETTING_STYLE Channel , '], 37: ['GEMSTONE_1_SETTING Channel , '], 42: ['GEMSTONE_1_SETTING Channel , '], 52: ['GEMSTONE_2_SETTING Channel , '], 56: ['GEMSTONE_2_SETTING Channel , '], 69: ['GEMSTONE_3_SETTING Channel , '], 79: ['GEMSTONE_4_SETTING Channel , '], 92: ['GEMSTONE_5_SETTING Channel , ']}




    
            
   
