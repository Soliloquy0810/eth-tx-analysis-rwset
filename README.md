## 目的
- 对于以太坊上调用次数 top 1000 的合约，对每个合约获取其最近10000笔交易，并进行分析。
  - 交易获取时间为：2022年8月18日
- 对 top 1000 中的每个合约，统计得到其调用次数前3的方法。
- 对于上述每个方法，分析其进行的状态读写。

## 数据处理方式

- 使用脚本 `get_transactions_etherscan.py` 获取每个合约的交易数据。
  - 脚本中通过 [etherscan api](http://api.etherscan.io/api) 获取交易信息。
  - 每个交易文件中包含如下信息
```
blockNumber
timeStamp
hash
nonce
blockHash
from
to
value
gas
input
cumulativeGasUsed
gasUsed
methodId
functionName
functionName_noParas：对functionName只截取函数名、不保留形参信息
```
- 使用脚本 `frequent_function.py` 得到每个合约中调用次数前3的方法及具体调用次数，将其写入 `contracts_top3_funcs.csv` 。写入信息包含每个合约的：
```
number: 调用频率排名
address: 合约地址
percentage: 合约中被调用频率前3的方法占总调用次数的百分比
functionName1: 被调用频率第1的方法名称
times1: 被调用频率第1的方法的被调用次数
functionName2: 被调用频率第2的方法名称
times2: 被调用频率第2的方法的被调用次数
functionName3: 被调用频率第3的方法名称
times3: 被调用频率第3的方法的被调用次数
```
- 对于“被调用次数前 3 的方法的总调用次数”占合约总调用次数的比例未超过90%的合约，使用脚本 `print_all_func_counts.py` 将其所有方法的被调用次数打印到文件中。
- 使用脚本`contract_rw_statistics.py`打印临时分析结果。

## 文件说明
- `scripts`中为分析过程中使用的 python 脚本。
- `transactions`中为获取到的 top1000 合约对应的交易
  - 每个文件命名规则为：`调用频率排名-合约地址.csv`
- `contract_address.csv` 文件中是调用频率前1000的合约地址。
- `contracts_top3_funcs.csv`中为每个合约中，被调用次数前3的方法相关信息。


## 脚本执行环境
- python 3.9.2 64-bit
- numpy 1.23.2
- pandas 1.4.3

## 数据处理结果
- 成功获取 999 个合约的交易，1个合约的交易无法获取。
  - 调用频率第852的合约的交易无法获取（合约地址为0x4c6f947ae67f572afa4ae0730947de7c874f95ef）
- 对剩余 999 个合约中的每个合约，其中 48 个合约无法统计，原因是无法从交易中获取到其被调用的方法名称。另有 106 个合约只能从部分交易中获取到方法名称。
  - Function executed based on decoded input data. For undefined functions, method ID is displayed instead.
- “被调用次数前 3 的方法的总调用次数”平均约占合约总调用次数的 98.36%

## 合约分析
- 选择每个合约中最常被调用的方法进行分析
  - 若“被调用次数前 3 的方法的总调用次数”占合约总调用次数的比例超过90%，则只分析这3个方法中对状态变量的读写情况。
  - 若未超过90%（共 48 个合约未超过），则额外分析若干方法，直至总调用次数超过90% 。




