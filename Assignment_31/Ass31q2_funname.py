import schedule
import time

def DisplayMessage(msg):
    print(msg)

def main():
    ret=input("Enter the message : ")

    schedule.every(5).seconds.do(DisplayMessage,msg=ret)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
