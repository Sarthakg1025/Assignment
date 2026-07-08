import threading


def even_fact(number):
   
    even = []
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 == 0:
            even.append(i)

    total_sum = sum(even)
    print(f"Even Factors: {even}")
    print(f" Sum of even factors: {total_sum}")


def odd_fact(number):
    
    odd = []
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 != 0:
            odd.append(i)

        

    total_sum = sum(odd)
    print(f"Odd Factors: {odd}")
    print(f" Sum of odd factors: {total_sum}")


def main():
    
    input_number = int(input("Enter a number: "))
   

    
    even_thread = threading.Thread(target=even_fact, args=(input_number,), name="EvenFactor")
    odd_thread = threading.Thread(target=odd_fact, args=(input_number,), name="OddFactor")

   
    even_thread.start()
    odd_thread.start()

   
    even_thread.join()
    odd_thread.join()

    
   


if __name__ == "__main__":
    main()