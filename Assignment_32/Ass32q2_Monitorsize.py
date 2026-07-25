import os
import time
import schedule
from datetime import datetime

def monitor_file():
    File_path = "sample.txt"


    Log_File = "FileSizeLog.txt"
    
    with open(Log_File, "a") as log:
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if os.path.exists(File_path):
            size = os.path.getsize(File_path)

            log.write(f"Date & Time : {now}\n")
            log.write(f"File Path   : {os.path.abspath(File_path)}\n")
            log.write(f"File Size   : {size} bytes\n")
            log.write("-" * 40 + "\n")

            print(f"Logged: {size} bytes")

        else:
            log.write(f"Date & Time : {now}\n")
            log.write(f"Error       : File does not exist.\n")
            log.write("-" * 40 + "\n")

            print("File does not exist.")


def main():
    print("Monitoring started... Press Ctrl+C to stop.")


    schedule.every(30).seconds.do(monitor_file)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()