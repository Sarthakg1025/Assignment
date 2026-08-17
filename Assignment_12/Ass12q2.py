def Fac():
	No=int(input("Enter the number : "))
	
	for s in range(1,No+1):
		if No % s == 0:
			print(s)
Fac()