#odd even index
#approach 1
'''
n=input()
r=""
s=""
for i in range(len(n)):
    if i%2==0:
        r=r+n[i]
    else:
        s=s+n[i]
print(s+r)
'''
#approach 2
n=input()
print(n[1::2]+n[::2])
