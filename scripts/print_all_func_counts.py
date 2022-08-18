import os
import pandas as pd
import numpy as np
from collections import Counter
from utils import get_specific_info

def print_frequent_functions(specific_number_address_percentage):
    txt_path = os.path.abspath(os.getcwd())+"\\contracts_all_func_counts.txt"
    file = open(txt_path, 'w+')

    n = len(specific_number_address_percentage)
    for i in range(0, n):
        cur_number = specific_number_address_percentage[i][0]
        cur_address = specific_number_address_percentage[i][1]
        contract_tx_path = os.path.abspath(os.getcwd())+"\\transactions\\"+str(cur_number)+"-"+str(cur_address)+".csv"
        if not os.path.isfile(contract_tx_path):
            continue
        
        all_tx_info = pd.read_csv(contract_tx_path)
        # get all 'functionName_noParas' from every txs file, and transform it(DataFrame) into list
        all_function_name = all_tx_info[['functionName_noParas']]
        function_name_array = np.array(all_function_name)
        function_name_list_raw = function_name_array.tolist()
        function_name_list = []
        for func_item in function_name_list_raw:
            function_name_list.append(func_item[0])
        
        function_counts = Counter(function_name_list)
        print(str(i+1)+"-"+str(cur_number)+"-"+str(cur_address))
        file.write(str(cur_number)+"-"+str(cur_address)+":\n")
        file.write(str(function_counts))
        file.write('\n\n')

    file.close()


def get_contracs_lower_90_percent(number_address_percentage):
    array_form = np.array(number_address_percentage)
    list_form = array_form.tolist()

    i = 0
    result = []
    for p in list_form:
        if  0.9 > list_form[i][2] and list_form[i][2] > 0.5:
            result.append([list_form[i][0], list_form[i][1], list_form[i][2]])
        i += 1

    return result




number_address_percentage = get_specific_info()
specific_number_address_percentage = get_contracs_lower_90_percent(number_address_percentage)
# print(specific_number_address_percentage)
print_frequent_functions(specific_number_address_percentage)