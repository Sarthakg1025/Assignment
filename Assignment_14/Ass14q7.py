div=lambda No : No % 5 == 0

def main():
	n=int(input("Enter the Number : ")) 
	ret=div(n)
	print(ret)
if __name__ == "__main__":
	main()