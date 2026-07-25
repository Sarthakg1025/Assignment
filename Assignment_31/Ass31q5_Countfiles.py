import os
import time
import schedule
from datetime import datetime


def log_directory_stats(target_dir, log_file):
    items = os.listdir(target_dir)

    file_count = sum(
        1 for item in items
        if os.path.isfile(os.path.join(target_dir, item))
    )

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"Directory Path : {os.path.abspath(target_dir)}\n"
        f"Number of Files: {file_count}\n"
        f"Date and Time  : {current_time}\n"
        f"{'-' * 40}\n"
    )

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"Logged status at {current_time}")


def main():
    target_dir = input("Enter the full path of the directory to monitor: ").strip()
    log_file = "CountLog.txt"

    if not os.path.isdir(target_dir):
        print("Invalid directory path!")
        return

    log_directory_stats(target_dir, log_file)

    schedule.every(5).seconds.do(
        log_directory_stats,
        target_dir=target_dir,
        log_file=log_file
    )

    print(f"Monitoring started. Logging to '{log_file}' every 5 minutes.")
    print("Press Ctrl + C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()