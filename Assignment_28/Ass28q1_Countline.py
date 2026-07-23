def main():
    filename=input("Enter the file name : ")

    try:
        fobj=open(filename,"r")
        print("File is open...")

        linecount=sum(1 for line in fobj)

        print("Total line count is : ",linecount)

    except Exception as e:
        print("An error occured : ",e)

if __name__ == "__main__":
    main()
