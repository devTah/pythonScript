import os
# root = os.path.dirname(__file__)
arrPath = ['C:\\Users\\huypo\\Downloads',
           'C:\\Users\\huypo\\Downloads\\text or code']


def commandLine(params):
    if(params == arrPath[0]):
        path = os.chdir(params)
        os.system("start cmd /K py filterTool.py")
    if(params == arrPath[1]):
        path = os.chdir(params)
        # os.system("start cmd /K py test.py diginet.txt")
        os.system("start cmd /K py test.py vvsolution.txt")



if __name__ == "__main__":
    print("input 0 to filter, input 1 to open project")
    print("test.py diginet.txt")
    # print(arrPath[0])
    pathCode = int(input())
    commandLine(arrPath[pathCode])
