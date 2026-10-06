import os
def main():

    ret= os.path.exists("Demo.txt")

    if ret==True:
        print("File is Current in Folder..")
    else:
        print("File is Not Found")

if __name__ == "__main__":
    main()