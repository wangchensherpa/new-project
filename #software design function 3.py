#software design function 2
class person:
    name:str
    Class:int
    age:int
    address:str
    
    def __init__(self,name,Class,age,address):
        self.name=name
        self.Class=Class
        self.age=age
        self.address=address
    
    def greet(self):
        print(f"my name is {self.name}, i study in class {self.Class}.")
    def umer(self):
        print(f"i am {self.age} years old and i live in {self.address}")
    def speaking(self):
        print(f"this is {self.name} speaking from {self.address}")
    
person1=person('pema',12,19,'ramhiti  boudha')
person1.greet()

person2=person('hari',12,18,'chuchapati boudha')
person2.greet()

person3=person('ram',20,12,'simaltar kapan')
person3.greet()

person2.speaking()
person1.umer()
person1.speaking()
person2.umer()  
person3.speaking()
person3.umer()  