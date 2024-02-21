def profit(nu):
    p=nu*50*(0.3)
    return int(p)
def test(t):
    if t==0:
        return
    else:
        n=int(input())
        print(profit(n))
    test(t-1)
t=int(input()) 
test(t)

