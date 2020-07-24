# -*- coding: utf-8 -*-
"""
1. Floyd-Warshall all pairs shortest path algorithm.
2. Johnson's algorithm, 
    using Bellman-Ford for detecting negative cycle, reweighting,
    using Dijkstra for all single source shortest paths.
"""

import copy
import math
import dijkstra

def load_data(filename):
    f = open(filename)
    data = f.readline().split(' ')
    n,m = int(data[0]), int(data[1])
    dic = dict()
    for i in range(m):
        data = f.readline().split(' ')
        left = int(data[0]) - 1
        right = int(data[1]) - 1
        length = int(data[2])
        if (left,right) not in dic or ( (left,right) in dic and length < dic[(left,right)] ):
            dic[(left,right)] = length
    f.close()
    return dic,n
    

def floyd(edgedict,n):
    """
    O(n^3) time, O(n^2) space, Floyd all pairs shortest path.
    """
    # initialize
    d = [[math.inf for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i,j) in edgedict: d[i][j] = edgedict[(i,j)]
    # dynamic programming
    for k in range(n):
        dist = copy.deepcopy(d)
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(d[i][j], d[i][k] + d[k][j])
        d = dist
    
    return d


def bellman_ford(edgedict,n,s=0):
    """
    Bellman Ford shortest path, O(n) space, O(mn) time.
    """
    innodes = []
    for i in range(n):
        innodes.append([])
        for j in range(n):
            if (j,i) in edgedict: innodes[-1].append(j)
    # initialize
    a = []
    for i in range(n):
        if (s,i) in edgedict: a.append(edgedict[(s,i)])
        else: a.append(math.inf)
    # dynamic programming
    for k in range(n):
        b = []
        for i in range(n):
            shortest = a[i]
            for w in innodes[i]:
                shortest = min(shortest, edgedict[(w,i)] + a[w])
            b.append(shortest)
        if k != n-1:
            a = b
        else:
            if a != b:
                print('bellman-ford negative cycle')
                return None
    
    return a


def johnson(edgedict,n):
    """
    one Bellman-Ford O(mn), n Dijkstra O(n*m*log(n)), n^2 pairwise distances O(n^2).
    """
    # 1. create G' by adding a new source
    Gprime = copy.deepcopy(edgedict)
    for i in range(n): Gprime[(n,i)] = 0
    # 2. compute shortest path via bellman-ford, if negative cycle, halt
    reweight = bellman_ford(Gprime,n+1,s=n)
    if reweight is None: return reweight
    reweight = reweight[0:-1]
    # 3. create adjacency list with modified edge lengths
    adjlist = [[] for i in range(n)]
    lengths = [[] for i in range(n)]
    for (i,j),value in edgedict.items():
        adjlist[i].append(j)
        lengths[i].append(value + reweight[i] - reweight[j])
    # 4. repeat Dijkstra for every sources
    dist = []
    for s in range(n):
        temp = dijkstra.dijkstra(adjlist, lengths, s)
        dist.append(temp)
    # 5. recover real distance
    for i in range(n):
        for j in range(n):
            dist[i][j] += reweight[j] - reweight[i]
    return dist
    
    
if __name__ == '__main__':
    f = 'g3.txt'
    edgedict,n = load_data(f)
    
    # Johnson's 
    dist = johnson(edgedict,n)
    if not dist:
        print('Johnson NULL')
    else:
        shortest = dist[0][0]
        for x in dist:
            shortest = min(shortest,min(x))
        print(shortest)
    
    # Floyd
    d = floyd(edgedict,n)
    q = True
    for i in range(n):
        if d[i][i] < 0 : 
            q = False
            break
    if not q : print('Floyd NULL')
    else:
        shortest = d[0][0]
        for x in d:
            shortest = min(shortest,min(x))
        print(shortest)
