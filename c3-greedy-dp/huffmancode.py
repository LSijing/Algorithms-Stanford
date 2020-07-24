# -*- coding: utf-8 -*-
"""
Huffman code
"""

from data_structures import MinHeap

def huffmancode(weight):
    heap = MinHeap()
    depth = []
    for i,w in enumerate(weight):
        heap.insert(key=w, node=[i])
        depth.append(0)
    while len(heap.key) >= 2:
        w1,symbols1 = heap.extract_min()
        heap.delete_min()
        w2,symbols2 = heap.extract_min()
        heap.delete_min()
        w = w1 + w2
        symbols1.extend(symbols2)
        for s in symbols1:
            depth[s] += 1
        heap.insert(key=w, node=symbols1)
    
    return min(depth), max(depth)

