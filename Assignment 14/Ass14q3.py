max= lambda No1,No2 : No1 if No1 > No2 else No2

def main():
	n1=int(input("Enter the First Number : "))
	n2=int(input("Enter the Secind Number : "))
	ret=max(n1,n2)
	print("Maximum Number is : ",ret)
if __name__ == "__main__":
	main()
	
	
	