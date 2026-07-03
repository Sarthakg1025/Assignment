from functools import reduce

Mul=lambda No1,No2 : No1*No2
	
def main():
	l=[11,21,51,101,17,10]
	ret=reduce(Mul,l)
	print(ret)
if __name__ == "__main__":
	main()