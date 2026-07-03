Square= lambda No : No*No

def main():
	
	listX=[11,21,51,101,17,10]
	ret=list(map(Square,listX))
	print("Square of list is : ",ret)
if __name__ == "__main__":
	main()