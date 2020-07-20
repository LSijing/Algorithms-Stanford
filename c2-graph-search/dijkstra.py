# -*- coding: utf-8 -*-

import numpy as np


class min_heap():
    def __init__(self,n=0):
        self.value = [ [] for i in range(n) ]
        self.node  = [ [] for i in range(n) ]
        
    def insert(self,v, node):
        idx = len(self.value)
        self.value.append(v)
        self.node.append(node)
        while idx!=0 and self.value[(idx+1)//2-1] > v:
            self.value[idx], self.node[idx] = self.value[(idx+1)//2-1], self.node[(idx+1)//2-1]
            idx = (idx+1)//2-1
        self.value[idx], self.node[idx] = v, node
        
    def delete(self, pos=int(0)):
        self.value[pos], self.node[pos] = self.value[-1], self.node[-1]
        v, node = self.value[pos], self.node[pos]
        self.value.pop()
        self.node.pop()
        last = len(self.value)-1
        idx = pos
        # bubble
        if pos!=0 and v < self.value[(pos+1)//2-1]:
            while idx!=0 and self.value[(idx+1)//2-1] > v:
                self.value[idx], self.node[idx] = self.value[(idx+1)//2-1], self.node[(idx+1)//2-1]
                idx = (idx+1)//2-1
            self.value[idx], self.node[idx] = v, node
        # sink
        else:
            while idx*2+1 <= last:
                if self.value[idx*2+1] < self.value[idx]:
                    if idx*2+2 <= last and self.value[idx*2+2] < self.value[idx*2+1]:
                        self.value[idx*2+2], self.value[idx] = self.value[idx], self.value[idx*2+2]
                        self.node[idx*2+2], self.node[idx] = self.node[idx], self.node[idx*2+2]
                        idx = idx*2+2
                    else:
                        self.value[idx*2+1], self.value[idx] = self.value[idx], self.value[idx*2+1]
                        self.node[idx*2+1], self.node[idx] = self.node[idx], self.node[idx*2+1]
                        idx = idx*2+1
                elif idx*2+2 <= last and self.value[idx*2+2] < self.value[idx]:
                    self.value[idx*2+2], self.value[idx] = self.value[idx], self.value[idx*2+2]
                    self.node[idx*2+2], self.node[idx] = self.node[idx], self.node[idx*2+2]
                    idx = idx*2+2
                else:
                    break
            
def dijkstra(adjlist, lengths, s=0):
    n = len(adjlist)
    # initialization
    dist = np.zeros((n))
    heap = min_heap(0)
    is_explored = [False for i in range(n)]
    is_explored[s] = True
    for i,head in enumerate(adjlist[s]):
        heap.insert(lengths[s][i], head)
    # processing
    for i in range(n-1):
        # extract the root of min heap
        score,e = heap.value[0] , heap.node[0]
        dist[e] = score
        heap.delete(0)
        is_explored[e] = True
        # add heads to the min heap
        for ee,head in enumerate(adjlist[e]):
            if not is_explored[head]:
                if head not in heap.node:
                    heap.insert(dist[e]+lengths[e][ee], head)
                else:
                    idx = heap.node.index(head)
                    if dist[e]+lengths[e][ee] < heap.value[idx]:
                        heap.delete(idx)
                        heap.insert(dist[e]+lengths[e][ee], head)
    
    return dist
        
        
        
        
if __name__ == '__main__':
    
#    f = open('stanford-algs-master/testCases/course2/assignment2Dijkstra/input_random_28_256.txt')
#    output = open('stanford-algs-master/testCases/course2/assignment2Dijkstra/output_random_28_256.txt')
    f = open('data/dijkstraData.txt')
    data = f.readlines()
    n = len(data)
    nodes = np.zeros((n),dtype=int)
    adjlist = []
    weights = []
    for i,s in enumerate(data):
        lst = []
        weight = []
        idx = s.find('\t')
        nodes[i] = int(s[0:idx])
        s = s[idx+1:]
        while True:
            idx = s.find('\t')
            if idx==-1:
#                jdx = s.find('\n')
#                comma = s.find(',')
#                lst.append(int(s[0:comma])-1)
#                weight.append(int(s[comma+1:jdx]))
                adjlist.append(lst)
                weights.append(weight)
                break
            comma = s.find(',')
            lst.append(int(s[0:comma])-1)
            weight.append(int(s[comma+1:idx]))
            s = s[idx+1:]
            
            
    dist = dijkstra(adjlist, weights, s=0)
    
    pos = [7,37,59,82,99,115,133,165,188,197]
    for i in range(len(pos)):
        print(int(dist[pos[i]-1]))
#    print(output.readlines()[0])