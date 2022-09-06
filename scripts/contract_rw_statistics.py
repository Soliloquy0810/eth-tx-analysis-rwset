import os
import xlrd2

# open xlxs file
xlsx_file_path = os.path.abspath(os.getcwd())+"\\analysis\\4-function_analysis.xlsx"
workbook = xlrd2.open_workbook(xlsx_file_path)

# get sheet data
sheet1 = workbook.sheet_by_name(sheet_name='Sheet1')

# get colums
contract_function_col = sheet1.col_values(colx=0)
normal_read_col = sheet1.col_values(colx=1)
normal_write_col = sheet1.col_values(colx=2)
normal_read_write_col = sheet1.col_values(colx=3)
map_state_add_col = sheet1.col_values(colx=4)
hotspot_state_add_col = sheet1.col_values(colx=5)
map_state_sub_col = sheet1.col_values(colx=6)
hotspot_state_sub_col = sheet1.col_values(colx=7)
branch_state_read_col = sheet1.col_values(colx=8)
branch_state_write_col = sheet1.col_values(colx=9)
branch_state_read_write_col = sheet1.col_values(colx=10)
is_map_col = sheet1.col_values(colx=11)

# delete header
del(contract_function_col[0])
del(normal_read_col[0])
del(normal_write_col[0])
del(normal_read_write_col[0])
del(map_state_add_col[0])
del(hotspot_state_add_col[0])
del(map_state_sub_col[0])
del(hotspot_state_sub_col[0])
del(branch_state_read_col[0])
del(branch_state_write_col[0])
del(branch_state_read_write_col[0])
del(is_map_col[0])

n = len(contract_function_col)

# Count the total number of each column
quantity_normal_read = 0
quantity_normal_write = 0
quantity_normal_read_write = 0
quantity_map_state_add = 0
quantity_hotspot_state_add = 0
quantity_map_state_sub = 0
quantity_hotspot_state_sub = 0
quantity_branch_state_read = 0
quantity_branch_state_write = 0
quantity_branch_state_read_write = 0
quantity_is_map = 0

for i in range(n):
    quantity_normal_read += normal_read_col[i]
    quantity_normal_write += normal_read_col[i]
    quantity_normal_read_write += normal_read_write_col[i]
    quantity_map_state_add += map_state_add_col[i]
    quantity_hotspot_state_add += hotspot_state_add_col[i]
    quantity_map_state_sub += map_state_sub_col[i]
    quantity_hotspot_state_sub += hotspot_state_sub_col[i]
    quantity_branch_state_read += branch_state_read_col[i]
    quantity_branch_state_write += branch_state_write_col[i]
    quantity_branch_state_read_write += branch_state_read_write_col[i]
    quantity_is_map += is_map_col[i]


print("### the quantity of all reads and writes is " + str(int(quantity_normal_read + quantity_normal_write + \
        2*quantity_normal_read_write + 2*quantity_map_state_add + 2*quantity_hotspot_state_add + \
            2*quantity_map_state_sub + 2*quantity_hotspot_state_sub + quantity_branch_state_read + \
                quantity_branch_state_write + 2*quantity_branch_state_read_write)))

print("### the quantity of all reads and writes is " + str(int(quantity_normal_write + quantity_normal_read_write + \
        quantity_map_state_add + quantity_hotspot_state_add + quantity_map_state_sub + \
            quantity_hotspot_state_sub + quantity_branch_state_write)))

print("### the quantity of normal_read is " + str(int(quantity_normal_read)))
print("### the quantity of normal_write is " + str(int(quantity_normal_write)))
print("### the quantity of normal_read_write is " + str(int(quantity_normal_read_write)))
print("### the quantity of map_state_add is " + str(int(quantity_map_state_add)))
print("### the quantity of hotspot_state_add is " + str(int(quantity_hotspot_state_add)))
print("### the quantity of map_state_sub is " + str(int(quantity_map_state_sub)))
print("### the quantity of hotspot_state_sub is " + str(int(quantity_hotspot_state_sub)))
print("### the quantity of branch_state_read is " + str(int(quantity_branch_state_read)))
print("### the quantity of branch_state_write is " + str(int(quantity_branch_state_write)))
print("### the quantity of branch_state_read_write is " + str(int(quantity_branch_state_read_write)))
print("### the quantity of is_map is " + str(int(quantity_is_map)))

# split "contract_function_col"
contract_no_col = []
functin_name_col = []
for i in range(n):
    (str1, str2) = contract_function_col[i].split("-", 1)
    contract_no_col.append(int(str1))
    functin_name_col.append(str2)

pre_contract_quantity = list(set(contract_no_col))
print("### (before)the quantity of contracts is " + str(len(pre_contract_quantity)))

operate_contract_no_col_hotspot = []
for item in contract_no_col:
    operate_contract_no_col_hotspot.append(item)
operate_functin_name_col_hotspot = []
for item in functin_name_col:
    operate_functin_name_col_hotspot.append(item)
hotspot_state = []

# merge "hotspot_state_add" and "hotspot_state_sub"
for i in range(n):
    hotspot_state.append(int(hotspot_state_add_col[i] + hotspot_state_sub_col[i]))

# delete rows where the value of hotspot_state[i] is 0
# row i contains operate_contract_no_col_hotspot[i], operate_functin_name_col_hotspot[i] and hotspot_state[i]
for i in range(n-1, -1, -1):
    if(hotspot_state[i] == 0):
        del(operate_contract_no_col_hotspot[i])
        del(operate_functin_name_col_hotspot[i])
        del(hotspot_state[i])

# print results (hotspot)
current_n = len(operate_functin_name_col_hotspot)
print("### hotspot: the quantity of rows now is " + str(current_n))

current_contract_no = list(set(operate_contract_no_col_hotspot))
print("### hotspot: (after) the quantity of contracts is " + str(len(current_contract_no)))

branch_state = []
# merge "branch_state_write" and "branch_state_read_write"
for i in range(n):
    branch_state.append(int(branch_state_write_col[i] + branch_state_read_write_col[i]))

# delete rows where the value of branch_state[i] is 0
# row i contains contract_no_col[i], functin_name_col[i] and branch_state[i]
for i in range(n-1, -1, -1):
    if(branch_state[i] == 0):
        del(contract_no_col[i])
        del(functin_name_col[i])
        del(branch_state[i])

# print results (branch)
current_n = len(functin_name_col)
print("### branch: the quantity of rows now is " + str(current_n))

current_contract_no = list(set(contract_no_col))
print("### branch: (after) the quantity of contracts is " + str(len(current_contract_no)))



