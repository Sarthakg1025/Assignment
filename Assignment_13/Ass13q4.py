def Binary():
	No=int(input("Enter the number : "))

	if No==0:
		print("Binary Equivalent is : 0")
	else:
		Bin=""
		temp=No
	
		while temp>0:
			rem = temp % 2
			Bin = str(rem)+Bin
			temp=temp//2
		print("Binary Equivalent of",No,"is : ",Bin)
Binary()