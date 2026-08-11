from multiprocessing import Pool
import time

def sum_powers(n):
	total = sum(i**5 for i in range(1, n + 1))
	
	return n, total

def main():
	no = [1000000, 2000000, 3000000, 4000000]

	start_time = time.time()

	with Pool() as pool:
		results = pool.map(sum_powers, no)

	end_time = time.time()

	for n, total in results:
		print(f"N = {n:4d} | Sum of 5th powers: {total:.4f}")

	print("-" * 50)
	print(f"Total execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
	main()