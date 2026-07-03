def Prime():
	No=int(input("Enter the number : "))
	
	if No > 1:
		for s in range(2,No):
			if (No%s)==0:
				print("It is a not prime number")
				break
		else:
			print("It is a prime number ..") 
	else:
		print("It is a not prime number")
Prime()