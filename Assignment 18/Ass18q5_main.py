from Ass18q5_MarvellousNum import *
def listp(element):
	prime=0
	for num in element:
		if check(num):
			prime+=num
	return prime	

def main():

	n=int(input("Number of Element : "))
	num=[]
	print(f"Enter {n} elements : ")
	for i in range(n):
		ele=int(input())
		num.append(ele)
	ret=listp(num)
	print("Output : ",ret)
if __name__ == "__main__":
	main()
	