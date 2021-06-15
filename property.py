class myname:
    def __init__(self,name):
        self.name=name
    @property
    def urname(self):
        print( self.name)
    @urname.setter
    def urname(self,n):
        self.name=n

name=myname("prem")
name.urname
