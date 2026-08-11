from multiprocessing import Pool
import os 

def even(n):
	total = sum(i for i in range(2, n + 1, 2))
		
	id=os.getpid()
	print("Process ID : ",id)
	print("Input Number : ",n)
	print("Even number : ",total)
	
def main():
	No=[10000,20000,30000,40000]
	
	with Pool() as p:
		p.map(even,No)
	
if __name__ == "__main__":
	main()