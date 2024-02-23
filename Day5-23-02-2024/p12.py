'''
class classa:
    def factorial(self,n):
        k=1
        for i in range(1,n+1):
            k*=i
        print(k)
ob=classa()
ob.factorial(5)
            '''
"""
class classa:
    def __init__(self,n):
        self.n=n
    def factorial(self):
        k=1
        for i in range(1,self.n+1):
            k*=i
        print(k)
ob=classa(5) #passing a value through constructor
ob.factorial()"""

class classa:
    def __init__(self,n):
        self.n=n
    def factorial(self):
        print(self.recfact(self.n))
    def recfact(self,n):
        if n==1:
            return 1
        else:
            return n*self.recfact(n-1)
ob=classa(5)
ob.factorial()
