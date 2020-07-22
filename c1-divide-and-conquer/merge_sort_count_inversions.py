# -*- coding: utf-8 -*-

"""
count number of inversions in an array, i.e. i < j and a[i] > a[j],
using merge sort
"""

import time
import random

def count_inversion(x):
    n = len(x)
    y = 0
    for i in range(n):
        for j in range(n):
            y += 1 if i < j and x[i] > x[j] else 0
    return y

def merge_sort_count_inversion(x):
    """
    n,m1,m2 : sizes
    s,s1,s2 : sorted arrays
    y,y1,y2 : number of inversions
    i,j : pointers
    """
    n = len(x)
    if n == 0: return x,0
    if n == 1: return x,0
    m1 = n//2
    m2 = n - m1
    s1,y1 = merge_sort_count_inversion(x[0:m1])
    s2,y2 = merge_sort_count_inversion(x[m1:])
    
    i,j = 0,0
    y = 0
    s = []
    for k in range(n):
        if j >= m2:
            s.extend(s1[i:])
            break
        if i >= m1:
            s.extend(s2[j:])
            break
        if s1[i] <= s2[j]:
            s.append(s1[i])
            i += 1
        else:
            s.append(s2[j])
            j += 1
            y += m1 - i
    return s , y+y1+y2



if __name__ == '__main__':
    N = 2**20
    n = 1000
    x = [random.randint(0,N) for i in range(n)]
    y,n = merge_sort_count_inversion(x)
    # correctness
    print(sorted(x)==y)
    print(n , count_inversion(x))
    
    # running time
    x.extend([random.randint(0,N) for i in range(N)])
    size = list(map(lambda i:2**i,range(14,21)))
    for i in size:
        start = time.clock()
        y,n = merge_sort_count_inversion(x[0:i])
        end = time.clock()
        print(end-start, (end-start)/i)
        
