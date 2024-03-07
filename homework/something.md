# 作业中的一些数据结构整理
## Stack
1、基础类型 list，实体 ```list```

2、操作：

### push : 
```
stack.push(item)
```
无返回值

### pop:
```
stack.pop()
```
返回弹出的栈顶元素

### isEmpty:
```
stack.isEmpty()
```
返回栈是否为空

## Queue
1、基础类型 list，实体 ```list```

2、操作：

### push:
```
queue.push(item)
```
无返回值

### pop:
```
queue.pop()
```
返回弹出的队首元素

### isEmpty:
```
stack.isEmpty()
```
返回栈是否为空

## PriorityQueue
1、基础类型 heapq, int，实体```heap, count```

2、操作：

### push:
```
heap.push(item, priority)
```
放入优先队列的实际是一个元组，由priority, count, item组成

### pop:
```
heap.pop()
```
弹出的是元素，返回的只有item

### update:
```
heap.update(item, priority)
```
更新优先队列的元素，如果变小了应该更新并重新排列优先队列，否则不动

## PriorityQueueWithFunction
1、从PriorityQueue继承而来，基础类型 函数，实体 ```PriorityQueue```, priorityFunction
2、操作：

改写了push，通过priorityFunction计算出item的priority, 在调用PriorityQueue的push函数，其他使用PriorityQueue的相关函数
