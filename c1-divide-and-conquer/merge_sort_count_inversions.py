# -*- coding: utf-8 -*-

import numpy as np
import time

def count_inversion(x):
    n = x.size
    y = 0
    for i in range(n):
        for j in range(n):
            if (i<j) and (x[i] > x[j]):
                y += 1
    return y

def merge_sort_count_inversion(x):
    """
    n,m1,m2 : sizes
    s,s1,s2 : sorted arrays
    y,y1,y2 : number of inversions
    i,j : pointers
    """
    n = x.size
    if n==0:
        return x,0
    if n==1:
        return x,0
    m1 = n//2
    m2 = n - m1
    s1,y1 = merge_sort_count_inversion(x[0:m1])
    s2,y2 = merge_sort_count_inversion(x[m1:])
    
    i,j = 0,0
    y = 0
    s = np.zeros(x.shape)
    for k in range(n):
        if j >= m2:
            s[k] = s1[i]
            i += 1
            continue
        if i >= m1:
            s[k] = s2[j]
            j += 1
            continue
        if s1[i]<= s2[j]:
            s[k] = s1[i]
            i += 1
        else:
            s[k] = s2[j]
            j += 1
            y += m1 - i
    return s , y+y1+y2

if __name__ == '__main__':
#    x = np.random.permutation(np.arange(10))
#    y,n = merge_sort_count_inversion(x)
#    print(x)
#    print(y)
#    print(n , count_inversion(x))
    
    f = open('data/IntegerArray.txt', mode='r')
    data = f.readlines()
    f.close()
    x = np.zeros((len(data)))
    
    for i in range(len(data)):
        x[i] = int(data[i])
    start = time.clock()
    y, n = merge_sort_count_inversion(x)
    end = time.clock()
    print(start, end, n)
    
    
    y,n = count_inversion(x)
#    size = np.exp2(np.arange(10,17))
#    for i in range(size.size):
#        start = time.clock()
#        y,n = merge_sort_count_inversion(x[0:int(size[i])])
#        end = time.clock()
#        print(end-start, n)
        
