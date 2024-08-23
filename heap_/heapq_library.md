# heapq库，实现了优先队列算法
1.heapq.heapify(x) 将list x 转换成堆，原地，线性时间内；<br>2.heapq.heappush(heap, item)    将 item 的值加入 heap 中，保持堆的不变性。
3.heapq.heappop(heap)    弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。
4.使用 heap[0] ，可以只访问最小的元素而不弹出它
5.heapq.heappushpop(heap, item)  将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。
6.heapq.heapreplace(heap, item)  弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。
7.heapq.merge(*iterables, key=None, reverse=False) 将多个已排序的输入合并为一个已排序的输出。返回已排序值的 iterator。
8.heapq.nlargest(n, iterable, key=None)  从 iterable 所定义的数据集中返回前 n 个最大元素组成的列表。 
9.heapq.nsmallest(n, iterable, key=None)   从 iterable 所定义的数据集中返回前 n 个最小元素组成的列表。
