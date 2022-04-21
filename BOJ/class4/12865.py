import sys

input = sys.stdin.readline

n,k = list(map(int,input().split()))

packs = []
for i in range(n):
    mass, value = list(map(int,input().split()))
    packs.append([mass,value])