"""class personaldetails:
    def __init__(self,name,rollno):
        self.name=name
        self.__rollno=rollno

    def __displaytheprivate(self):
        print("The Roll No is ",self.__rollno)

class derived(personaldetails):
    def __init__(self,name,rollno):
        personaldetails.__init__(self,name,rollno)

    def accesstheprivate(self):
        self.__displaytheprivate()

name=input("Enter ur name : ")
rollno=input("Enter the roll no : ")
key=derived(name,rollno)

key.accesstheprivate()"""

"""object can not access private member, so it will generate Attribute error"""
"""AttributeError: 'derived' object has no attribute '_derived__displaytheprotected'"""

class personal:
    def __init__(self,name,rollno,dept):
        self.name=name
        self._rollno=rollno
        self.__dept=dept
    def public(self):
        print("Name : ",self.name)
    def _protect(self):
        print("Roll No : ",self._rollno)
    def __private(self):
        print("Department : ",self.__dept)
    def accessprivate(self):
        self.__private()

class derive(personal):
    def __init__(self,name,rollno,dept):
        super().__init__(name,rollno,dept)

    def accessprotect(self):
        self._protect()

name=input("Enter the name : ")
rollno=input("enter the roll no :")
dept=input("enter the dept : ")

key=derive(name,rollno,dept)
key.public()
key.accessprotect()
key.accessprivate()
