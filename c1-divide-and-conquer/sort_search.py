# -*- coding: utf-8 -*-

"""
quick sort, count number of comparisons in it.
linear time search the k-th smallest element in an unsorted array.
"""
import math
import random
import copy

def quick_sort(a,start,end,pivot='r'):
    """
    a[start],a[end] included
    pivot == 
    'r' random pivot
    'first' first element, a[start]
    'last' last element, a[end]
    'med' median of a[start],a[end],a[(start+end)//2]
    """
    # base case
    n = end + 1 - start
    if n <= 1: return a, 0
    if n == 2:
        if a[start] > a[end]:
            a[start], a[end] = a[end], a[start]
        return a, 1
    
    # define pivot
    if pivot == 'first':
        p = start
    elif pivot == 'last':
        p = end
    elif pivot == 'med':
        p_s = list(sorted( [start, (start+end)//2, end], key= lambda i:a[i]))
        p = p_s[1]
    else:
        p = random.randint(start,end)
            
    v = a[p]
    a[start], a[p] = a[p], a[start]
    
    # partition
    i = start + 1
    for j in range(start+1,end+1):
        if a[j] < v:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[start], a[i-1] = a[i-1], a[start]
    
    # subroutine
    _, cl = quick_sort(a, start, i-2, pivot)
    _, cr = quick_sort(a, i, end, pivot)
    
    # sorted array, number of comparisons
    return a, cl+cr+n-1
    
    
def linear_search(a,start,end,idx):
    n = end + 1 - start
    # base case
    if n == 1: return start, 0
    
    # define pivot
    p = random.randint(start,end)
    v = a[p]
    a[start], a[p] = a[p], a[start]
    
    # partition
    i = start + 1
    for j in range(start+1,end+1):
        if a[j] < v:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[start], a[i-1] = a[i-1], a[start]
    
    if idx == i - start:
        return i-1, n-1
    if idx < i - start:
        pos, cl = linear_search(a, start, i-2, idx)
        return pos, cl+n-1
    if i - start < idx:
        pos, cr = linear_search(a, i, end, idx-i+start)
        return pos, cr+n-1
    
    


if __name__ == '__main__':
    #random.seed(10)
    n = 100000
    x = [random.randint(0,n) for i in range(n)]
    y = copy.copy(x)
    _, num_compare = quick_sort(x, 0,len(x)-1, 'med')
    print( sorted(y)==x, int(len(x) * math.log2(len(x))), num_compare/len(x)/math.log2(len(x)) )

    for i in range(5):
        idx = random.randint(1,len(x))
        x = [random.randint(0,n) for i in range(n)]
        y = copy.copy(x)
        i, num_compare = linear_search(x,0,len(x)-1,idx)
        value = x[i]
        stat = sorted(y)[idx-1]
        print(stat==value, num_compare/len(x))