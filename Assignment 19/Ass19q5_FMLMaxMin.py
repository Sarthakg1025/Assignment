from functools import reduce

filsev = lambda No :No > 1 and all(No % i != 0 for i in range(2,int(No**0.5)+1))

Increment = lambda No : No*2

Addition = lambda No1,No2 :No1 if No1 > No2 else No2

def main():
	n=int(input("Enter the element : "))
	Data = []
	
	for i in range(n):
		ele=int(input())
		Data.append(ele)

	print("Input Data is : ",Data)

	FData = list(filter(filsev,Data))
	print("Data after Filter : ",FData)


	MData = list(map(Increment,FData))
	print("After map : ",MData)

	RData = reduce(Addition,MData)
	print("After Reduce : ", RData)

if __name__ == "__main__":
    main()