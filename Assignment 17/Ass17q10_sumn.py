def numadd(No):
	Sum=0
	No=abs(No)
	while No > 0:
		dig=No%10
		Sum += dig
		No=No//10
	return Sum 


def main():
	n=int(input("Enter the number : "))
	ret=numadd(n)
	print("Addition of given Length  is : ",ret)

if __name__ == "__main__":
	main()
