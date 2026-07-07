def str(msg):
	print(msg)

def main():
	msgx=input("Enter the String : ")

	n=int(input("Ho many times message to be printed ? : "))
	for i in range(n):
		str(msgx)

if __name__ == "__main__":
	main()