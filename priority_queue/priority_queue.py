import heapq

class PriorityQueue :

    def __init__(self) :
        self._queue = [] # 堆
        self._index = 0 # 索引

    def insert(self, item, priority) : # insert item and its priority at the same time
        heapq.heappush(self._queue, (priority, self._index, item)) # push into the heap 
        # 放入的是一个元组，排序是根据元组的第0个元素 priority ，第1个元素是索引，最后一个是真正要排序的元素或节点，排序时根据第0个元素，也就是priority排序
        self._index += 1 # 索引，最后堆的总数

    def remove(self) :
        return heapq.heappop(self._queue)[-1] # 弹出队首的元素
    
    def is_empty(self) :
        return len(self._queue) == 0 # 判断队列是否为空
    
    def front(self) :
        return self._queue[0][-1] # 取出队首的元素
