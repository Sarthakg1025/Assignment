import threading


def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def display_primes(numbers):
   
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
   
    print(f"Prime numbers found: {primes}\n", end="")

def display_non_primes(numbers):
   
    non_primes = []
    for num in numbers:
        if not is_prime(num):
            non_primes.append(num)
    print(f"Non-prime numbers found: {non_primes}\n", end="")

def main():
   
    n=int(input("Enter numbers :"))
    numbers_list = []
    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        numbers_list.append(number)

    print(f"Original List: {numbers_list}\n")

    
    prime_thread = threading.Thread(target=display_primes, args=(numbers_list,),name="Prime")
    non_prime_thread = threading.Thread(target=display_non_primes, args=(numbers_list,), name="NonPrime")

   
    prime_thread.start()
    non_prime_thread.start()

  
    prime_thread.join()
    non_prime_thread.join()

if __name__ == "__main__":
    main()  