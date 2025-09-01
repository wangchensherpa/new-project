#softwrare design (function)

# def greeting(name,age):
#     print(f"my name is {name} , and i am {age} years old.")
# def room(name,address):
#     print(f"my name is {name} , and my room no is{address}")
# greeting('pema',19)
# greeting('hari',20)
# room('sita', 1998)
# room('tashi',1111)


class math:
    num1=int
    num2=int
    num3=int
    num4=int
    name=str
    
    def __init__(self,num1,num2,num3,num4,name,):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.num4=num4
        self.name=name
        
    def addition(self):
        print(f"the addition of{self.num1} , {self.num2} , {self.num3} , {self.num4} is {self.num1 + self.num2+self.num3+self.num4} ")
    def subtraction(self):
        print(f"the subtraction of{self.num1} and {self.num2} is {self.num1 - self.num2} ")
    def multiplication(self):
        print(f"the multiplication of{self.num1} and {self.num2} is {self.num1 * self.num2} ")
    def nam(self):
        print(f"hello!{self.name}")
        
math1=math(9,10,3,4,'hari')
math1.addition()   
math2=math(10,2,4,5,"hello")
math2.subtraction()