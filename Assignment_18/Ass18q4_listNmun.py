def main():
	n=int(input("Enter the number : "))

	number_list=[]

	print(f"Enter {n} numbers :")

	for i in range(n):
		num=int(input())
		number_list.append(num)

	search=int(input("Enter the element : "))

	freq=number_list.count(search)

	print(f"Total is : {freq}")
if __name__ == "__main__":
	main()
