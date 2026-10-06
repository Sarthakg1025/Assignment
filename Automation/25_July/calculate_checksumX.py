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

def main():
    ret=Cal("Demo.txt")
    print("Checksum is : ",ret)

if __name__ == "__main__":
    main()


