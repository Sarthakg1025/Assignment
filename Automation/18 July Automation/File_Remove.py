import os
def main():
    try:
        #fobj.remove()->Not Applic
        os.remove("Demo.txt")
        
    except FileNotFoundError as fobj:
        print("File is not present in current at Directory")
if __name__ == "__main__":
    main() 