# -*- coding: utf-8 -*-


def knapsack(value, weight, n, w):
    """
    dynamic programming for knapsack problem, O(w) space, O(nw) time.
    """
    d = []
    for x in range(w+1):
        if weight[0] <= x: d.append(value[0])
        else: d.append(0)
    for i in range(1,n):
#        print(i)
        for x in range(w,weight[i]-1,-1):
            d[x] = max(d[x], d[x-weight[i]] + value[i])
    return d[-1]
    
    
if __name__ == '__main__':
    f = open('knapsack1.txt')
    data = f.readline().split(' ')
    w,n = int(data[0]), int(data[1])
    value, weight = [],[]
    for i in range(n):
        data = f.readline().split(' ')
        value.append(int(data[0]))
        weight.append(int(data[1]))
    f.close()
    
    sol = knapsack(value, weight, n,w)
    print(sol)