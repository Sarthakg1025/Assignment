div= lambda No : No % 3 ==0 and No % 5 == 0

def main():
	l=[11,21,51,101,17,10,15,25,30,90,45,5]
	ret=list(filter(div,l))
	print(ret)
if __name__ == "__main__":
	main()	