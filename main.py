"""
Getting the category and attributes from the excel file and matching it with the data from the json file.
"""
import json
import pandas as pd
from fuzzywuzzy import fuzz

df = pd.read_excel('NER_Attributes.xlsx')
# pylint: disable=line-too-long
category = ['jewelry', 'bracelet', 'brooches', 'earrings', 'necklaces', 'pendants', 'rings', 'rack & sets',
            'accessories', 'ankle', 'bracelet chain', 'bangle', 'bolo', 'bracelet-charm', 'cuff', 'identification', 'tennis',
            'friendship', 'brooches', 'dress-clips', 'fur-clips', 'jewelry-clips', 'ball', 'button', 'dangle', 'ear-jacket',
            'ear-climber', 'huggie', 'linear', 'hoop', 'drop', 'ear-cuffs', 'ear-pins', 'ear-wraps', 'half-ball',
            'stud', 'necklace chain', 'charm-necklace', 'multi-strand', 'choker', 'collar', 'pearl-strands',
            'pendant-necklaces(with chain)', 'pendants(without chain)', 'pendant-enhancers', 'pendant_slides', 'anniversary',
            'bands', 'claddagh', 'class', 'engagement', 'promise', 'right-hand', 'signet', 'thumb', 'toe', 'wedding-bands',
            'cocktail', 'double-band', 'two-finger', 'wrap', 'earring-sets', 'bracelet-sets', 'necklace-sets', 'ring-set',
            'jewel extension', 'earring pressure']

with open('test.json', encoding='utf-8') as f:
    data = json.load(f)

final_output = {}
for index, chunk in enumerate(data):
    print(chunk['SKU_SHORT_DESCRIPTION'])

    items = []
    for _, row in df.iterrows():
        for attribute, item in row.iteritems():
            if pd.isnull(item):
                pass
            elif isinstance(item, (float, int)):
                continue
            elif (fuzz.ratio(item, chunk['SKU_SHORT_DESCRIPTION']) > 40 or
                  fuzz.ratio(item, chunk['SKU_LONG_DESCRIPTION']) > 40 or
                  fuzz.ratio(item, chunk['SKU_TITLE']) > 40 or
                  item.lower() in category):

                items.append(f"{attribute} {item}, ")

        if items:
            final_output[index] = items
            items = []

print("final output", final_output)
