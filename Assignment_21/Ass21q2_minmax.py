import threading

def find_max(numbers):
    max_val = max(numbers)
    print(f"\nMaximum element is: {max_val}")

def find_min(numbers):
    min_val = min(numbers)
    print(f"Minimum element is: {min_val}")

def main():
  
    n = int(input("Enter numbers separated by spaces: "))
    
   
    numbers_list = []
    for i in range(n):
        number = int(input())
        numbers_list.append(number)

  
    thread1 = threading.Thread(target=find_max, args=(numbers_list,))
    thread2 = threading.Thread(target=find_min, args=(numbers_list,))

   
    thread1.start()
    thread2.start()

   
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()