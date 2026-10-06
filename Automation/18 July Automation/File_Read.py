def main():
    try:

        fobj=open("Demo.txt","r")
        print("File Gets Opened")
        Data=fobj.read(10)
        fobj.close()
        print(Data)
    except FileNotFoundError as fobj:
        print("File is not present in current at Directory")
if __name__ == "__main__":
    main()