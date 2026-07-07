def DisMsg(msg):
	print(msg)

def main():
	
	n=int(input("Enter the number to Revers the Sequence : "))
	for i in range(n):
		DisMsg(n-i)

if __name__ == "__main__":
	main()