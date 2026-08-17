Square=lambda no: no*no

def main():

	No=int(input("Enter the number : "))

	sq=Square(No)

	print("Square of ",No,"is : ",sq)

if __name__ == "__main__":
	main()