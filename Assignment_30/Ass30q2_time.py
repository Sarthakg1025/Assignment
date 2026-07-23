import schedule
import time
import datetime

displayMessage = lambda msg : print(msg)
getCustomDate= lambda : f'Current Date and Time is:  {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}'

def main():
    schedule.every(1).minutes.do(lambda : displayMessage(getCustomDate()))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()