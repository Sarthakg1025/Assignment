from functools import reduce

Add= lambda No1,No2 : No1 + No2

def main():
	l=[11,21,51,101,10,17]
	ret=(reduce(Add,l))
	print("Addition of given list is ",ret)
if __name__ == "__main__":
	main()