from classes import Calculator

class childimpl(Calculator):
    num2 = 200

    def __init__(self,a,b):
        Calculator.__init__(self,a,b)
        print("I am in child class")

    def getdata(self):
        return self.num2

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = childimpl(6,7)
print(obj.getCompleteData())
print(obj.getdata())
obj = Calculator(2,2)
print(obj.getdata())

#Python executes all code in import 