# -*- coding: utf-8 -*-



class Heap():
    def __init__(self, heaptype = 'min'):
        self.key = []
        self.type = heaptype

    def insert(self, key):
        self.key.append(key)
        idx = len(self.key) - 1
        self.bubble_up(idx)
        return
    
    def extract_root(self):
        if self.key:
            return self.key[0]
        else:
            return None
        
    def delete_root(self):
        n = len(self.key)
        self.key[0] = self.key[n-1]
        self.key.pop()
        self.bubble_down(0)
        return
        
    def bubble_down(self, idx):
        n = len(self.key)
        while idx <= n-1:
            left = idx * 2 + 1
            if left > n - 1:
                break
            child = left
            right = idx * 2 + 2
            if right <= n-1:
                if ( (self.type == 'min' and self.key[right] < self.key[left]) or
                    (self.type == 'max' and self.key[right] > self.key[left]) ):
                    child = right
            if ( ( self.type == 'min' and self.key[idx] > self.key[child] )
                or (self.type == 'max' and self.key[idx] < self.key[child] ) ):
                self.__swap(child, idx)
                idx = child
            else:
                break
        return
    
    def bubble_up(self,idx):
        while idx > 0:
            father = (idx-1) //2
            if ((self.type == 'min' and self.key[father] > self.key[idx])
                or (self.type == 'max' and self.key[father] < self.key[idx]) ):
                self.__swap(idx,father)
                idx = father
            else:
                break
        return
                
    def __swap(self, i, j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
        return
        

if __name__ == '__main__':
    nums = [2,3,9,4,1,5,7,0]
    min_heap = Heap(heaptype='max')
    for x in nums:
        min_heap.insert(x)
    print(min_heap.key)
    for i in range(3):
        mini = min_heap.extract_root()
        min_heap.delete_root()
        print(mini)
        print(min_heap.key)
