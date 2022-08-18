import os
import csv
import pandas as pd
import numpy as np
from collections import Counter
from utils import get_contract_address

def get_frequent_functions(addresses):
    csv_path = os.path.abspath(os.getcwd())+"\\contracts_top3_funcs.csv"
    fieldnames = ['number', 'address', 'percentage', 'functonName1', 'times1', \
                    'functonName2', 'times2', 'functonName3', 'times3']
    
    csv_file = open(csv_path, mode='a', newline='', encoding='utf-8-sig')
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # if the size of current file is 0, then write header
    if not os.path.getsize(csv_path):
        csv_writer.writeheader()

    n = len(addresses)
    for i in range(0, n):
        cur_address = addresses.get(i)
        contract_tx_path = os.path.abspath(os.getcwd())+"\\transactions\\"+str(i+1)+"-"+str(cur_address)+".csv"
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
        top3_funcs = function_counts.most_common(3)
        print(str(i+1)+"-"+cur_address+":"+str(top3_funcs))
        
        func_num = len(top3_funcs)
        # set field values
        number = i+1
        
        if func_num==3:
            percentage = (top3_funcs[0][1]+top3_funcs[1][1]+top3_funcs[2][1]) / 10000
            csv_writer.writerow({"number":number, "address":cur_address, "percentage":percentage, \
                "functonName1":top3_funcs[0][0],"times1":top3_funcs[0][1],"functonName2":top3_funcs[1][0], \
                    "times2":top3_funcs[1][1],"functonName3":top3_funcs[2][0],"times3":top3_funcs[2][1]})
        elif func_num==2:
            percentage = (top3_funcs[0][1]+top3_funcs[1][1]) / 10000
            csv_writer.writerow({"number":number, "address":cur_address, "percentage":percentage, \
                "functonName1":top3_funcs[0][0],"times1":top3_funcs[0][1],"functonName2":top3_funcs[1][0], \
                    "times2":top3_funcs[1][1]})
        elif func_num==1:
            percentage = (top3_funcs[0][1]) / 10000
            csv_writer.writerow({"number":number, "address":cur_address, "percentage":percentage, \
                "functonName1":top3_funcs[0][0],"times1":top3_funcs[0][1]})
        else:
            csv_writer.writerow({"number":number, "address":cur_address})

    csv_file.close()



addresses = get_contract_address()
get_frequent_functions(addresses)
