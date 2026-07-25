import os
import time
import schedule




def read_file():
    File_path = "sample.txt"
    try:
        if not os.path.exists(File_path):
            print("Error: File does not exist.")
            return

        if not os.access(File_path, os.R_OK):
            print("Error: Permission denied.")
            return

        with open(File_path, "r") as file:
            content = file.read()

            if content.strip() == "":
                print("Error: File is empty.")
            else:
                print("\n----- File Contents -----")
                print(content)
                print("-------------------------")

    except OSError:
        print("Error: File cannot be opened.")


def main():
    print("Reading file every minute... Press Ctrl+C to stop.")

    # Schedule the task every minute
    schedule.every(10).seconds.do(read_file)

    # Optional: Read immediately when the program starts
    read_file()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()