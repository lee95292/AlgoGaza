n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

for i in arr2:
    l = 0
    r = len(arr)-1
    flag = False
    while(True):
        piv = (l+r)//2
        if(i == arr[piv]):
            flag = True
            print(1)
            break

        if(l == r):
            break
        if(i < arr[piv]):
            r = piv
        elif(i > arr[piv]):
            l = piv+1

    if(not flag):
        print(0)
