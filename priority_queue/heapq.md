# 堆排列算法——heapq
## heapq是python的一个模块，实现了堆排列算法，即优先队列算法
堆是一棵完全二叉树，其中每个节点的值都小于等于其各个子节点的值。这个使用数组的实现，索引从 0 开始，且对所有的 k 都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]。比较时不存在的元素被认为是无限大。堆最有趣的特性在于最小的元素总是在根结点：heap[0]。
## 堆的创建
要创建一个堆，可以新建一个空列表 []，或者用函数 heapify() 把一个非空列表变为堆。
## 一些常用的函数

1、将item放入堆heap中
```
heapq.heappush(heap, item)
```
2、弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。
```
heapq.heappop(heap)
```
使用 heap[0] ，可以只访问最小的元素而不弹出它。

3、将 item 放入堆中，然后弹出并返回 heap 的最小元素。
```
heapq.heappushpop(heap, item）
```
该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。注意这里是先放入 item 在弹出，也就是说弹出时要考虑 itme 。

4、将list x 转换成堆，原地，线性时间内。
```
heapq.heapify(x)
```
5、弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。
```
heapq.heapreplace(heap, item)
```
这个单步骤操作比 heappop() 加 heappush() 更高效，并且在使用固定大小的堆时更为适宜。 pop/push 组合总是会从堆中返回一个元素并将其替换为 item。
注意这里时先弹出在放入 item ，所以弹出的值可能比 item 大。
