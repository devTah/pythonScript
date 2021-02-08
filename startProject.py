import sys
import os


def startReactProject(path):
    os.chdir(path)
    os.system("start cmd /K code .")
    os.system("start cmd /K npm run start")


def main():
    try:
        path = sys.argv[1]

        fileSize = os.stat(path).st_size
        if fileSize == 0:
            raise Exception("Empty paths file")

        with open(path) as f:
            for line in f:
                line = line.rstrip()
                startReactProject(line)
    except IndexError:
        print("Not found paths file")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
