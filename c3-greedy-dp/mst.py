# -*- coding: utf-8 -*-
"""
Prim's minimum spanning tree algorithm
"""
from data_structures import MinHeap

def load_data(filename):
    f = open(filename)
    size = f.readline().split(sep=' ')
    n,m = int(size[0]), int(size[1])
    adjlist = [[] for _ in range(n)]
    length = [[] for _ in range(n)]
    for _ in range(m):
        data = f.readline().split(' ')
        left,right,l = int(data[0])-1, int(data[1])-1, int(data[2])
        adjlist[left].append(right)
        length[left].append(l)
        adjlist[right].append(left)
        length[right].append(l)
    f.close()
    return adjlist, length
    
    
def prim_mst(adjlist, length, s=0):
    n = len(adjlist)
    explored = [False for _ in range(n)]
    heap = MinHeap()
    # initialize
    explored[s] = True
    for nex,l in zip(adjlist[s],length[s]): 
        if nex not in heap.node: heap.insert(l, nex)
        elif l < heap.value[heap.node.index(nex)]:
            heap.delete(heap.node.index(nex))
            heap.insert(l, nex)
    cost = 0
    # adding to tree
    for i in range(n-1):
        l,candidate = heap.extract_min()
        heap.delete_min()
        explored[candidate] = True
        cost += l
        for v,lgth in zip( adjlist[candidate], length[candidate]):
            if explored[v]: continue
            if v not in heap.node:
                heap.insert(lgth, v)
            else:
                pos = heap.node.index(v)
                if heap.key[pos] > lgth:
                    heap.remove(idx= pos)
                    heap.insert(key=lgth, node= v)
    return cost
    

if __name__ == "__main__":
    f = 'edges.txt'
    adjlist, length = load_data(f)
    cost = prim_mst(adjlist, length)
    print(cost)
