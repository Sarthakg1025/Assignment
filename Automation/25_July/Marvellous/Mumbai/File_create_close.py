def main():
    try:

        fobj=open("Demo.txt","w")
        print("File Gets Open")
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current at Directory")
if __name__ == "__main__":
    main()