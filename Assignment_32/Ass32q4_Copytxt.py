import os
import shutil
import time
import schedule
from datetime import datetime




def copy_txt_files(source_dir, destination_dir):
    Log_File = "CopyLog.txt"
    
    if not os.path.isdir(source_dir):
        print("Error: Source directory does not exist.")
        return

    if not os.path.isdir(destination_dir):
        print("Error: Destination directory does not exist.")
        return

    with open(Log_File, "a") as log:
        log.write(f"\n===== {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} =====\n")

        for file_name in os.listdir(source_dir):
            if file_name.endswith(".txt"):
                source_file = os.path.join(source_dir, file_name)
                destination_file = os.path.join(destination_dir, file_name)

                try:
                    shutil.copy2(source_file, destination_file)
                    print(f"Copied: {file_name}")
                    log.write(f"Copied: {file_name}\n")

                except Exception as e:
                    print(f"Failed to copy {file_name}: {e}")
                    log.write(f"Failed: {file_name} - {e}\n")


def main():
    source_dir = input("Enter Source Directory: ")
    destination_dir = input("Enter Destination Directory: ")

    
    schedule.every(10).seconds.do(copy_txt_files, source_dir, destination_dir)

    print("Copy service started... Press Ctrl+C to stop.")

    
    copy_txt_files(source_dir, destination_dir)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()