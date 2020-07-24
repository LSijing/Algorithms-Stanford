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
        if n == 0 : return
        self._swap(0,n-1)
        self.key.pop()
        self.node.pop()
        self._bubble_down(0)
        return
    
    def remove(self, idx):
        n = len(self.key)
        if idx > n-1: return
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
            if son > n - 1: break
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



class UnionFind():
    def __init__(self,nodes):
        self.father = dict()
        for x in nodes: self.father[x] = x
        self.num_cluster = len(self.father)
        
    def union(self, i, j):
        k = self.find(i)
        l = self.find(j)
        k,l = min(k,l), max(k,l)
        if k == l: return
        self.father[l] = k
        self.num_cluster -= 1
        return
        
    def find(self, i):
        f = self.father[i]
        if f == i:
            return i
        self.father[i] = self.find(f)
        return self.father[i]
    
    
#if __name__ == '__main__':
#    heap = MinHeap()
#    nums = [5,2,0,8,6,7,1,3,9,4]
#    index = list(range(len(nums)))
#    for x,i in zip(nums,index):
#        heap.insert(x,i)
#    print(heap.key,heap.node)
#    
#    for _ in range(4):
#        x,i = heap.extract_min()
#        heap.delete_min()
#        print(heap.key,heap.node)


if __name__ == '__main__':
    nodes  = [i+1 for i in range(6)]
    s = UnionFind(nodes)
    print(s.father)
    s.union(3,5)
    s.union(2,5)
    print(s.father, s.num_cluster)
    for i in nodes:
        print(s.find(i))