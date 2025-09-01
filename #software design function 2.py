#software design function 2
class person:
    name:str
    Class:int
    age:int
    address:str
    
    def greet(self):
        print(f"my name is {self.name}, i study in class {self.Class}.")
    def umer(self):
        print(f"i am {self.age} years old and i live in{self.address}")
    def speaking(self):
        print(f"this is {self.name} speaking from {self.address}")
    
person1=person()
person1.name='pema'
person1.Class=12
person1.age=19
person1.address='ramhiti boudha'
person1.greet()

person2=person()
person2.name='hari'
person2.Class=12
person2.age=18
person2.address='chuchapati boudha'
person2.greet()

person2.speaking()
person1.umer()
person1.speaking()
person2.umer()    