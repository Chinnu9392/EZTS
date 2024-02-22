#phonebook
n=int(input())
d={}
for i in range(n):
    name,ph=input().split()
    d[name]=ph
    
def finding(f):
    if f in d:
        print(f"{f}={d[f]}")
    else:
        print("Not Found")
while True:
    s=input()
    finding(s)
