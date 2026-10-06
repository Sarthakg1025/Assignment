import hashlib,os,sys

def Cal(fileName):
    fobj=open(fileName,"rb")

    hobj=hashlib.md5()
    buffer=fobj.read(1024)

    while (len(buffer)> 0):
        hobj.update(buffer)
        buffer=fobj.read(1024)

    fobj.close()

    checkjsum=hobj.hexdigest()

    return checkjsum
def FindDuplicate(dirname):
    ret=False
    ret=os.path.exists(dirname)

    if ret == False:
        print("Path invaild")
        return 

    ret = os.path.isdir(dirname)

    if ret == False:
        print("It is not a directory..")

    Duplicate={}
    same=0
    unique=0

    for foldername, subfoldername,filename in os.walk(dirname):
        print(filename)
        for fname in filename:
            fname= os.path.join(foldername,fname)
            print(fname)
            checksum= Cal(fname)

            print(f"{filename}:{checksum}")

        if checksum in Duplicate:
            same = same + 1
        else:
            unique= unique + 1

    print("Unique files found: Unique",unique)
    print("Duplicate file found: Duplicates ",same)


def main():
    FindDuplicate("test")

if __name__ == "__main__":
    main()


