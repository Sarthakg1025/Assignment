def Add(No1,No2):
	Ans=No1+No2
	return Ans

def main():
	Num1=int(input("Enter The First Number : "))
	Num2=int(input("Enter The Second Number"))
	ret=Add(Num1,Num2)
	print("Addition is ",ret)

if __name__ == "__main__":
	main()