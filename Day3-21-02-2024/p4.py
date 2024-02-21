t=int(input())
for i in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    h=0
    for j in range(n):
        if (A[j]<= 2* B[j] and B[j]<= 2* A[j]):
           h=h+1
    print(h)
