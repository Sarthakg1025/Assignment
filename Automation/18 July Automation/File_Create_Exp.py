def main():
    try:

        open("Demo.txt","w")
        print("File Gets Open")

    except FileNotFoundError as fobj:
        print("File is not present in current at Directory")
if __name__ == "__main__":
    main()