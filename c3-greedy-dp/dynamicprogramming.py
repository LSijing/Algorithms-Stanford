# -*- coding: utf-8 -*-



def mwis(weight):
    n = len(weight)
    d = [0]
    d.append(weight[0])
    for i in range(2,len(weight)+1):
        d.append( max(d[i-1], d[i-2]+weight[i-1]) )
    
    exist = ''
    i = n-1
    while i >=  0:
        if d[i+1] == d[i]:
            exist = '0' + exist
            i -= 1
        else:
            exist = '01' + exist
            i -= 2
    if i == -2:
        exist = exist[1:]
    return exist


def knapsack(value, weight, n, w):
    d = []
    for x in range(w+1):
        if weight[0] <= x: d.append(value[0])
        else: d.append(0)
    for i in range(1,n):
        print(i)
        for x in range(w,weight[i]-1,-1):
            d[x] = max(d[x], d[x-weight[i]] + value[i])
    return d[-1]
    
def knapsack_recursive(value, weigth, n, w):
    if n == 0: return 0
    if w < 0: return 0
    exclude = knapsack_recursive(value, weight, n-1, w)
    if w - weight[n-1] >= 0:
        include = knapsack_recursive(value, weight, n-1, w-weight[n-1]) + value[n-1]
    else:
        include = 0
    return max(exclude,include)
    
    
if __name__ == '__main__':
    # knapsack problem
#    num_file = '40_1000000_2000'
#    f = open('stanford-algs-master/testCases/course3/assignment4Knapsack/input_random_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course3/assignment4Knapsack/output_random_'+num_file+'.txt').readlines()
    f = open('data/knapsack_big.txt')
    data = f.readline().split(' ')
    w,n = int(data[0]), int(data[1])
    value, weight = [],[]
    for i in range(n):
        data = f.readline().split(' ')
        value.append(int(data[0]))
        weight.append(int(data[1]))
    
    sol = knapsack(value, weight, n,w)
#    sol_2 = knapsack_recursive(value, weight, n ,w)
    print(sol)
    
#    # maximum weighted independent set
#    num_file = '45_10000'
#    f = open('stanford-algs-master/testCases/course3/assignment3HuffmanAndMWIS/question3/input_random_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course3/assignment3HuffmanAndMWIS/question3/output_random_'+num_file+'.txt').readlines()
#    f = open('data/mwis.txt')
#    n = int(f.readline())
#    weight = []
#    for i in range(n):
#        data = f.readline()
#        
#        w = float(data)
#        weight.append(float(w))
#        
#    sol = mwis(weight)
#    pos = [1, 2, 3, 4, 17, 117, 517, 997]
#    res = ''
#    for i in pos:
#        if i <= n:
#            res = res + sol[i-1]
#        else:
#            res = res + '0'
#            
#    print(res)