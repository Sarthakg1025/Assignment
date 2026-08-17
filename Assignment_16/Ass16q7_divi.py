def CheckDiv(Div,Dis):
	if Div % Dis == 0 :
		True
	else:
		False

def main():
	divX=int(input("Enter the Dividend : "))
	disX=int(input("Enter the Divisor : "))

	ret=CheckDiv(Div=divX,Dis=disX)
	print(ret)
	
	
if __name__ == "__main__":
	main()
	