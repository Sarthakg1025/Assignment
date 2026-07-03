Odd= lambda No : False if (No%2==0) else True

def main():
	n=int(input("Enter the number : "))
	ret=Odd(n)
	print(ret)
if __name__ == "__main__":
	main()
