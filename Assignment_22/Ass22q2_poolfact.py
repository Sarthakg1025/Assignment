from multiprocessing import Pool
import os
import math

def fact(n):
	id=os.getpid()
	result=math.factorial(n)
	#for i in range(2,n+1):
		#result*=1
		
	return result,n,id


def main():
	l=[10,15,20,25]
	
	with Pool() as p :
		ret=p.map(fact,l)
	
	print(f"{'Process ID':<12} | {'Input Number':<12} | {'Factorial':<25}")
	print("-" * 55)
	for pid, num, factt in ret:
        	print(f"{pid:<12} | {num:<12} | {factt:<25}")
	
if __name__ == "__main__":
	main()
