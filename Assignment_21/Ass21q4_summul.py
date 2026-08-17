import threading

def compute_sum(numbers, results):
    
    results['sum'] = sum(numbers)
    return results

def compute_product(numbers, resultsX):
   
    total_product = 1
    for num in numbers:
        total_product *= num
    resultsX['product'] = total_product
    return resultsX

def main():
    n=int(input("Enter the number : "))
    shared_list = []
    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        shared_list.append(number)
    print(f"Input List: {shared_list}\n")

    
    thread_results = {}

   
    thread1 = threading.Thread(target=compute_sum, args=(shared_list, thread_results))
    thread2 = threading.Thread(target=compute_product, args=(shared_list, thread_results))


    thread1.start()
    thread2.start()

  
    thread1.join()
    thread2.join()

   
    print("--- Final Results ---")
    print(f"Sum of elements: {thread_results.get('sum')}")
    print(f"Product of elements: {thread_results.get('product')}")

if __name__ == "__main__":
    main()