import os
from datetime import datetime
import schedule
import time


def scan(directory_path):
    items = os.listdir(directory_path)

    total_files = 0
    total_subdirs = 0

    for item in items:
        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            total_files += 1
        elif os.path.isdir(item_path):
            total_subdirs += 1

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print(f"\nDirectory Scanned: {directory_path}")
    print(f"Total Files: {total_files}")
    print(f"Total Subdirectories: {total_subdirs}")
    print(f"Scan Time: {current_time}")


def main():
    target = input("Enter the directory path to scan: ").strip()

    scan(target)

    schedule.every(1).minutes.do(scan, directory_path=target)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()