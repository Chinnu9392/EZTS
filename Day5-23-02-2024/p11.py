#adding a particular digit to the characters of a string
#approach 1
# sam  2  ---> uco
'''
t=int(input())
alpha="abcdefghijklmnopqrstuvwxyz"
for i in range(t):
    s,n=input().split()
    r=""
    for j in s:
        m=alpha.index(j)+int(n)
        if m>25:
            m=m%26
        r+=alpha[m]
    print(r)
'''
#approach 2
t=int(input())
alpha="abcdefghijklmnopqrstuvwxyz"
for i in range(t):
    s,n=input().split()
    r=""
    for j in s:
        k=ord(j)+int(n)
        if k>122:
            k=96+(k-122)
            r+=chr(k)
        else:
            r+=chr(k)
    print(r)
