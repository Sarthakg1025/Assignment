import schedule
import time 


def Display(msg):
    print(msg)    


def main():
    print("Automation Script Started")
    ret=input("Enter the string : ")
    interval=int(input("Enter the interval second : "))        

    schedule.every(interval).seconds.do(Display,msg=ret)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

    print("Automation Ending")
    
if __name__ == "__main__":
    main() 