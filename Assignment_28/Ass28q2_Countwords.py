def main():
    filename=input("Enter the file name : ")

    try:
        fobj=open(filename,"r")
        print("File is open...")
        wordcount=0

        for line in fobj:
            word=line.split()
            wordcount += len(word)

        print("Total words is : ",wordcount)            

    except Exception as e:
        print("An error occured : ",e)

if __name__ == "__main__":
    main()