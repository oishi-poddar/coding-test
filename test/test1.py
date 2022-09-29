import os

def getListOfFiles(dirName, extension = '.txt'):

    total_lines = 0
    listOfFile = os.listdir(dirName)
    print(listOfFile)
    allFiles = list()
    for file in listOfFile:
        # Create full path
        print("file", file)
        fullPath = os.path.join(dirName, file)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            print(file)
            if file.endswith(extension):
                print("yaay",file)
                allFiles.append(fullPath)



    return allFiles

print("hello")
# /Users/apple/Downloads
dirName = '/test/';
# Get the list of all files in directory tree at given path
allFiles = getListOfFiles(dirName, ".py")
print("list,", allFiles)

total_lines = 0
total_num_files = len(allFiles)
print(allFiles)
for file in allFiles:
    fp = open(file, 'r')
    num_lines= len(fp.readlines())
    # print('Total lines:',file, file)  # 8
    total_lines+=num_lines
    fp.close()
print("Total lines",total_lines)
# check for divide by zero
print("avg", total_lines/total_num_files)