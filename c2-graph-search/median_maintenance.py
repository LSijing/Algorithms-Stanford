# -*- coding: utf-8 -*-

from data_structure import Heap

def med_series(nums):
    minheap = Heap()
    maxheap = Heap(heaptype='max')
    n = 0
    median = []
    for x in nums:
        if n % 2 == 0:
            right = minheap.extract_root()
            if right is None or x <= right:
                maxheap.insert(x)
            else:
                minheap.delete_root()
                minheap.insert(x)
                maxheap.insert(right)
        else:
            left = maxheap.extract_root()
            if left <= x:
                minheap.insert(x)
            else:
                maxheap.delete_root()
                maxheap.insert(x)
                minheap.insert(left)
        n += 1
        m = maxheap.extract_root()
        median.append(m)
    print(sum(median) % 10000)
    return median
    
