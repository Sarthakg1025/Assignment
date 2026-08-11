from multiprocessing import Pool

def prime(n):
	if n < 2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n%i == 0:
			return False
	return True

def count_prime(No):
	count=0
	for i in range(1,No+1):
		if prime(i):
			count+=1
	return count

def main():
	l=[10000,20000,30000,40000] 

	with Pool() as p:
		ret=p.map(count_prime,l)

	print(ret)

if __name__ == "__main__":
	main()