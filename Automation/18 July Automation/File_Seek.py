#kuthe kuthun

#0=
#1=
#2=end


def main():
    try:

        fobj=open("Demo.txt","r")
        print("File Gets Opened")
        Data=fobj.read()
        print(Data)
        fobj.seek(10)

        Data=fobj.read()

        print("After Seek :",Data)



    except FileNotFoundError as fobj:
        print("File is not present in current at Directory")
if __name__ == "__main__":
    main()