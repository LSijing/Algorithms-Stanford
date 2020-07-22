# -*- coding: utf-8 -*-
"""
minimum cut problem using random contraction, 
i.e. compute cut (A,B) with minimum number of crossing edges.
"""
import copy
import random

def union(i,j,father):
    ani = find(i,father)
    anj = find(j,father)
    if ani == anj: return 0
    if ani < anj:
        father[anj] = ani
    else:
        father[ani] = anj
    return -1
    
def find(i,father):
    f = father[i]
    if f == i:
        return i
    else:
        father[i] = find(f,father)
        return father[i]

def random_contraction(n,edges,father):
    """
    run this routine multiple times O(n^2log(n)) to record the minimum one.
    use union-find to merge nodes
    """
    # random contraction
    for k in range(n-2):
        i = random.randint(0,len(edges)-1)
        pl,pr = tuple(edges[i])
        while union(pl,pr,father) == 0:
            edges.pop(i)
            i = random.randint(0,len(edges)-1)
            pl,pr = tuple(edges[i])
#    print(m,len(edges))
    
    # delete cyclic path
    i = int(0)
    while i < len(edges):
        pl,pr = tuple(edges[i])
        if find(pl,father) == find(pr,father):
            edges.pop(i)
        else:
            i +=1
    return edges,father


if __name__ == '__main__':
    
    data = ['1 19 15 36 23 18 39',
            '2 36 23 4 18 26 9',
            '3 35 6 16 11',
            '4 23 2 18 24',
            '5 14 8 29 21',
            '6 34 35 3 16',
            '7 30 33 38 28',
            '8 12 14 5 29 31',
            '9 39 13 20 10 17 2',
            '10 9 20 12 14 29',
            '11 3 16 30 33 26',
            '12 20 10 14 8',
            '13 24 39 9 20',
            '14 10 12 8 5',
            '15 26 19 1 36',
            '16 6 3 11 30 17 35 32',
            '17 38 28 32 40 9 16',
            '18 2 4 24 39 1',
            '19 27 26 15 1',
            '20 13 9 10 12',
            '21 5 29 25 37',
            '22 32 40 34 35',
            '23 1 36 2 4',
            '24 4 18 39 13',
            '25 29 21 37 31',
            '26 31 27 19 15 11 2',
            '27 37 31 26 19 29',
            '28 7 38 17 32',
            '29 8 5 21 25 10 27',
            '30 16 11 33 7 37',
            '31 25 37 27 26 8',
            '32 28 17 40 22 16',
            '33 11 30 7 38',
            '34 40 22 35 6',
            '35 22 34 6 3 16',
            '36 15 1 23 2',
            '37 21 25 31 27 30',
            '38 33 7 28 17 40',
            '39 18 24 13 9 1',
            '40 17 32 22 34 38']

    n = len(data)
    adjlist = []
    edges = []
    father = dict()
    for i,s in enumerate(data):
        lst = []
        idx = s.find(' ')
        node = int(s[0:idx])
        father[node] = node
        s = s[idx+1:]
        while True:
            idx = s.find(' ')
            if idx == -1: break
            rend = int(s[0:idx])
            edge = sorted([node,rend])
            if edge not in edges:
                edges.append(edge)
            s = s[idx+1:]
    m = len(edges)
    
    # trials of random contraction
    mini = m+1
    for j in range(n**2):
        e = copy.copy(edges)
        f = copy.copy(father)
        if j % (5*n) ==0:
            print('finished %d/%d, num of edges %d, nodes %d'%(j,n**2,len(e),len(f)))
        res,ans = random_contraction(n,e,f)
        if len(res) < mini:
            print(len(res))
            mini = len(res)
    print(mini)
            
    # result ：17
    
    
    
    