'''t=int(input())
c=0
while t>0:
    c+=1
    t//=10
d=n/(10**c)
d=d+3
d=d*(10**c)
d=d*10
d=d+3
print(int(d))'''
'''    
#approach 2
def rev(t):
    s=0
    while t>0:
        r=t%10
        s=(s*10)+r
        t=t//10
    return s
n=int(input())
n=(n*10)+3
z=rev(n)
z=(z*10)+3
z=rev(n)
print(z)
'''
#approach 3
n=int(input())
def tem(n):
    r=n
    c=0
    while r>0:
        c+=1
        r=r//10
    n=(3*pow(10,c))+n
    n=n*10+3
    return n
print(tem(n))
