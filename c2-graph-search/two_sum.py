# -*- coding: utf-8 -*-
"""
two sum, 
given: an array a, interval [a,b],
goal: count the number of two-sums falling in [a,b] in linear time.
"""

def two_sum(arr, a,b):
    qualified = [False for i in range(b-a+1)]
    dic = dict()
    for elem in arr:
        x = elem - a
        q, r = x // (b-a+1), x % (b-a+1)
        if q in dic:
            dic[q].append(r)
        else:
            dic[q] = [r]
    
    for y in arr:
        q, r = y // (b-a+1), y % (b-a+1)
        if -1-q in dic:
            for rx in dic[-1-q]:
                twosum = -(b-a+1) + r + rx
                if twosum >= 0 and twosum <= b-a: qualified[twosum] = True
        if -q in dic:
            for rx in dic[-q]:
                twosum = r + rx
                if twosum >= 0 and twosum <= b-a: qualified[twosum] = True
                
    c = len([i for i in qualified if i])
    return c
    

if __name__ == '__main__':
    import random
    a,b = -10000, 10000
    M = 10 ** 13
    n = 640000
    arr = [random.randint(-M,M) for i in range(n)]
    t = two_sum(arr, a, b)
    print(t)