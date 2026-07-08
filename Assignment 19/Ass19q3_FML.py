from functools import reduce

filsev = lambda No :70 <= No <= 90 

Increment = lambda No : No + 10

Addition = lambda No1 , No2 : No1 * No2

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

	RData = reduce(Addition , MData)
	print("After Reduce : ", RData)

if __name__ == "__main__":
    main()