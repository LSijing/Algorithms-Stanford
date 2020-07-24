# -*- coding: utf-8 -*-

"""
k-clustering problems.
1. compute maximum spacing of 4-clustering.
2. compute max number of clusters, i.e. maximal k, s.t. max spacing >= 3.
"""

import time
from data_structures import UnionFind

def load_data(filename, dtype='edges'):
    if dtype == 'edges':
        f = open(filename)
        n = int(f.readline())
        nodes = [i+1 for i in range(n)]
        data = f.readlines()
        f.close()
        left, right, length = [], [], []
        for line in data:
            edge = line.split(' ')
            left.append(int(edge[0]))
            right.append(int(edge[1]))
            length.append(int(edge[2]))
        return nodes,left,right,length
    if dtype == 'nodes':
        f = open(filename)
        size = f.readline().split(' ')
        n,l = int(size[0]), int(size[1])
        data = f.readlines()
        f.close()
        nodes, dic = [], dict()
        for line in data:
            x = ''.join(line.split(' '))
            if x not in dic:
                nodes.append(x)
                dic[x] = True
        return nodes,l
    return None
        

def max_spacing(nodes, left, right, length, k=4):
    """
    compute maximum spacing of k-clustering
    """
    ordering = sorted(range(len(length)), key= lambda i:length[i])
    unionfind = UnionFind(nodes)
    i = 0
    while unionfind.num_cluster > k:
        idx = ordering[i]
        l = unionfind.find(left[idx]) 
        r = unionfind.find(right[idx])
        i += 1
        if l == r: continue
        unionfind.union(l, r)
    while unionfind.find(left[ordering[i]]) == unionfind.find(right[ordering[i]]):
        i += 1
    return length[ordering[i]]

def max_k(nodes):
    """
    compute maximum k, s.t. max spacing >= 3, O(nl^2) running time.
    """
    uf = UnionFind(nodes)
    start = time.time()
    for x in nodes:
        for j in range(l):
            # one digit differs
            y = x[0:j] + str(1-int(x[j])) + x[j+1:]
            if y in uf.father: uf.union(x,y)
            # two digits differ
            for k in range(l):
                if k == j: continue
                p1, p2 = min(k,j), max(k,j)
                y = x[0:p1] + str(1-int(x[p1])) + x[p1+1:p2] + str(1-int(x[p2])) + x[p2+1:]
                if y in uf.father: uf.union(x,y)
    end = time.time()
    return uf.num_cluster, end-start


if __name__ == "__main__":
    f = 'clustering1.txt'
    nodes, left, right, length = load_data(f, dtype='edges')
    maxspacing = max_spacing(nodes, left, right, length, k= 4)
    print(maxspacing)

    f = 'clustering_big.txt'
    nodes,l = load_data(f, dtype='nodes')
    n = len(nodes)
    num, ti = max_k(nodes)
    print(num, ti, ti/n/l/l)
    
    
    