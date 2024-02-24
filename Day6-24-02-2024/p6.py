#single inheritance
class Dob:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def display1(self):
        mon=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
        print(self.date)
        print(mon[self.month-1])
        print(self.year)
        
class Detail(Dob):
    def __init__(self,name,age,date,month,year):
        self.name=name
        self.age=age
        self.date=date
        self.month=month
        self.year=year
        super().__init__(date,month,year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)
        
ob=Detail("abc",27,24,8,2024)
ob.display()
ob.display1()
#output

