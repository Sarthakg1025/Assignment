import multiprocessing
import os

def CalcCountOfEvenNumUptoN(num):
    count = 0
    for i in range(2, num+1, 2):
        count = count + 1
    return (count, os.getpid())

def main():
    list_size = int(input("Enter the size of list of numbers: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number: ")))
    
    pobj = multiprocessing.Pool()
    result = pobj.map(CalcCountOfEvenNumUptoN, num_list)
    pobj.close()
    pobj.join()

    mapped_res = zip(num_list, result)
    for num, [count, pid] in mapped_res:
        print("-"*40)
        print(f"\n Input Number: {num}\n Count of Even Numbers upto {num} is: {count}\n Processe ID: {pid}\n")
        print("-"*40)

if(__name__ == "__main__"):
    main()