min=lambda No1,No2 : No1 if No1 < No2 else No2
def main():
	n1=int(input("Enter the First Number : "))
	n2=int(input("Enter the Second Number : "))
	ret=min(n1,n2)
	print("Minimum Number is : ",ret)
if __name__ == "__main__":
	main()