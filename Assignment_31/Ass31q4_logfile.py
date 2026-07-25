import os
import schedule
import time
from datetime import datetime


def create_log():
    now = datetime.now()

    file_date = now.strftime("%d_%m_%Y_%H_%M_%S")
    file_name = f"Marvellous_{file_date}.txt"

    content_date = now.strftime("%d-%m-%Y %I:%M:%S %p")
    file_content = f"Log file created successfully. Creation Time: {content_date}"

    with open(file_name, "w") as f:
        f.write(file_content)

    print("Created:", file_name)


def main():
    schedule.every(1).seconds.do(create_log)

    print("Log creator started with schedule.")
    print("When your work is done, press Ctrl + C.")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()