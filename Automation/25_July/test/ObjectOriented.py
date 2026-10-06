class Arithematic:
    def Add(No1,No2):
        Ans=No1+No2
        return Ans

    def Sub(No1,No2):
        Ans=No1-No2
        return Ans
    
obj1= Arithematic()

print("Enter First Number : ")
Nooo1=int(input())

print("Enter First Number : ")    #Error
Nooo2=int(input())

ret1=obj1.Add(Nooo1,Nooo2)
ret2=obj1.Sub(Nooo1,Nooo2)

print("Sub",ret2)
print("Addition",ret1)