#inheritance --> multiple inheritance
class pratical:
    def __init__(self,pe1,pe2):
        self.pratical1=pe1
        self.pratical2=pe2

class theory:
    def __init__(self,te1,te2,te3,te4,te5):
        self.theory1=te1
        self.theory2=te2
        self.theory3=te3
        self.theory4=te4
        self.theory5=te5


class exam(pratical,theory):
    def __init__(self,p1,p2,t1,t2,t3,t4,t5):
        pratical.__init__(self,p1,p2)
        theory.__init__(self,t1,t2,t3,t4,t5)

    def total(self):
        p1=self.pratical1
        p2=self.pratical2
        t1=self.theory1
        t2=self.theory2
        t3=self.theory3
        t4=self.theory4
        t5=self.theory5
        av=(p1+p2)/2
        sum=av+t1+t2+t3+t4+t5
        print(f"Total : {sum}/600")
        avg=sum/6
        print(f"Average : {avg}/100")

print(" The Mark Sheet ")
print("Enter the Pratical Marks")
pe1=int(input("Enter Science Pratical Mark :  "))
pe2=int(input("Enter Computer Pratical Mark : " ))
print()
print("Enter the theory marks :")
te1=int(input("Enter English Mark :  "))
te2=int(input("Enter Tamil Mark :  "))
te3=int(input("Enter Maths Mark :  "))
te4=int(input("Enter Social Mark :  "))
te5=int(input("Enter Science Mark :  "))
print()

publictotal=exam(pe1,pe2,te1,te2,te3,te4,te5)
publictotal.total()
