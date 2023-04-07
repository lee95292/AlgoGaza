"""
class Node:
    def __init()__:
        data,next
"""
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

factories = [0]
numberNodeMap = [0]*100001
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.itemCount = 0
        self.head=None
        self.tail=None

    def appendData(self, data):
        curNode = Node(data)
        self.append(curNode)
        numberNodeMap[curNode.data] = curNode
        return self.itemCount

    def append(self,node):
        if self.itemCount == 0:
            self.head = node
            self.head.next= None
        else:
            node.prev = self.tail
            self.tail.next = node
        self.tail = node
        self.tail.next=None
        self.itemCount += 1
        return self.itemCount

    def appendLeft(self,node):
        if self.itemCount == 0:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
            self.itemCount +=1
            return 1

        self.head.prev = node
        node.next = self.head
        self.head = node
        self.head.prev=None
        self.itemCount += 1
        return self.itemCount
    def popLeft(self):
        if self.itemCount == 0: return
        r = self.head
        self.head = self.head.next
        if self.head: self.head.prev = None
        r.next = None
        self.itemCount -= 1
        if self.itemCount == 0: self.tail = None
        return r
    def search(self,n):
        if n > self.itemCount: return None
        r = self.head
        while n > 1:
            n-=1
            r = r.next
        return r
    def printItems(self):
        r = self.head
        while r!= None:
            print(r.data, end=' ')
            r = r.next
        if self.itemCount > 0: print('head,tail: ',self.head.data, self.tail.data, self.itemCount)
        else: print()
        if self.itemCount > 0 and (self.head.prev != None or self.tail.next != None): print("!!!!!!!!erorr")

def buildFactories(strs): # 100
    chrs = list(map(int,strs.split()))
    n,m = chrs[0:2]
    gifts = chrs[2:]
    for i in range(n):
        factories.append(LinkedList())
    for i,bn in enumerate(gifts):
        factories[bn].appendData(i+1)
def moveAllItems(src,dest): # 200
    if factories[src].itemCount == 0: return factories[dest].itemCount
    if factories[dest].itemCount == 0 :
        factories[dest].head = factories[src].head
        factories[dest].tail = factories[src].tail
    else:
        factories[src].tail.next = factories[dest].head
        factories[dest].head.prev = factories[src].tail
        factories[dest].head = factories[src].head

    factories[dest].itemCount += factories[src].itemCount
    # clear src
    factories[src].itemCount = 0
    factories[src].head = None
    factories[src].tail = None
    return factories[dest].itemCount

def swapFirstItem(src,dest): # 300
    orgDest = dest
    if factories[dest].itemCount + factories[src].itemCount == 0: return factories[dest].itemCount
    if factories[dest].itemCount == 0: src,dest = dest,src
    if factories[src].itemCount == 0: # 둘중 하나가 빈 벨트이면
        node = factories[dest].popLeft()
        factories[src].append(node)
        return factories[orgDest].itemCount
    sNode = factories[src].popLeft()
    dNode = factories[dest].popLeft()
    factories[dest].appendLeft(sNode)
    factories[src].appendLeft(dNode)
    return factories[dest].itemCount

def divideHalf(src,dest): #400
    if factories[src].itemCount < 2: return factories[dest].itemCount
    n = factories[src].itemCount//2
    edNode = factories[src].search(n)
    oldSrcHead = factories[src].head
    factories[src].head = edNode.next
    factories[src].head.prev = None

    if factories[dest].itemCount == 0:
        edNode.next = None
        factories[dest].tail = edNode
    else:
        edNode.next = factories[dest].head
        factories[dest].head.prev = edNode
    factories[dest].head = oldSrcHead
    factories[dest].head.prev = None

    factories[dest].itemCount += n
    factories[src].itemCount -= n
    return factories[dest].itemCount
def getGiftInfo(giftNum): #500
    gift = numberNodeMap[giftNum]
    a,b = -1,-1
    if gift.prev: a = gift.prev.data
    if gift.next: b= gift.next.data
    return a+2*b

def getBeltInfo(beltNum):
    a,b,c = -1,-1, factories[beltNum].itemCount
    if factories[beltNum].head: a = factories[beltNum].head.data
    if factories[beltNum].tail: b = factories[beltNum].tail.data
    return a+2*b+3*c
def printBelt():
    print('st================')
    for i in range(1,len(factories)):
        print(f'i{i}',end=' ')
        factories[i].printItems()
    print('ed================')

q = int(input())
for i in range(q):
    ops = input()
    if ops[0:3] == '100':
        buildFactories(ops[3:])
    elif ops[0:3] == '200':
        o, src, dest = map(int, ops.split())
        print(moveAllItems(src,dest))
    elif ops[0:3] == '300':
        o, src, dest = map(int, ops.split())
        print(swapFirstItem(src,dest))
    elif ops[0:3] == '400':
        o, src, dest = map(int, ops.split())
        print(divideHalf(src,dest))
    elif ops[0:3] == '500':
        o, src = map(int, ops.split())
        print(getGiftInfo(src))
    elif ops[0:3] == '600':
        o, src = map(int, ops.split())
        print(getBeltInfo(src))
    # print(ops,end='')
    # printBelt()


"""
9
100 9 10 2 2 9 1 3 9 5 9 3 5
600 1
400 8 1
300 8 4
200 8 6
300 1 6
200 6 2
200 4 3
500 10
"""