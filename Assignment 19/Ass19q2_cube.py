cube=lambda n: n*n*n

def main():
	No=int(input("Enter the Number : "))
	
	ret = cube(No)
	print("Cube of given number is : ",ret)

if __name__ == "__main__":
	main()