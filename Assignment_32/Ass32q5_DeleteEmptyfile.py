import os
import time
import schedule
from datetime import datetime




def delete_empty_files(directory):
    Log_file = "sample.txt"
    
    if not os.path.isdir(directory):
        print("Error: Directory does not exist.")
        return

    with open(Log_file, "a") as log:
        log.write(f"\n===== {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} =====\n")

        
        for folder_name, subfolders, file_names in os.walk(directory):
            for file_name in file_names:
                file_path = os.path.join(folder_name, file_name)

                try:
                    
                    if os.path.getsize(file_path) == 0:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                        log.write(f"Deleted: {file_path}\n")

                except PermissionError:
                    print(f"Permission denied: {file_path}")
                    log.write(f"Permission denied: {file_path}\n")

                except Exception as e:
                    print(f"Error: {file_path} -> {e}")
                    log.write(f"Error: {file_path} -> {e}\n")


def main():
    directory = input("Enter directory path: ")

   
    schedule.every(1).seconds.do(delete_empty_files, directory)

    print("Empty file cleanup started... Press Ctrl+C to stop.")

   
    delete_empty_files(directory)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()