"""
1629 분할정복을 이용한 거듭제곱

f(n) = ( f(n-1)**2 or f(n-1) ** 2 * k )
"""
a,b,c = list(map(int,input().split()))

def dc_pow(a,n):
    if n ==1 :
        return a%c

    temp = dc_pow(a,n//2)
    if n%2 ==0:
        return temp**2%c
    else:
        return temp**2*a%c

print(dc_pow(a,b)%c)