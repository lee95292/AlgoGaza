## 1927번 Min Heap문제, 최소 힙의 삽입과 삭제를 묻는 문제
## 해결방법: 최소힙을 그대로 구현하면 된다. 
## 완전트리를 기본으로 하며 자신보다 큰 값을 자식으로 두도록 삽입하며
## 삭제할때는 루트를 지우고 마지막 원소를 루트로 스왑한 뒤 힙을 재구성한다.

## 삭제 후 힙 재구성 시 주의점으로, 자식노드중 하나라도 부모노드보다 작은 경우가 있다면 그 방향으로 가야한다는 것이다!
import sys

class MinHeap():
    def __init__(self):
        self.heap = [-1]
    def insert(self,k):
        self.heap.append(k)
        idx = len(self.heap)-1
        while self.heap[idx//2] > k and idx > 1:
            self.swap(idx//2, idx)
            idx = idx//2
    def deleteMin(self):
        if len(self.heap) == 1:
            print(0)
            return

        self.swap(1,len(self.heap)-1)
        print(self.heap.pop())
        
        idx= 1
        while idx * 2 < len(self.heap) :
            childIdx = idx * 2
            if idx * 2 +1 < len(self.heap) and self.heap[idx*2 + 1] < self.heap[childIdx]:
                childIdx = childIdx + 1
            if self.heap[childIdx] < self.heap[idx]:
                self.swap(idx,childIdx)
            idx = childIdx
    def swap(self,a,b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
    def print(self):
        print(self.heap)


input = sys.stdin.readline

n = int(input())
minHeap = MinHeap()

for i in range(n):
    k = int(input())   
    if k > 0:
        minHeap.insert(k)
    elif k == 0:
        minHeap.deleteMin()
    