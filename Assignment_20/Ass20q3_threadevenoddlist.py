import threading

def even_list(numbers):
    evens=[]
    for num in numbers :
            if num % 2 == 0 :
                evens.append(num)

    total_sum = sum(evens)
    print(f"EvenList Thread - Even numbers: {evens}")
    print(f"EvenList Thread - Sum: {total_sum}\n")

def odd_list(numbers):
    odds=[]
    for num in numbers :
        if num % 2 != 0 :
            odds.append(num)
    
    total_sum = sum(odds)
    print(f"OddList Thread - Odd numbers: {odds}")
    print(f"OddList Thread - Sum: {total_sum}\n")


def main():

    input_list = [11,21,51, 12, 14, 15, 16, 17, 18, 19,17,10]
    
   
    EvenList = threading.Thread(target=even_list, args=(input_list,), name="EvenList")
    OddList = threading.Thread(target=odd_list, args=(input_list,), name="OddList")
    
   
    EvenList.start()
    OddList.start()
    
    
    EvenList.join()
    OddList.join()
    
    

if __name__ == "__main__":
    main()