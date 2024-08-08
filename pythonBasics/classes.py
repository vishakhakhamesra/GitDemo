class Calculator:
    num =100

#    def __init__(self):
#       print("I am in default constructor")

    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b

        print("I am in parent class")

    def getdata(self):
        return self.num

    def summation(self):
        return self.firstnumber+self.secondnumber+self.num

#obj = Calculator()
#print(obj.num)
obj1 = Calculator(4,5)
print(obj1.summation())