def Rev():
	No=int(input("Enter the number : ")) 
	revn=0
	while No > 0:
		dig=No%10	
		revn=revn*10+dig
		No=No//10
	print("Output : ",revn)
Rev()