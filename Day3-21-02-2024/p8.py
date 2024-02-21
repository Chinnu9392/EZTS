#Cooking Competiton
#approach 1
'''
t=int(input())
for i in range(t):
    n=int(input())
    even,odd=0,0
    for i in range(1,n+1):
        if n%i==0:
            if i%2==0:
                even+=1
            else:
                odd+=1

    if even==odd:
        print(1)
    else:
        print(0) '''
#approach 2
def chef(t):
    if t==0:
        return
    else:
        n=int(input())
        even,odd=0,0
        for i in range(1,n+1):
            if n%i==0:
                if i%2==0:
                    even+=1
                else:
                    odd+=1

        if even==odd:
            print(1)
        else:
            print(0)
    
    chef(t-1)
    
t=int(input())
chef(t)
