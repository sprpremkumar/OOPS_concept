# The basic Calculator Operation with class and object

class oops:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def add(self):
        num1=self.num1
        num2=self.num2
        sum=num1+num2
        print(f"The answer is {sum}")

    def sub(self):
        num1 = self.num1
        num2 = self.num2
        sub = num1 - num2
        print(f"The answer is {sub}")

    def product(self):
        num1 = self.num1
        num2 = self.num2
        pro = num1 * num2
        print(f"The answer is {pro}")

    def divide(self):
        num1 = self.num1
        num2 = self.num2
        div = num1 / num2
        print(f"The answer is {div}")






print("Welcome to The Calci, Please enter ur number!!")
a=int(input("Enter the first Number : "))
b=int(input("Enter the second Number : "))
symbol=input("Enter the Symbol for Calculation : ")
calculation = oops(a,b)
if symbol == "+" :
    calculation.add()
if symbol == "-" :
    calculation.sub()
if symbol == "*" :
    calculation.product()
if symbol == "/" :
    calculation.divide()