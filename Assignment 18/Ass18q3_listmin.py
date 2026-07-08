def main():
	n=int(input("Enter the number : "))

	number_list=[]

	for i in range(n):
		element = int(input("Enter :"))
		number_list.append(element)

	max_number = min (number_list)
	print("Maximum : ",max_number)
if __name__ == "__main__":
	main()



