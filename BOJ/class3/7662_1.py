import sys
import math
input = sys.stdin.readline

class Heap:
    def __init__(self):
        self.heap = [0]
    
    def swap(self,a,b):
        tmp = self.heap[a] 
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
    
    def insert(self,k):
        self.heap.append(k)
        idx = len(self.heap) -1
        while idx//2 > 0 and self.heap[idx] > self.heap[idx//2]:
            self.swap(idx,idx//2)
            idx = idx//2

    def delete(self,idx=1):
        if len(self.heap) == 1:
            return
        self.swap(idx,len(self.heap)-1)
        val = self.heap.pop()
        while idx*2 < len(self.heap):
            bidx = idx * 2
            if len(self.heap) > idx *2 + 1 and self.heap[idx*2+1] < self.heap[idx*2]:
                bidx = idx * 2 +1

            if self.heap[bidx] < self.heap[idx]:
                break
            self.swap(bidx,idx)    
            idx= bidx
        return val
    
    def deleteByValue(self,v):
        if len(self.heap) == 1:
            return

        for i in range(1, len(self.heap)):
            if self.heap[i] == v:
                self.delete(i)
                break            

T = int(input())
for t in range(T):
    maxHeap = Heap()
    minHeap = Heap()
    n = int(input())
    for i in range(n):
        inst, k = input().split()
        num = int(k)
        if inst =='I':
            maxHeap.insert(num)
            minHeap.insert(-1*num)
        if inst == 'D':
            if num == 1:
                value = maxHeap.delete()
                minHeap.deleteByValue(value*-1)

            if num == -1:
                value = minHeap.delete()
                maxHeap.deleteByValue(value*-1)
        print(maxHeap.heap)
        print(minHeap.heap)
    if maxHeap.heap[1:]:
        print(maxHeap.heap[1], minHeap.heap[1], end='')
    else:
        print("EMPTY")
