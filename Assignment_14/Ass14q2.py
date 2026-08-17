Cube= lambda No : No*No*No

def main():
	No=int(input("Enter the number : "))
	ret=Cube(No)
	print("Cube of ",No," is : ", ret)
if __name__ == "__main__":
	main()