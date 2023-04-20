# import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
import copy


# download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
stop_words = stopwords.words('english') + list(string.punctuation)

class PreProcess():
    def preprocess(self,text=None):
        # tokenize text
        tokens = word_tokenize(text.lower())
        # remove stopwords and punctuation
        tokens = [token for token in tokens if token not in stop_words]
        # lemmatize words
        lemmatizer = nltk.stem.WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        # join tokens back into a string
        preprocessed_text = ' '.join(tokens)
        return preprocessed_text



    def extract_weight_and_length(self,text=None):
        """
        Extracts weight and length values along with their units from text using regular expressions.
        Returns a dictionary with keys 'weight' and 'length'.
        """
        # regular expressions to detect weight and length values
        weight_pattern = r"\b(\d+(?:\.\d+)?)\s*(g|kg|pound|lb)\b"
        length_pattern = r"\b(\d+(?:\.\d+)?)\s*(m|cm|mm|kilometer|km|mile|inch|in)\b"
        size_pattren =   r'\b(\d+\s*x\s*\d+)\s*(m|cm|mm|kilometer|km|mile|inch|in)\b'


        # extract weight and length values and their units from text
        weights = re.findall(weight_pattern, text, re.IGNORECASE)
        lengths = re.findall(length_pattern, text, re.IGNORECASE)
        sizes = re.findall(size_pattren, text, re.IGNORECASE)

        # convert weight values to grams
        size_dict = {}
        for size, unit in sizes:
            size_dict['size'] = str(size) + str(unit)

        # convert length values to meters
        length_dict = {}
        for length, unit in lengths:
            
            length_dict['length'] = str(length) + str(unit)

        # combine weight and length dictionaries and return
        result = {}
        result.update(length_dict)
        result.update(size_dict)
        return result