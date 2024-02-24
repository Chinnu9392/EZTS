#private access specifier
'''
class car:
    __maxspeed = 0
    __name = ""
    def _init_(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    def drive(self):
        print(self.__maxspeed)
car1 = car()
car1.drive()
car1.__maxspeed = 10
car1.drive()
'''
#class and variable instances
class Dog:
    kind = "canine"
    def __init__(self,name):
        self.name = name
d = Dog("Bunny")
e = Dog("Rocky")
print(d.name)
print(e.name)
