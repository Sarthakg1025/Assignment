import schedule
import time

def Jayganesh():
    print("Jay Ganesh....")

def main():
    schedule.every(2).seconds.do(Jayganesh)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()