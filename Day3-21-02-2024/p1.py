#comparison between even and odd factors of a number
#approach 1
'''
t=int(input())
for i in range(t):
    n=int(input())
    t1=0
    t2=0
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                t1=t1+1
            else:
                t2=t2+1
    if t1==t2:
        print(1)
    else:
        print(0)
#approach 2
t=int(input())
for i in range(t):
    n=int(input())
    t1=[]
    t2=[]
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                t1.append(j)
            else:
                t2.append(j)
    if len(t1)==len(t2):
        print(1)
    else:
        print(0)'''
#approach 3
def res(n):
    t1=0
    t2=0
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                t1=t1+1
            else:
                t2=t2+1
    if t1==t2:
        return 1
    else:
        return 0
t=int(input())
def test(t):
    if t>0:
        n=int(input())
        print(res(n))
    else:
        return
    test(t-1)
test(t)
    
