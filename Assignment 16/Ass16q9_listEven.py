
def GetFirstNEvenNum(num):
    i = 1
    count = 0
    evn_num_lst = list()
    while count != num:
        if(checkEven(i)):
            evn_num_lst.append(i)
            count = count + 1
        i = i + 1
    return evn_num_lst

def printMsg(msg, end):
     print(msg, end=end)

checkEven = lambda num: True if num % 2 == 0 else False

def main():
    num = int(input("Enter how many even number you want? : "))
    evn_num_lst = GetFirstNEvenNum(num)
    for evn_num in evn_num_lst:
        printMsg(evn_num, "   ")
    

if(__name__ == "__main__"):
    main()