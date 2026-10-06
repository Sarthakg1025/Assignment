def main():
    try:

        fobj=open("Demo.txt","w")
        print("File Gets Open")
        fobj.write("Jay Ganesh...")
        fobj.write("Jay")
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current at Directory")
if __name__ == "__main__":
    main()