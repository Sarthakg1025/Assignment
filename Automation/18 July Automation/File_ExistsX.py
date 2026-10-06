import os
def main():

    

    if os.path.exists("Demo.txt"):
        print("File is Current in Folder..")
    else:
        print("File is Not Found")

if __name__ == "__main__":
    main()