# -*- coding: utf-8 -*-


class MinHeap():
    def __init__(self):
        self.key = []
        self.node = []
        
    def extract_min(self):
        n = len(self.key)
        if n == 0:
            return None
        else:
            return self.key[0], self.node[0]
        
    def delete_min(self):
        n = len(self.key)
        if n == 0 :
            return
        self._swap(0,n-1)
        self.key.pop()
        self.node.pop()
        self._bubble_down(0)
        return
    
    def remove(self, idx):
        n = len(self.key)
        if idx > n-1:
            return
        self._swap(idx, n-1)
        self.key.pop()
        self.node.pop()
        self._bubble_up(idx)
        self._bubble_down(idx)
        return
        
    def insert(self, key , node):
        self.key.append(key)
        self.node.append(node)
        n = len(self.key)
        self._bubble_up(n-1)
        return
    
    def _bubble_down(self, idx):
        n = len(self.key)
        while idx <= n - 1:
            son = idx * 2 + 1
            if son > n - 1:
                break
            right = idx * 2 + 2
            if right <= n-1 and self.key[right] < self.key[son]:
                son = right
            if self.key[son] < self.key[idx]:
                self._swap(son, idx)
                idx = son
            else:
                break
        return
        
    def _bubble_up(self, idx):
        n = len(self.key)
        while idx > 0 and idx <= n - 1:
            father = (idx - 1) // 2
            if self.key[father] > self.key[idx]:
                self._swap(idx,father)
                idx = father
            else:
                break
        return
        
    def _swap(self, i,j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
        self.node[i], self.node[j] = self.node[j], self.node[i]
        return
        

def prim_mst(adjlist, length, s=0):
    n = len(adjlist)
    explored = [False for _ in range(n)]
    heap = MinHeap()
    # initialize
    explored[s] = True
    for tail,l in zip(adjlist[s],length[s]):
        heap.insert(l,tail)
    cost = 0
    # adding to tree
    for i in range(n-1):
        l,candidate = heap.extract_min()
        heap.delete_min()
        explored[candidate] = True
        cost += l
        for v,lgth in zip( adjlist[candidate], length[candidate]):
            if explored[v]:
                continue
            if v not in heap.node:
                heap.insert(lgth, v)
            else:
                pos = heap.node.index(v)
                if heap.key[pos] > lgth:
                    heap.remove(idx= pos)
                    heap.insert(key=lgth, node= v)
    return cost
    
    
class UnionFind():
    def __init__(self,n):
        self.father = [i for i in range(n)]
        self.num_cluster = n
        
    def union(self, i, j):
        k = self.find(i)
        l = self.find(j)
        k,l = min(k,l), max(k,l)
        if k == l:
            return
        self.father[l] = k
        self.num_cluster -= 1
        return
        
    def find(self, i):
        f = self.father[i]
        if f == i:
            return i
        self.father[i] = self.find(f)
        return self.father[i]
    
def k_clustering(left, right, length, n, k=4):
    index = sorted(range(len(length)), key= lambda i:length[i])
    unionfind = UnionFind(n)
    i = 0
    while unionfind.num_cluster > k:
        idx = index[i]
        l = unionfind.find(left[idx]) 
        r = unionfind.find(right[idx])
        i += 1
        if l == r:
            continue
        unionfind.union(l, r)
    while unionfind.find(left[index[i]]) == unionfind.find(right[index[i]]):
        i += 1
    return length[index[i]]

if __name__ == '__main__':
    import time
    num_file = '81_131072_24'
#    f = open('stanford-algs-master/testCases/course3/assignment2Clustering/question2/input_random_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course3/assignment2Clustering/question2/output_random_'+num_file+'.txt').readlines()
    f = open('data/clustering_big.txt')
    dic = {}
    node = []
    size = f.readline().split(' ')
    n,l = int(size[0]), int(size[1])
    data = f.readlines()
    pos = 0
    for s in data:
        x = ''.join(s.split(' '))
        if x not in dic:
            dic[x] = pos
            pos += 1
            node.append(x)
    n = len(node)
    
    uf = UnionFind(n)
    start = time.time()
    for x in node:
        for j in range(l):
            # one digit difference
            y = x[0:j] + str(1-int(x[j])) + x[j+1:]
            if y in dic:
                uf.union(dic[x],dic[y])
            # two digits difference
            for k in range(l):
                if k != j:
                    p1,p2 = min(k,j), max(k,j)
                    y = x[0:p1] + str(1-int(x[p1])) + x[p1+1:p2] + str(1-int(x[p2])) + x[p2+1:]
                    if y not in dic:
                        continue
                    else:
                        uf.union(dic[x],dic[y])
    end = time.time()
    print(uf.num_cluster,  (end-start)/n/l/l)
        
        
    
    

    
    
#if __name__ == '__main__':
#    s = UnionFind(6)
#    print(s.father)
#    s.union(3,5)
#    s.union(2,5)
#    print(s.father)
#    for i in range(6):
#        print(s.find(i))

#if __name__ == "__main__":
#    num_file = '32_1024'
##    f = open('stanford-algs-master/testCases/course3/assignment2Clustering/question1/input_completeRandom_'+num_file+'.txt')
##    output = open('stanford-algs-master/testCases/course3/assignment2Clustering/question1/output_completeRandom_'+num_file+'.txt').readlines()
#    f = open('data/clustering1.txt')
#    n = int(f.readline())
#    left, right, length = [], [], []
#    data = f.readlines()
#    for s in data:
#        edge = s.split(' ')
#        left.append( int(edge[0]) -1 )
#        right.append( int(edge[1]) -1 )
#        length.append( int(edge[2]) )
#        
#    maxspacing = k_clustering(left, right, length, n, 4)
#    print(maxspacing)
        
#if __name__ == '__main__':
#    heap = MinHeap()
#    nums = [5,2,0,8,6,7,1,3,9,4]
#    index = [i for i in range(len(nums))]
#    for x,i in zip(nums,index):
#        heap.insert(x,i)
#    print(heap.key,heap.node)
#    
#    for _ in range(4):
#        x,i = heap.extract_min()
#        heap.delete_min()
#        print(heap.key,heap.node)
#        
    
#if __name__ == "__main__":
#    num_file = '68_100000'
#    f = open('stanford-algs-master/testCases/course3/assignment1SchedulingAndMST/question3/input_random_'+num_file+'.txt')
#    output = open('stanford-algs-master/testCases/course3/assignment1SchedulingAndMST/question3/output_random_'+num_file+'.txt').readlines()
#    f = open('data/edges.txt')
#    size = f.readline().split(sep=' ')
#    n,m = int(size[0]), int(size[1])
#    adjlist = [[] for _ in range(n)]
#    length = [[] for _ in range(n)]
#    for _ in range(m):
#        data = f.readline().split(' ')
#        left,right,l = int(data[0])-1, int(data[1])-1, int(data[2])
#        adjlist[left].append(right)
#        length[left].append(l)
#        adjlist[right].append(left)
#        length[right].append(l)
#        
#    cost = prim_mst(adjlist, length)
#    print(cost)
#    print(cost,output[0] ,cost-int(output[0]))
