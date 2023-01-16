n=input()
n=int(n)
arr=list(map(int,input().split()))

x,y=list(map(int,(input().split())))
sum=0
for i in range(x-1,y):
    sum=sum+arr[i]

print(sum)
