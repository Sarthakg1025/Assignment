def PNZ(NO):
	if NO == 0:
		print("Number is Zero..")
	elif NO >= 1:
		print("Number is Positive..")
	elif NO <= 1:
		print("Number is Negative")

def main():
	Num=int(input("Enter the number : "))
	PNZ(Num)

if __name__ == "__main__":
	main()