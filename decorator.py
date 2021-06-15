def decorator(f):
    def newrule(a,b):
        if a<b:
            a,b=b,a
        return f(a,b)
    return newrule


@decorator
def div(a,b):
    print(a/b)

div(5,7)
