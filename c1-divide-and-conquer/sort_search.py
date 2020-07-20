# -*- coding: utf-8 -*-

import numpy as np
from merge_sort_count_inversions import merge_sort_count_inversion
import copy

def quick_sort(a,n):
    # base case
    if n==1 or n==0:
        return a, 0
    if n==2:
        if a[0]>a[1]:
            a[[0,1]] = a[[1,0]]
        return a, 1
    
    # define pivot
#    p = int(np.random.randint(n, size=1))
    med = list( sorted( [0,(n-1)//2, n-1] , key = lambda i:a[i] ) )
    p = med[1]
#    p = n-1
    v = a[p]
    a[[0,p]] = a[[p,0]]
    
    # partition
    i = 1
    for j in range(1,n):
        if a[j] < v:
            a[[i,j]] = a[[j,i]]
            i += 1
    a[[0,i-1]] = a[[i-1,0]]
    
    # subroutine
    a[0:i-1], cl = quick_sort(a[0:i-1], i-1)
    a[i:], cr = quick_sort(a[i:], n-i)
    
    # sorted array, number of comparisons
    return a, cl+cr+n-1
    
    
def linear_search(a,idx,n):
    # base case
    if n==1:
        return a[0], 0
    
    # define pivot
    p = int(np.random.randint(n, size=1))
    v = a[p]
    a[[0,p]] = a[[p,0]]
    
    # partition
    i = 1
    for j in range(1,n):
        if a[j] < v:
            a[[i,j]] = a[[j,i]]
            i += 1
    a[[0,i-1]] = a[[i-1,0]]
    
    if idx==i-1:
        return v, n-1
    if idx < i-1:
        sol, cl = linear_search(a[0:i-1], idx, i-1)
        return sol, cl+n-1
    if i-1 < idx:
        sol, cr = linear_search(a[i:], idx-i, n-i)
        return sol, cr+n-1
    
    


if __name__ == '__main__':
    f = open('data/QuickSort.txt', mode='r')
    data = f.readlines()
    f.close()
    x = np.zeros((len(data)))
    for i in range(len(data)):
        x[i] = int(data[i])
    
    xorigin = copy.copy(x)
    y1, n = merge_sort_count_inversion(x)
    y2, num_compare = quick_sort(x, x.size)
    
    print(x.size, int(x.size * np.log2(x.size)), num_compare)

    for i in range(10):
        idx = int(np.random.randint(x.size))
        x = copy.copy(xorigin)
        value, num_compare = linear_search(x, idx, x.size)
        print(idx+1,value, num_compare/x.size)