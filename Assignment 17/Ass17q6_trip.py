def trip(No):
	for i in range(No,0,-1):
		print("* "* i)

def main():
	N=int(input("Enter the numner : "))
	trip(N)
if __name__ == "__main__":
	main()