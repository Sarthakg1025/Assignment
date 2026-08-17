def fact(No):
	
	if No < 0 :
		print("Factorial is Negative")
	elif No == 0:
		print("Zero Factor is 1 ")
	else :
		factt=1	
		for i in range(1,No+1):
			factt *= i
		print(f"Factor is {No} is = {factt}")

def main():
	Num=int(input("Enter the number to find Factorial : "))
	fact(Num)
if __name__ == "__main__":
	main()

