#with one recursive function
"""
def coun(n):
    c=0
    while n>0:
        r=n%10
        if r==4:
            c+=1
        n=n//10
    return c
def test(t):
    if t>0:
        n=int(input())
        print(coun(n))
    else:
        return
    test(t-1)
t=int(input())
test(t)"""
#with two recursive function
"""def coun(n,c=0):
    if n==0:
        print(c)
        return
    else:
        if n%10==4:
             c+=1
        coun(n//10,c)
def test(t):
    if t>0:
        n=int(input())
        coun(n)
    else:
        return
    test(t-1)
t=int(input())
test(t)""" 
