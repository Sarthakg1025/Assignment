import sys

def main():

    if (len(sys.argv)!=2):
        print(len(sys.argv))
        DirectoryName = sys.argv[1]
        print("number of argument : ",DirectoryName)
        
    else:
        print("Invalid number of argument ")

   

if __name__ == "__main__":
    main()
