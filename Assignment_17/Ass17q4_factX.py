def sumfact(No):
	total=0
	for i in range(1,No):
		if No % i == 0:
			total += i
	return total

def main():
	num=int(input("Enter the number : "))
	ret=sumfact(num)
	print(ret)

if __name__ == "__main__":
	main()