import sys
sys.stdin = open("input.txt", "r")

n = int(input())

words = [[] for i in range(51)]
for i in range(n):
    w = input()
    lw = len(w)
    if  w not in words[lw]:
        words[lw].append(w)


for warr in words:
    
    for w in sorted(warr):
        print(w)

