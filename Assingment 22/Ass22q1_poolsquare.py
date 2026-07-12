from multiprocessing import Pool

def sum(n):
	ans=(n*(n+1)*(2*n+1))//6
	return ans

def main():
	no=[1000000,2000000,30000000,40000000]
	
	
	with Pool() as p:
		result=p.map(sum,no)
	
	print(no)
	print(result)
	
if __name__ == "__main__":
	main()