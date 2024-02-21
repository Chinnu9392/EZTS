#prime
'''
n=int(input())
f=[]
for i in range(1,n+1):
    if n%i==0:
        f.append(i)
if len(f)==2:
    print("prime")
else:
    print("NOt Prime")
'''
#approach 2
n=int(input())
if all([n%i!=0 for i in range(2,n)]):
    print("prime")
else:
    print("NOt Prime")
