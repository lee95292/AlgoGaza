"""
11729 Max Heap 문제
"""
from collections import deque
import sys
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.n = int(input())
        self.heap = deque([0])
    
    def swap(self,a,b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
        
    def insert(self,k):
        self.heap.append(k)
        idx = len(self.heap)-1
        while idx//2 > 0 and self.heap[idx//2] < self.heap[idx]:
            self.swap(idx,idx//2)
            idx = idx //2 
        #print(self.heap)
    def delete(self):
        if len(self.heap) == 1:
            print(0)
            return
        self.swap(1, len(self.heap)-1)
        print(self.heap.pop())
        idx = 1
        while idx * 2 < len(self.heap):
            bidx = idx * 2
            if idx*2 +1 < len(self.heap) and self.heap[idx * 2] < self.heap[idx*2+1]:
                bidx= idx*2+1
            
            if self.heap[bidx] > self.heap[idx]:
                self.swap(idx,bidx)
                idx=bidx
            else:
                break

    def solve(self):
        for i in range(self.n):
            inp = int(input())
            if inp == 0:
                self.delete()
            else:
                self.insert(inp)
maxHeap = MaxHeap()
maxHeap.solve()