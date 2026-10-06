import psutil
import sys
import os

def platformSurvillence(Foldername):
    Border="-"*50
    Ret = False
    Ret=os.path.exists(Foldername)
    if Ret == True:
        Ret=os.path.isdir(Foldername)
        if Ret == False:
            print("Unable to processed as Directory name is existing but its not a directory")

            return 

    else:
        os.mkdir(Foldername)
        print("Directory fror the logfile gets created Succesfully")



def main():
    Border="-"*50
    print(Border)
    print("-------Marvellous Platfrom Survillence System --------")
    print(Border)
    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h"or sys.argv[1]=="--H"):
            print("This automation script is use to perform")
            print("1 : It fetch the informaton of running processess")
            print("2 : It fetch information about the primary storage as Ram")
            print("3 : It fetch information about the secondary storage as HDD ")
            print("4 : It fetch information about the microprocessorss ")
        elif(sys.argv[1]=="--u"or sys.argv[1]=="--U"):
            print("Use the automation script as : ")
            print(f"Use python {sys.argv[0]} Time Interval Folder Name")
            
        else:
            print("Unable to processed as there is no matching argument")
    elif (len(sys.argv)==3):
        platformSurvillence(sys.argv[2])
    else:
        print("Invalid Number of Arguments.")
        print("Arguments are not matching.")
        print("Number of Arument are not mathchin plzz use  --h or --u flag to get more details.")
    print(Border)
    print("------Thank You For Using Our Automation System -------")
    print(Border)
   
if __name__ == "__main__":
    main()
