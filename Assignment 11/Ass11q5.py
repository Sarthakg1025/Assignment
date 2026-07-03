def Pali():
	No=int(input("Enter the number : "))
	temp=No
	rev=0
	while No > 0:
		n=No%10
		rev=rev*10+n
		No=No//10
	if rev == temp:
		print("Its a Palindrome")
	else:
		print("It is Not a Palindrome")
Pali()