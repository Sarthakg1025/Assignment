import threading
def even(No):
	for i in range(1,11):
		
		even_no=2 * i
		print(f"Number {i} : {even_no}")


def odd(No):
	for i in range(1,11):
		
		odd_no=2 * i-1
		print(f"Number {i} : {odd_no}")

def main():
	t1=threading.Thread(target=even(10))
	t2=threading.Thread(target=odd(10))
	
	t1.start()
	t2.start()

	t1.join()
	t2.join()
if __name__ == "__main__":
	main()
	