import sys
import os

def MatchSearchTerm(fileName, searchTerm):
    fobj = open(fileName)
    lines = fobj.readlines()
    searchTermFoundCount = 0
    for line in lines:
        searchTermFoundCount = searchTermFoundCount + line.count(searchTerm)

    fobj.close()
    
    return searchTermFoundCount


def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    fileName, searchTerm = sys.argv[1], sys.argv[2]

    if ChkFileExists(fileName):
        searchTermFoundCount = MatchSearchTerm(fileName, searchTerm)
        print(f"Number of occurances of '{searchTerm}' in '{fileName}': {searchTermFoundCount}")
    else:
        print(f"Unable to read number occurances of '{searchTerm}' in '{fileName}': File not found")

if(__name__ == "__main__"):
    main()