# -*- coding: utf-8 -*-

import numpy as np
import math


def combitorial(n,p,s=0):
    if n - s < p : return []
    if n - s == p: return [[i for i in range(s,n)]]
    if p == 0: return [[]]
    if p == 1: return [[i] for i in range(s,n)]
    sol = []
    for i in range(s,n):
        res = combitorial(n,p-1,i+1)
        for x in res:
            x.insert(0,i)
            sol.append(x)
    return sol
    
def combi_to_int(s):
    i = 0
    for x in s: i += 2 ** x
    return i

def tsp_dp(x,y,n):
    if n == 0 or n == 1: return 0
    if n == 2: return 2*np.sqrt((x[0] - x[1])**2 + (y[0] - y[1]) ** 2)
    l = [ [math.inf for _ in range(n)] for _ in range(2**n)]
    l[1][0] = 0
    adjmatrix = [ [math.sqrt((x[i] - x[j])**2 + (y[i] - y[j]) ** 2) for j in range(n)] for i in range(n)]
    for k in range(1,n):
        combi = combitorial(n,k+1)
        for s in combi:
            idx_s = combi_to_int(s)
            for j in s:
                temp = s.copy()
                temp.remove(j)
                idx = idx_s - 2 ** j
                mini = math.inf
                #print(s,temp,idx)
                for mid in temp: mini = min(mini,l[idx][mid] + adjmatrix[mid][j])
                #print(mini)
                l[idx_s][j] = mini
                
    cycle = math.inf
    for i,dist in enumerate(l[-1]):
        cycle = min(cycle, dist + adjmatrix[0][i] ) 
    return cycle
    
def tsp_heuristic(x,y,n,s=0):
    if n == 0 or n == 1: return 0
    if n == 2 : return 2*np.sqrt((x[0] - x[1])**2 + (y[0] - y[1]) ** 2)
    tour = 0
    prev = s
    unvisited = [j for j in range(n)]
    unvisited.remove(s)
    for k in range(n-1):
        curr = min(unvisited , key= lambda j: (x[prev] - x[j]) ** 2 + (y[prev] - y[j]) ** 2)
        unvisited.remove(curr)
        tour += math.sqrt( (x[prev] - x[curr]) ** 2 + (y[prev] - y[curr]) ** 2 )
        prev = curr
    tour += math.sqrt( (x[prev] - x[s]) ** 2 + (y[prev] - y[s]) ** 2 )
    return tour
        
    
    
    
if __name__ == '__main__':
#    num_file = '64_10000'
#    f = open('stanford-algs-master/testCases/course4/assignment3TSPHeuristic/input_simple_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course4/assignment3TSPHeuristic/output_simple_'+num_file+'.txt').readlines()
    f = open('data/nn.txt')
    data = f.readline()
    n = int(data)
    x,y = [],[]
    for i in range(n):
        data = f.readline().split(' ')
        x.append(float(data[1]))
        y.append(float(data[2]))
        
    sol = tsp_heuristic(x,y,n)
    print(sol)
        
        
#if __name__ == '__main__':
#    num_file = '73_20'
#    f = open('stanford-algs-master/testCases/course4/assignment2TSP/input_float_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course4/assignment2TSP/output_float_'+num_file+'.txt').readlines()
#    f = open('data/tsp.txt')
#    data = f.readline()
#    n = int(data)
#    x,y = [],[]
#    for i in range(n):
#        data = f.readline().split(' ')
#        x.append(float(data[0]))
#        y.append(float(data[1]))
#    
#    sol = tsp_dp(x,y,n)
#    print(sol)
##    print(sol,output)
