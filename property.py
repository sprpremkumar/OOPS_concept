class myage:
    def __init__(self):
        self.__age=0

    def get_age(self):#getter method
        return self.__age

    def set_age(self,a):#setter method
        self.__age=a

prem_age=myage()

prem_age.set_age(21) #setting the age

print(prem_age.get_age())# getting the age

