def main():
	n=int(input("Enter the number : "))

	number=[]
	
	print(f"Enter {n} number : ")

	for i in range(n):
		num=int(input("Enter : "))
		number.append(num)

	total_sum=sum(number)

	print(f"Output : {total_sum}")
if __name__ == "__main__":
	main()