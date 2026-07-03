from functools import reduce

Min=lambda No1,No2: No1 if No1 < No2 else No2

def main():
	m=[11,21,51,101,17,10]
	ret=reduce(Min,m)
	print("Minimum number of given list is : ",ret)
if __name__ == "__main__":
	main()