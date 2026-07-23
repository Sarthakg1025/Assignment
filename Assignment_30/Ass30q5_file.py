import schedule
import time
import datetime

def WriteInFile(fileName:str, text:str):
    fobj = open(fileName, "a")
    fobj.write(text+"\n")
    fobj.close()

getCustomDateTimeFormat = lambda : datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

def main():

    schedule.every(5).minutes.do(lambda : WriteInFile("marvellous.txt", f"Task executed at: {getCustomDateTimeFormat()}"))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()