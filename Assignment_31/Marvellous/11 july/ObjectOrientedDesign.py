class Arithematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
    def Add(self):
        Ans=self.No1+self.No2
        return Ans

    def Sub(self):
        Ans=self.No1-self.No2
        return Ans
    

print("Enter First Number : ")
Nooo1=int(input())

print("Enter First Number : ")   
Nooo2=int(input())
n=100
n2=50
obj1=Arithematic(Nooo1,Nooo2)
obj2=Arithematic(n,n2)
ret3=obj2.Add()
ret4=obj2.Sub()

ret1=obj1.Add()
ret2=obj1.Sub()

print(ret3)
print(ret4)
print("Sub",ret2)
print("Addition",ret1)                      