Even=lambda No : No % 2 == 0

def main():
	l=[11,12,21,22,51,52,17,10]
	ret=len(list(filter(Even,l)))
	print("Total Count of even number is :",ret)
if __name__ == "__main__":
	main()