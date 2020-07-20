# -*- coding: utf-8 -*-

def floyd(edgedict,n):
    import math
    import copy
    d = [[math.inf for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i,j) in edgedict: d[i][j] = edgedict[(i,j)]
    
    for k in range(n):
        dist = copy.deepcopy(d)
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(d[i][j], d[i][k] + d[k][j])
        d = dist
    
    return d

def bellman_ford(edgedict,n,s=0):
    import math
    innodes = []
    for i in range(n):
        innodes.append([])
        for j in range(n):
            if (j,i) in edgedict: innodes[-1].append(j)
    
    a = []
    for i in range(n):
        if (s,i) in edgedict: a.append(edgedict[(s,i)])
        else: a.append(math.inf)
        
    for k in range(n):
        b = []
        for i in range(n):
            shortest = a[i]
            for w in innodes[i]:
                shortest = min(shortest, edgedict[(w,i)] + a[w])
            b.append(shortest)
        if k != n-1:
            a = b
        else:
            if a != b:
                print('bellman-ford negative cycle')
                return None
    
    return a
        
def johnson(edgedict,n):
    import copy
    # 1. create G' by adding a new source
    Gprime = copy.deepcopy(edgedict)
    for i in range(n): Gprime[(n,i)] = 0
    # 2. compute shortest path via bellman-ford, if negative cycle, halt
    reweight = bellman_ford(Gprime,n+1,s=n)
    if reweight is None: return reweight
    reweight = reweight[0:-1]
    # 3. create adjacency list with modified edge lengths
    adjlist = [[] for i in range(n)]
    lengths = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i,j) in edgedict: 
                adjlist[i].append(j)
                lengths[i].append(edgedict[(i,j)] + reweight[i] - reweight[j])
    # 4. repeat Dijkstra for every sources
    dist = []
    for s in range(n):
        temp = dijkstra(adjlist, lengths, s)
        dist.append(temp)
    # 5. recover real distance
    for i in range(n):
        for j in range(n):
            dist[i][j] += reweight[j] - reweight[i]
    return dist
    

def dijkstra(adjlist, lengths, s=0):
    import math
    from dijkstra import min_heap
    n = len(adjlist)
    # initialization
    dist = [ math.inf for i in range(n)]
    heap = min_heap(0)
    is_explored = [False for i in range(n)]
    is_explored[s] = True
    for i,head in enumerate(adjlist[s]):
        heap.insert(lengths[s][i], head)
    # processing
    for i in range(n-1):
        # extract the root of min heap
        if not heap.value: break
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
#    num_file = '39_1024'
#    f = open('stanford-algs-master/testCases/course4/assignment1AllPairsShortestPath/input_random_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course4/assignment1AllPairsShortestPath/output_random_'+num_file+'.txt').readlines()
    f = open('data/g3.txt')
    data = f.readline().split(' ')
    n,m = int(data[0]), int(data[1])
    dic = dict()
    left,right,length = [],[],[]
    for i in range(m):
        data = f.readline().split(' ')
        left = int(data[0]) - 1
        right = int(data[1]) - 1
        length = int(data[2])
        if (left,right) not in dic or ( (left,right) in dic and length < dic[(left,right)] ):
            dic[(left,right)] = length
    
    
    dist = johnson(dic,n)
    if not dist:
        print('Johnson NULL')
    else:
        shortest = dist[0][0]
        for x in dist:
            shortest = min(shortest,min(x))
        print(shortest)
#    print(output[0])
    
#    bellman_ford(dic,n)
#    d = floyd(dic,n)
#    q = True
#    for i in range(n):
#        if d[i][i] < 0 : 
#            q = False
#            break
#    if not q : print('Floyd NULL')
#    else:
#        shortest = d[0][0]
#        for x in d:
#            shortest = min(shortest,min(x))
#        print(shortest)
#    print(output[0])