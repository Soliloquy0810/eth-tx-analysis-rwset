import requests
import os
import csv
import certifi
from collections import defaultdict
from utils import get_contract_address

def get_transactions_by_address(address, number_transactions):
    # sort=desc : get recent transactions
    url = "http://api.etherscan.io/api?module=account&action=txlist&address=" + address + \
    "&startblock=0&endblock=99999999&page=1&offset=" + str(number_transactions) + "&sort=desc"

    response = requests.get(url, verify=certifi.where())
    address_content = response.json()
    result = address_content.get("result")
    data = defaultdict(dict)
    
    for n, transaction in enumerate(result):
        blockNumber = transaction.get("blockNumber")
        timeStamp = transaction.get("timeStamp")
        hash = transaction.get("hash")
        nonce = transaction.get("nonce")
        blockHash = transaction.get("blockHash")
        tx_from = transaction.get("from")
        tx_to = transaction.get("to")
        value = transaction.get("value")
        gas = transaction.get("gas")
        input = transaction.get("input")
        cumulativeGasUsed = transaction.get("cumulativeGasUsed")
        gasUsed = transaction.get("gasUsed")
        methodId = transaction.get("methodId")
        functionName = transaction.get("functionName")
        functionName_noParas = str(functionName).split('(')[0]

        data[n]["blockNumber"] = blockNumber
        data[n]["timeStamp"] = timeStamp
        data[n]["hash"] = hash
        data[n]["nonce"] = nonce
        data[n]["blockHash"] = blockHash
        data[n]["from"] = tx_from
        data[n]["to"] = tx_to
        data[n]["value"] = value
        data[n]["gas"] = gas
        data[n]["input"] = input
        data[n]["cumulativeGasUsed"] = cumulativeGasUsed
        data[n]["gasUsed"] = gasUsed
        data[n]["methodId"] = methodId
        data[n]["functionName"] = functionName
        data[n]["functionName_noParas"] = functionName_noParas

    return data

addresses = get_contract_address()
n = len(addresses)
for i in range(0, n):
    cur_address = addresses.get(i)
    cur_file_path = os.path.abspath(os.getcwd())+"\\transactions\\"+str(i+1)+"-"+cur_address+".csv"
    if os.path.isfile(cur_file_path):
        continue
    
    txs = get_transactions_by_address(cur_address, 10000)

    # csv header
    fieldnames = ['blockNumber', 'timeStamp', 'hash', 'nonce', 'blockHash','from', 'to', \
                'value', 'gas', 'input', 'cumulativeGasUsed', 'gasUsed', 'methodId', 'functionName', 'functionName_noParas']

    with open(cur_file_path, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # if the size of current file is 0, then write header
        if not os.path.getsize(cur_file_path):
            writer.writeheader()
        
        n = len(txs)
        print(str(i+1)+"-current contract:"+cur_address+", tx counts:"+str(n))
        for i in range(0, int(n)):
            writer.writerow(txs.get(i))