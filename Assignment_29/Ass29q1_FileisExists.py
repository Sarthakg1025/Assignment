import os 
import sys

def Checkfile(filename):
    return os.path.exists(filename)

def main():
    filename=sys.argv[1]

    if Checkfile(filename):
        print(f"{filename} is exists in the folder..")
    else:
        print(f"Noo {filename} is not exists in the folder.")
if __name__ == "__main__":
    main()

