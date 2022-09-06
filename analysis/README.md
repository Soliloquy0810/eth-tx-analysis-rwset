
# 符号说明

- `@normal_read`：普通读取，

- `@normal_write`：普通写入，即除`@branch_state_write`以外的写入

- `@map_state_add`：map状态变量读写（+=），针对map的key是user address的情况。

- `@hotspot_state_add`：热点状态变量读写（+=）

- `@map_state_sub`：map状态变量读写（-=），针对map的key是user address的情况。

- `@hotspot_state_sub`：热点状态变量读写（-=）

- `@branch_state_read`：在分支中读取状态变量

- `@branch_state_write`：在分支中写入状态变量

- `@branch_state_read_write`：在分支中读写状态变量

- `@is_map`：是对`@normal_read`和`@normal_write`的额外标注（不包含`@map_state_add`和`@map_state_sub`）。针对map的key是address的情况，即`map(address=>datatype)`。

- `@call(functionName)`：调用名称为functionName的方法。

- `@notConsider`：暂未考虑被标注部分的读写

- `@duplacate_branch_hotspot`：既在分支中，同时又是hotspot。

# 其他情况处理

- 对于每个方法中重复的读写，只记为 1 次。对结构体的读写也只记为 1 次（除特殊情况外，例如结构体实例中保存的是合约全局的状态）。

- 未考虑跨合约调用的读写情况。

- 对于多个方法调用同一个方法的情况，读写分别计算。例如transfer()和transferFrom()都调用super.transfer()，那么super.transfer()中的读写分别计算。

- modifier中需要访问的状态变量被考虑在内。

- Read和Write合并为ReadWrite。

- 对于在循环中出现的对状态的访问，记为 1 次访问。对于循环中出现的if-else分支，不算作分支。
