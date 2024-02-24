#abstraction
from abc import ABC, abstractmethod
class shape(ABC): # applying the abstraction for entire class(shape)
    @abstractmethod
    def area(self): # applying the abstraction for method area
        pass
    
class rect(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        print(self.a*self.b)
        
class square(shape):
    def __init__(self,n):
        self.n=n
    def area(self):
        print(self.n*self.n)
ob1=rect(2,4)
ob2=square(5)
ob1.area()
ob2.area()
 
