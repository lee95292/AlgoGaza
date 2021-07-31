n = int(input())

r=1
for i in range(1,20000):
    if n <= i * (i+1) /2:
        r=i
        break

k = i * (i+1) /2 - n
l = r- k

if r % 2 == 0:
    x,y  = l,k+1
else:
    x,y = k+1,l 


print(str(int(x)) + "/"+str(int(y)))
