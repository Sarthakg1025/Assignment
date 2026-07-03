Even= lambda No : No % 2 == 0

def main():
	num=[11,21,51,101,17,10]
	ret=list(filter(Even,num))
	print("Even Number of given list is : ",ret)
if __name__ == "__main__":
	main()