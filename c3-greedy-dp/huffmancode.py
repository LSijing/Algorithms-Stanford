# -*- coding: utf-8 -*-


from mst import MinHeap



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





if __name__ == '__main__':
#    num_file = '46_10000'
#    f = open('stanford-algs-master/testCases/course3/assignment3HuffmanAndMWIS/question1And2/input_random_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course3/assignment3HuffmanAndMWIS/question1And2/output_random_'+num_file+'.txt').readlines()
    f = open('data/huffman.txt')
    n = int(f.readline())
    weight = []
    for i in range(n):
        data = f.readline()
        
        w = float(data)
        weight.append(float(w))
        
    xiao,da = huffmancode(weight)
    
    print(da,xiao)
    
