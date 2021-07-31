import math
a,b,v = map(int,input().split())
d = a-b

x= math.ceil((v - a ) / d ) + 1 
print(x)