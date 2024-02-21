#factorial of a number
#approach 1
n=int(input())
p=1
for i in range(1,n+1):
    p*=i
print(p)

#approach 2
n=int(input())
p=1
while n>0:
    p*=n
    n-=1
print(p)

#approach 3
def fact(n):
    if n>1:
        return n*fact(n-1)
    else:
        return 1
print(fact(n))
