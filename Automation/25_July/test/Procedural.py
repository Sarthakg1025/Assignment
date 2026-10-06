def Add(No1,No2):
    Ans=No1+No2
    return Ans

def Sub(No1,No2):
    Ans=No1-No2
    return Ans

print("Enter First Number : ")
Nooo1=int(input())

print("Enter First Number : ")
Nooo2=int(input())

ret1=Add(Nooo1,Nooo2)
ret2=Sub(Nooo1,Nooo2)

print("Sub",ret2)
print("Addition",ret1)