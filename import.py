import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

test = 'oppo 3.4inch 35GB SUPER VALUE' #value taken from scraper 

#data = pd.read_csv(r'./productkey.csv', usecols= [0]) #read from CSV, only use col 0 (brand)
data = pd.read_csv(r'./productkey.csv') #read from CSV

brand = (data['brand'].unique()) #gets list of brand names from PS dbase (note lowercase names)

i = 0
while i < 15: #15 is the number of brands (can be made better)
    if (fuzz.token_set_ratio(test, brand[i]) == 100): # > 90 for fuzzy matching of brand name (not recommended)
        print(brand[i])
        break
    else:
        i = i + 1

#output here will be brand name match, using this we can search only within the 
# respective brand fr he fuzzy matching.

