def Fact():
	No=int(input("Enter The Number"))
	fact=1

	for i in range(1,No+1):
		fact*=i
	print(fact)
Fact()