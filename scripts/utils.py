import os
import csv
import pandas as pd
import numpy as np
from collections import defaultdict

# get all addresses from contract_address.csv
def get_contract_address():
    csv_path = os.path.abspath(os.getcwd())+"\\contract_address.csv"
    reader = csv.reader(open(csv_path))
    addresses = defaultdict(dict)

    i = 0
    for address in reader:
        contract_address = address[0]
        addresses[i] = contract_address
        i += 1

    return addresses

# get some info (including number, address, percentage) from contracts_top3_funcs.csv
def get_specific_info():
    contract_info_path = os.path.abspath(os.getcwd())+"\\contracts_top3_funcs.csv"
    
    all_contract_info = pd.read_csv(contract_info_path)
    number_address_percentage = all_contract_info[['number', 'address', 'percentage']]
    return number_address_percentage

# test = get_specific_info()
# print(test)