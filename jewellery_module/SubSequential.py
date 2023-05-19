

class SubSequential():

    def stamping(self, All_data):
        index_count=0
        resp = All_data
        for block  in resp:
            if block:
                if block['tags'].get('RAW_METAL') is not None and'silver' in block['tags'].get('RAW_METAL'):
                    if block['tags'].get('RAW_MATERIAL_PURITY') == 800:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = 'Second Law'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 925:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = 'Sterling'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 930:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = 'Argentium'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 958:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = 'Britannia'
                if block['tags'].get('RAW_METAL') is not None and 'platinum' in block['tags'].get('RAW_METAL'):
                    if block['tags'].get('RAW_MATERIAL_PURITY') == 850:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 900:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 950:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 999:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 500:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                if block['tags'].get('RAW_METAL') is not None and 'palladium' in block['tags'].get('RAW_METAL'):
                    if block['tags'].get('RAW_MATERIAL_PURITY') == 500:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 950:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 999:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = ''
                if block['tags'].get('RAW_METAL') is not None and 'gold' in block['tags'].get('RAW_METAL'):
                    if block['tags'].get('RAW_MATERIAL_PURITY') == 333:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '8k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 375:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '9k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 416:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '10k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 416:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '10k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 417:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '11k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 458:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '12k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 500:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '13k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 541:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '14k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 583:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '14k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 585:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '15k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 625:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '16k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 666:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '17k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 708:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '18k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 750:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '19k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 791:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '20k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 833:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '21k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 875:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '22k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 916:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '22k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 917:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '23k'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == 958:
                        resp[index_count]['tags']['RAW_MATERIAL_STAMP'] = '24k' 
                
                if block['tags'].get('RAW_MATERIAL_STAMP') is not None: 
                    if block['tags'].get('RAW_MATERIAL_STAMP') == 'Second Law':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == 'Sterling':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == 'Argentium':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == 'Britannia':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '8k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '9k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '10k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '10k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '11k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '12k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '13k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '14k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '14k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '15k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '16k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '17k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '18k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '19k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '20k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '21k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '22k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '22k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '23k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                    elif block['tags'].get('RAW_MATERIAL_STAMP') == '24k':
                        resp[index_count]['tags']['RAW_METAL'] = 'Gold'
                if block['tags'].get('RAW_MATERIAL_PURITY') is not None:
                    if block['tags'].get('RAW_MATERIAL_PURITY') == '800':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '925':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '930':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '958':
                        resp[index_count]['tags']['RAW_METAL'] = 'Silver'
                        
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '850':
                        resp[index_count]['tags']['RAW_METAL'] = 'Platinum'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '900':
                        resp[index_count]['tags']['RAW_METAL'] = 'Platinum'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '950':
                        resp[index_count]['tags']['RAW_METAL'] = 'Platinum'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '999':
                        resp[index_count]['tags']['RAW_METAL'] = 'Platinum'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '500':
                        resp[index_count]['tags']['RAW_METAL'] = 'Palladium'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '950':
                        resp[index_count]['tags']['RAW_METAL'] = 'Palladium'
                    elif block['tags'].get('RAW_MATERIAL_PURITY') == '999':
                        resp[index_count]['tags']['RAW_METAL'] = 'Palladium' 
                        
            index_count+=1
        return resp
    def category_taxonomy(self, All_data):
        resp = All_data
        CATEGORY_1 = ['jewelry']

        CATEGORY_2=['bracelet', 'bracelet', 'bracelet', 'bracelet', 'bracelet', 'bracelet', 'bracelet', 'bracelet',
                    'bracelet', 'brooches', 'brooches', 'brooches', 'brooches', 'earring', 'earring', 'earring',
                    'earring', 'earring', 'earring', 'earring', 'earring', 'earring', 'earring', 'earring',
                    'earring', 'earring', 'earring', 'necklaces', 'necklaces', 'necklaces', 'necklaces', 'necklaces',
                    'necklaces', 'necklaces', 'pendants', 'pendants', 'pendants', 'rings', 'rings', 'rings', 'rings',
                    'rings', 'rings', 'rings', 'rings', 'rings', 'rings', 'rings', 'rings', 'rings', 'rings', 'rings',
                    'rings', 'pack & sets', 'pack & sets', 'pack & sets', 'pack & sets', 'accesories', 'accesories','brooch']

        CATEGORY_3 = ['ankle', 'bracelet chain', 'bangle', 'bolo', 'bracelet-charm', 'cuff', 'identification', 'tennis',
                    'friendship', 'brooches', 'dress-clips', 'fur-clips', 'jewelry-clips', 'ball', 'button', 'dangle',
                    'ear-jacket', 'ear-climber', 'huggie', 'linear', 'hoop', 'drop', 'ear-cuffs', 'ear-pins', 'ear-wraps',
                    'half-ball', 'stud', 'necklace chain', 'charm-necklace', 'multi-strand', 'choker', 'collar',
                    'pearl-strands', 'pendant-necklaces(wihchain)', 'pendants(withoutchain)', 'pendant-enhancers',
                    'pendant_slides', 'anniversary', 'bands', 'claddagh', 'class', 'engagement', 'promise', 'right-hand',
                    'signet', 'thumb', 'toe', 'wedding-bands', 'cocktail', 'open', 'doubleband', 'two-finger', 'wrap',
                    'earring-sets', 'bracelet-sets', 'necklace-sets', 'ring-set', 'jewel extension', 'earring pressure','brooch']


        index_count=0
        for block  in resp:
            if block:
                if block['tags'].get('CATEGORY_3') is not None:

                    if block['tags'].get('CATEGORY_2') is not None:
                        cat_3_val = block['tags'].get('CATEGORY_3')
                        for val in cat_3_val:
                            index = CATEGORY_3.index(val)
                            cat_2_val = CATEGORY_2[index] 
                            if cat_2_val in block['tags'].get('CATEGORY_2'):
                                if block['tags'].get('CATEGORY_1') is None:
                                    resp[index_count]['tags']['CATEGORY_1'] = 'jewelry'
                            else:
                                resp[index_count]['tags']['CATEGORY_2'].append(cat_2_val)
                                if block['tags'].get('CATEGORY_1') is None:
                                    resp[index_count]['tags']['CATEGORY_1'] = 'jewelry'
                    else:
                        cat_3_val = block['tags'].get('CATEGORY_3')
                        for val in cat_3_val:
                            index = CATEGORY_3.index(val)
                            cat_2_val = CATEGORY_2[index]
                            resp[index_count]['tags']['CATEGORY_2'] = cat_2_val
                            if block['tags'].get('CATEGORY_1') is None:
                                resp[index_count]['tags']['CATEGORY_1'] = 'jewelry'
                            
                elif block['tags'].get('CATEGORY_2') is not None:
                    if block['tags'].get('CATEGORY_1') is None:
                        resp[index_count]['tags']['CATEGORY_1'] = 'jewelry'
                    
                    
            index_count+=1
        return resp

SubSequential_obj = SubSequential()