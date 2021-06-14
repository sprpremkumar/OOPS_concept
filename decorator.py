def divide(a,b):
    print(a/b)

def decorator(f):

    def newrule(a,b):
        if a<b:
            a,b=b,a
        return f(a,b)
    return newrule

divide=decorator(divide)
a=int(input("Enter the num1 :"))
b=int(input("Enter the num2 :"))
divide(a,b)
