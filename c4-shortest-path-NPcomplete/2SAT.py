# -*- coding: utf-8 -*-
"""
2SAT using SCC on implication graph
"""

def load_data(fname):
    """
    load data and convert to implication graph
    """
    f = open(fname)
    data = f.readline().split()
    n = int(data[0])
    data = f.readlines()
    adjlist = [[] for _ in range(2*n)]
    for line in data:
        literals = list(map(int,line.split()))
        x1 = max(2 * literals[0] - 1, -2 * literals[0]) -1 
        nx1 = max(-2 * literals[0] - 1, 2 * literals[0]) -1
        x2 = max(2 * literals[1] - 1, -2 * literals[1]) -1
        nx2 = max(-2 * literals[1] - 1, 2 * literals[1]) -1
        if x2 not in adjlist[nx1] : adjlist[nx1].append(x2)
        if x1 not in adjlist[nx2] : adjlist[nx2].append(x1)
    f.close()
    return adjlist
    

def graph_reverse(adjlist):
    n = len(adjlist)
    rev = [[] for i in range(n)]
    for r,lst in enumerate(adjlist):
        for l in lst:
            rev[l].append(r)
    return rev

def dfs(adjlist,order=None):
    n = len(adjlist)
    if order is None: order = [i for i in range(n)]
    explored = [False for i in range(n)]
    remains = [len(adjlist[i])-1 for i in range(n)]
    finish_order = []
    lead = [i for i in range(n)]
    for leader in order:
        stack = [] if explored[leader] else [leader]
        explored[leader] = True
        while stack:
            curr = stack[-1]
            while remains[curr] >= 0 and explored[adjlist[curr][remains[curr]]]: 
                remains[curr] -= 1
            if remains[curr] < 0:
                stack.pop()
                lead[curr] = leader
                finish_order.append(curr)
            else:
                nex = adjlist[curr][remains[curr]]
                stack.append(nex)
                explored[nex] = True
    return finish_order, lead

def scc(adjlist):
    rev = graph_reverse(adjlist)
    ordering,_ = dfs(rev)
    ordering.reverse()
    _,father = dfs(adjlist, order=ordering)
    groups = []
    dic = dict()
    for idx,root in enumerate(father):
        if root not in dic:
            groups.append([idx])
            dic[root] = len(groups) - 1
        else:
            groups[dic[root]].append(idx)
    return father,groups


def twosat(adjlist):
    father,_ = scc(adjlist)
    for i in range(len(adjlist)):
        if i % 2 == 1: continue
        if father[i] == father[i+1]: return 0
    return 1
    
    
        

if __name__ == '__main__':
    for i in range(6):
        f = '2sat' + str(i+1) + '.txt'
        adjlist = load_data(f)
        satis = twosat(adjlist)
        print(satis)
