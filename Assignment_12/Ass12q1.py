def Vowel():
	char=input("Enter the number : ")
	if len(char)==1:
		
		if char in ["a","e","i","o","u","A","E","I","O","U"]:
			print("It is vowel ")
		else:
			print("It is Not a Vowel")
	else:
		print("Plzz Enter a Single Character")
Vowel()