def pre():

	No=int(input("Enter the number : "))
	div=0
	for s in range(1,(No//2)+1):
		if No % s == 0:
			div+=s
	if div == No:
		print("It is a Prefect Number..")
	else: 
		print("It is Not a Prefect Number ")
pre()