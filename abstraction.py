from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def mode(self):
        pass

class transport(car):
    def mode(self):
        print("Mode of Transport --> Road")

class benz():
    def spec(self,trans):
        trans.mode()
        print("Benz A class ---> 15.5 km/l ")

T=transport()
# T.mode()  o/p : Mode of Transport --> Road
B=benz()
B.spec(T)



