Max= lambda n1,n2,n3 : n1 if (n1>=n2 and n1>=n3)else(n2 if n2 >= n3 else n3)

def main():
	No1=int(input("Enter First Number : "))
	No2=int(input("Enter Second Number : "))
	No3=int(input("Enter Third Number : "))
	ret=Max(No1,No2,No3)
	print("The Largest Number is ",ret)
if __name__ == "__main__":
	main()