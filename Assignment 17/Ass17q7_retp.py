def recp(No):
	for i in range(No):
		for j in range(1,No+1):
			print(f"{j}   ",end="")
		print()

def main():
	n=int(input("Enter the number : "))
	recp(n)
if __name__ == "__main__":
	main()