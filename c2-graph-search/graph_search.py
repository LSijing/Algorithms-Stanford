# -*- coding: utf-8 -*-

import numpy as np
from sort_search import quick_sort

def reverse_graph(adjlist):
    n = int( len(adjlist)-1 )
    rev_adjlist = [ [] for i in range(n+1)]
    for tail,head_list in enumerate(adjlist):
        for idx, head in enumerate(head_list):
            rev_adjlist[head].append(tail)
    return rev_adjlist
            

def dfs_loop(adjlist, orderlist=None):
    n = int( len(adjlist) -1 )
    is_explored = [False for i in range(n+1)]
    father = [ 0 for i in range(n+1)]
    ft = []
    if orderlist is not None:
        for node in orderlist:
            if is_explored[node]==False:
                depth_first_search(node, adjlist, is_explored, ft, leader=father, original=node)
    else:
        for node in range(1,n+1):
            if is_explored[node]==False:
                depth_first_search(node, adjlist, is_explored, ft, leader=father, original=node)
    return ft, father

#def dfs_scc(adjlist):
#    n = int( len(adjlist) - 1 ) 
#    is_explored = [False for i in range(n+1)]
#    father = [ 0 for i in range(n+1)]
#    ft = []
#    for node in range(1,n+1):
#        if is_explored[node] == False:
#            depth_first_search(node, adjlist, is_explored, ft, leader=father, original=node)
#    return father

def depth_first_search(node, adjlist, explored, finish_time, leader, original):
    explored[node] = True
    leader[node] = original
    for head in adjlist[node]:
        if explored[head]==False:
            depth_first_search(head, adjlist, explored, finish_time= finish_time, leader = leader, original=original)
    finish_time.append(node)
    

def dfs_loop_stack(adjlist, orderlist=None):
    """
    compute strongly connected components
    """
    n = int( len(adjlist)-1 )
    is_explored = [False for i in range(n+1)]
    father = [0 for i in range(n+1)]
    ft = []
    order_adjacency = np.zeros((n+1), dtype=int)
    if orderlist is None:
        orderlist = range(1,n+1)
    for node in orderlist:
        if is_explored[node]==False:
            stack = []
            stack.append(node)
            while stack:
                current_node = stack[-1]
                is_explored[current_node] = True
                father[current_node] = node
                while ( order_adjacency[current_node] < len(adjlist[current_node]) and 
                       is_explored[adjlist[current_node][order_adjacency[current_node]]] == True):
                    order_adjacency[current_node] += 1
                if order_adjacency[current_node] >= len(adjlist[current_node]):
                    stack.pop()
                    ft.append(current_node)
                else:
                    head = adjlist[current_node][order_adjacency[current_node]]
                    stack.append(head)
    return ft,father

if __name__ == '__main__':
    """
    compute strongly connected components by depth first search through stack (not recursion)
    """
    
#    f = open('stanford-algs-master/testCases/course2/assignment1SCC/input_mostlyCycles_68_320000.txt')
#    output = open('stanford-algs-master/testCases/course2/assignment1SCC/output_mostlyCycles_68_320000.txt')
#    n = 320000
    
    n = 875714
    adjlist = [[] for i in range(n+1)]
    
    f = open('data/SCC.txt')
    data = f.readlines()
    for i,s in enumerate(data):
        pos = s.find(' ')
        tail = int(s[0:pos])
        ed = s[pos+1:].find(' \n')
        head = int(s[pos+1:][0:ed])
        adjlist[tail].append(head)
        
    rev = reverse_graph(adjlist)
    
    s = 0
    for ite in rev:
        s += len(ite)
    print(s)
    
    ft, leader = dfs_loop_stack(rev)
    ft.reverse()
    finishtime, group = dfs_loop_stack(adjlist, orderlist=ft)
    
    
    # count SCCs
    arr = np.array(group[1:])
    size = np.zeros((n+1), dtype=int)
    for i in range(arr.size):
        size[arr[i]] += 1
    results = []
    for i in range(5):
        results.append( max(size) ) 
        size = np.delete(size, size.argmax())
    print(results)