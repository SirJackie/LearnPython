import os

def Search(KeyWord=None, ThisPath=None, Mode="Search", TargetList=[]):
    if Mode == "Report":
        return TargetList

    print("Searching", ThisPath, "...")
    Folders = [x for x in os.listdir(ThisPath) if os.path.isdir(os.path.join(ThisPath, x))]
    for Folder in Folders:
        Search(KeyWord, os.path.join(ThisPath, Folder))

    Files = [x for x in os.listdir(ThisPath) if os.path.isfile(os.path.join(ThisPath, x))]
    for File in Files:
        if File.find(KeyWord) != -1:
            TargetList.append(os.path.join(ThisPath, File))

def Main():
    os.system("cls")
    KeyWord = input("Please input word you want to search:")
    Search(KeyWord, os.path.abspath("."))
    TargetList = Search(Mode="Report")

    # Print Result
    print("========================================")
    print("Result : ")
    for Target in TargetList:
        print(Target[len(os.path.abspath(".")):])
    print("========================================")

if __name__ == "__main__":
    Main()
