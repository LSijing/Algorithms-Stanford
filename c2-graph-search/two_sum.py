# -*- coding: utf-8 -*-



import numpy as np



if __name__ == '__main__':
    a,b = -10000, 10000
    num_file = '60_160000'
#    f = open('stanford-algs-master/testCases/course2/assignment4TwoSum/input_random_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course2/assignment4TwoSum/output_random_'+num_file+'.txt')
    f = open('data/2sum.txt')
    data = f.readlines()
    qualified = [False for i in range(b-a+1)]
    # create hash table (quotient,remainders list)
    dic = dict()
    for idx,s in enumerate(data):
        x = int(s) - a
        q, r = x // (b-a+1), x % (b-a+1)
        if q in dic:
            dic[q].append(r)
        else:
            dic[q] = [r]
        
    # enumerate data
    for idx,s in enumerate(data):
        x = int(s)
        q,r = x // (b-a+1), x % (b-a+1)
        if -1-q in dic:
            for idx,r2 in enumerate(dic[-1-q]):
                res = (b-a+1) * -1 + r + r2
                if res >= 0 and res <= (b-a):
                    qualified[res] = True
        if -q in dic:
            for idx,r2 in enumerate(dic[-q]):
                res = r+r2
                if res >= 0 and res <= (b-a):
                    qualified[res] = True
                    
    
    t = 0 
    for i in range(len(qualified)):
        if qualified[i]:
            t += 1
    print(t)
#    print(t,output.readlines())
        
#    for i,(k,v) in enumerate(dic.items()):
#        print(k*(b-a+1)+v[0] + a - int(data[i]))