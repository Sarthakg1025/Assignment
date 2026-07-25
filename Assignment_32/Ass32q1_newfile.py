from datetime import datetime
import schedule
import time


def create_file():
   
    now = datetime.now()

    
    filename = now.strftime("File_%d_%m_%Y_%H_%M_%S.txt")

   
    with open(filename, "w") as file:
        file.write(f"Filename      : {filename}\n")
        file.write(f"Creation Date : {now.strftime('%d-%m-%Y')}\n")
        file.write(f"Creation Time : {now.strftime('%H:%M:%S')}\n")

    print(f"{filename} created successfully.")


def main():
    schedule.every(1).minutes.do(create_file)

    print("Program started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

    