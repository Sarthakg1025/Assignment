Even=lambda No : True if (No%2==0) else False
def main():
	n=int(input("Enter the number : "))
	ret=Even(n)
	print(ret)	

if __name__ == "__main__":
	main()