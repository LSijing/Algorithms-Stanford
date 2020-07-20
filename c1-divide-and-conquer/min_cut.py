# -*- coding: utf-8 -*-

import numpy as np
import copy

def union_set(i,j,father):
    ani = search_ancestor(i,father)
    anj = search_ancestor(j,father)
    if ani==anj:
        return 'error with union subroutine'
    if ani<anj:
        father[anj] = ani
    else:
        father[ani] = anj
    return
    
def search_ancestor(i,father):
    f = father[i]
    if f==i:
        return i
    else:
        father[i] = search_ancestor(f,father)
        return father[i]

def random_contraction(n,edges,father):
    # random contraction
    for k in range(n-2):
        i = np.random.randint(len(edges))
        pl,pr = tuple(edges[i])
        while search_ancestor(pl,father) == search_ancestor(pr,father):
            edges.pop(i)
            i = np.random.randint(len(edges))
            pl,pr = tuple(edges[i])
        union_set(pl,pr,father)
#    print(m,len(edges))
    
    # delete cyclic path
    i = int(0)
    while i<len(edges):
        pl,pr = tuple(edges[i])
        if search_ancestor(pl,father) == search_ancestor(pr,father):
            edges.pop(i)
        else:
            i +=1
    return edges,father


if __name__ == '__main__':
    # read data
    f = open('data/kargerMinCut.txt')
#    f = open('stanford-algs-master/testCases/course1/assignment4MinCut/input_random_15_50.txt')
#    output = open('stanford-algs-master/testCases/course1/assignment4MinCut/output_random_15_50.txt').readlines()
    data = f.readlines()
    
#    data = ['1 19 15 36 23 18 39',
#            '2 36 23 4 18 26 9',
#            '3 35 6 16 11',
#            '4 23 2 18 24',
#            '5 14 8 29 21',
#            '6 34 35 3 16',
#            '7 30 33 38 28',
#            '8 12 14 5 29 31',
#            '9 39 13 20 10 17 2',
#            '10 9 20 12 14 29',
#            '11 3 16 30 33 26',
#            '12 20 10 14 8',
#            '13 24 39 9 20',
#            '14 10 12 8 5',
#            '15 26 19 1 36',
#            '16 6 3 11 30 17 35 32',
#            '17 38 28 32 40 9 16',
#            '18 2 4 24 39 1',
#            '19 27 26 15 1',
#            '20 13 9 10 12',
#            '21 5 29 25 37',
#            '22 32 40 34 35',
#            '23 1 36 2 4',
#            '24 4 18 39 13',
#            '25 29 21 37 31',
#            '26 31 27 19 15 11 2',
#            '27 37 31 26 19 29',
#            '28 7 38 17 32',
#            '29 8 5 21 25 10 27',
#            '30 16 11 33 7 37',
#            '31 25 37 27 26 8',
#            '32 28 17 40 22 16',
#            '33 11 30 7 38',
#            '34 40 22 35 6',
#            '35 22 34 6 3 16',
#            '36 15 1 23 2',
#            '37 21 25 31 27 30',
#            '38 33 7 28 17 40',
#            '39 18 24 13 9 1',
#            '40 17 32 22 34 38']

    n = len(data)
    nodes = np.zeros((n),dtype=int)
    adjlist = []
    edges = []
    father = np.zeros((n),dtype=int)
    for i,s in enumerate(data):
        lst = []
        idx = s.find('\t')
        nodes[i] = int(s[0:idx])
        father[i] = i
        s = s[idx+1:]
        while True:
            idx = s.find('\t')
            if idx==-1:
                adjlist.append(lst)
                break
            rend = int(s[0:idx])
            lst.append(rend-1)
            edge = [min(i,rend-1),max(rend-1,i)]
            if edge not in edges:
                edges.append([min(i,rend-1),max(rend-1,i)])
            s = s[idx+1:]
    m = len(edges)
    
    # trials of random contraction
    mini = m+1
    for j in range(n**2):
        e = copy.copy(edges)
        f = copy.copy(father)
        if j % (5*n) ==0:
            print('starting',j,len(e),len(f))
        res,ans = random_contraction(n,e,f)
        if len(res) < mini:
            print(len(res))
#            print('true result',output[0])
            mini = len(res)
#
#    # random contraction
#    for k in range(n-2):
#        i = np.random.randint(len(edges))
#        pl,pr = tuple(edges[i])
#        while search_ancestor(pl,father) == search_ancestor(pr,father):
#            edges.pop(i)
#            i = np.random.randint(len(edges))
#            pl,pr = tuple(edges[i])
#        union_set(pl,pr,father)
#    print(m,len(edges))
#    
#    # delete cyclic path
#    i = int(0)
#    while i<len(edges):
#        pl,pr = tuple(edges[i])
#        if search_ancestor(pl,father) == search_ancestor(pr,father):
#            edges.pop(i)
#        else:
#            i +=1
#    print(len(edges))
#        
    ancestors = []
    for j in range(n):
        ans = search_ancestor(j,father)
        if ans not in ancestors:
            ancestors.append(ans)
            
    #结果 ：17
    
    
    
    