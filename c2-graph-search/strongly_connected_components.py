# -*- coding: utf-8 -*-
"""
compute strongly connected components, then print the sizes of 5 largest SCC.
"""

def graph_reverse(adjlist):
    n = len(adjlist)
    rev = [[] for i in range(n)]
    for r,lst in enumerate(adjlist):
        for l in lst:
            rev[l].append(r)
    return rev
            
def dfs(adjlist,order=None):
    """
    depth first search via stack
    """
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
    """
    compute strongly connected components
    """
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

def output_size(adjlist, x=5):
    _,gr = scc(adjlist)
    size = [len(g) for g in gr]
    sol = []
    for i in range(x):
        largest = max(size)
        sol.append(largest)
        size.remove(largest)
    return sol

