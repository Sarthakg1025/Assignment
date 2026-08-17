from functools import reduce
Max=lambda No1 , No2 : No1 if No1 > No2 else No2

def main():
	m=[11,21,51,101,10,17]
	ret=int(reduce(Max,m))
	print("Maximum of Give list",ret)
if __name__ == "__main__":
	main()