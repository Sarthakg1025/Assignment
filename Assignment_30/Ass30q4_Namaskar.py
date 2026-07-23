import schedule
import time
import datetime

displayMessage = lambda msg : print(msg, f"{datetime.datetime.now()}")

def main():
    schedule.every().day.at("09:00:00").do(lambda : displayMessage("Namaskar..."))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()