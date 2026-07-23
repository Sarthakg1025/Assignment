import os 
import sys

def Readfile(filename):
    fobj=open(filename)
    file=fobj.read()
    fobj.close()

    return file

def Checkfile(filename):
    return os.path.exists(filename)

def main():
    filename=sys.argv[1]

    if Checkfile(filename):
        print(f"{filename} is exists in the folder..")
        ret= Readfile(filename)
        print(f"Read {filename} in file content {ret}")
    else:
        print(f"Noo {filename} is not exists in the folder.")
if __name__ == "__main__":
    main()

