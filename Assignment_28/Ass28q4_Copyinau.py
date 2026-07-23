import sys
import os 

def Readfile(filename):
    fobj=open(filename)
    filecontent=fobj.read()

    fobj.close()
    return filecontent

def Createfile(newfilename,existingFileContent):
    fobj=open(newfilename,"w")
    fobj.write(existingFileContent)
    fobj.close

    return True

def Check(file_name):
    ret=os.path.exists(file_name)
    return ret

def main():

    existingfileName,newFilename=sys.argv[1],sys.argv[2]

     
    if Check(existingfileName):
        existingfileContent=Readfile(existingfileName)
        isCreateSuccess=Createfile(newfilename=newFilename,existingFileContent=existingfileContent)

        if isCreateSuccess:
            print(f"File {newFilename} created and pasted content of {existingfileName}in newly created file is Done ")

        else:
            print(f"File {newFilename} is not a created..")

    else:
        print(f"Unable to read {existingfileName}: File not found")
    


if __name__ == "__main__":
    main()
