def prime(num):
	if num <= 1:
		print("Not a prime Number. ")
	else:
		is_prime=True
		for i in range(2,num):
			if num % i == 0 :
				is_prime= False
				break
		if is_prime:
			print("The given number is prime.")
		else:
			print("The given number is Not Prime.")

def main():
	No=int(input("Enter the number : "))
	
	prime(No)
	

if __name__ == "__main__":
	main()

