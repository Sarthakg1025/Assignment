def readfile(filename):
    fobj=open(filename)
    filecount = fobj.read()

    fobj.close()

    return filecount

def main():
    filen=input("Enter the file name : ")
    ret=readfile(filen)
    print(ret)
if __name__ == "__main__":
    main()
