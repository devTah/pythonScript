import os
import shutil
import re
import time
import subprocess

# Move a file from the directory d1 to d2
error = ""


def filterImage():
    global error
    filelist = os.listdir('./')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not(fichier.endswith(".png") or fichier.endswith(".jpeg") or fichier.endswith(".gif") or fichier.endswith(".jpg")):
            filelist.remove(fichier)
    if (len(filelist) > 0):
        if not os.path.exists("images"):
            os.makedirs("images")
            print("Directory ", "images",  " Created ")
        else:
            print("Directory ", "images",  " already exists")
        for value in filelist:
            try:
                if(value.endswith(".gif")):
                    filterGif(value)
                else:
                    shutil.move(str(value), './images/' + str(value))
            except Exception as e:
                print(e)
                print("close the file then try again!!!")
                error = e

def filterGif(value):
    global error
    if not os.path.exists("Gifs"):
        os.makedirs("Gifs")
        print("Directory ", "Gifs",  " Created ")
    else:
        print("Directory ", "Gifs",  " already exists")
    try:
        shutil.move(str(value), './Gifs/' + str(value))
    except Exception as e:
        print(e)
        print("close the file then try again!!!")
        error = e


def filterWord():
    global error
    filelist = os.listdir('./')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not(fichier.endswith(".doc") or fichier.endswith(".docx") or fichier.endswith(".xlsx") or fichier.endswith(".xls")):
            filelist.remove(fichier)
    if (len(filelist) > 0):
        if not os.path.exists("words"):
            os.makedirs("words")
            print("Directory ", "words",  " Created ")
        else:
            print("Directory ", "words",  " already exists")
        for value in filelist:
            try:
                shutil.move(str(value), './words/' + str(value))
            except Exception as e:
                print(e)
                print("close the file then try again!!!")
                error = e


def filterPowerpoint():
    global error
    filelist = os.listdir('./')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not(fichier.endswith(".pptx")):
            filelist.remove(fichier)
    if (len(filelist) > 0):
        if not os.path.exists("powerpoints"):
            os.makedirs("powerpoints")
            print("Directory ", "powerpoints",  " Created ")
        else:
            print("Directory ", "powerpoints",  " already exists")
        for value in filelist:
            try:
                shutil.move(str(value), './powerpoints/' + str(value))
            except Exception as e:
                print(e)
                print("close the file then try again!!!")
                error = e


def filterPdf():
    global error
    filelist = os.listdir('./')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not(fichier.endswith(".pdf")):
            filelist.remove(fichier)
    if (len(filelist) > 0):
        if not os.path.exists("Pdfs"):
            os.makedirs("Pdfs")
            print("Directory ", "Pdfs",  " Created ")
        else:
            print("Directory ", "Pdfs",  " already exists")
        for value in filelist:
            try:
                shutil.move(str(value), './Pdfs/' + str(value))
            except Exception as e:
                print(e)
                print("close the file then try again!!!")
                error = e


def filterZip():
    global error
    filelist = os.listdir('./')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not(fichier.endswith(".zip") or fichier.endswith(".rar") or fichier.endswith(".rar4")):
            filelist.remove(fichier)
    if (len(filelist) > 0):
        if not os.path.exists("Zips"):
            os.makedirs("Zips")
            print("Directory ", "Zips",  " Created ")
        else:
            print("Directory ", "Zips",  " already exists")
        for value in filelist:
            try:
                shutil.move(str(value), './Zips/' + str(value))
            except Exception as e:
                print(e)
                print("close the file then try again!!!")
                error = e


def filterExe():
    global error
    filelist = os.listdir('./')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not(fichier.endswith(".exe") or fichier.endswith(".msi")):
            filelist.remove(fichier)
    if (len(filelist) > 0):
        if not os.path.exists("Exe"):
            os.makedirs("Exe")
            print("Directory ", "Exe",  " Created ")
        else:
            print("Directory ", "Exe",  " already exists")
        for value in filelist:
            try:
                shutil.move(str(value), './Exe/' + str(value))
            except Exception as e:
                print(e)
                print("close the file then try again!!!")
                error = e


def filterOtherFile():
    global error
    filelist = os.listdir('./')
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        lowerText = fichier.lower()
        if lowerText.startswith("filtertool") or not(lowerText.endswith(".svg") or lowerText.endswith(".txt") or lowerText.endswith(".js") or lowerText.endswith(".py") or lowerText.endswith(".cpp") or lowerText.endswith(".cs") or lowerText.endswith(".asta") or lowerText.endswith(".html") or lowerText.endswith(".css") or lowerText.endswith(".scss")):
            filelist.remove(fichier)
    if (len(filelist) > 0):
        if not os.path.exists("text or code"):
            os.makedirs("text or code")
            print("Directory ", "text or code",  " Created ")
        else:
            print("Directory ", "text or code",  " already exists")
        for value in filelist:
            try:
                shutil.move(str(value), './text or code/' + str(value))
            except Exception as e:
                print(e)
                print("close the file then try again!!!")
                error = e


class objectOfFunc:
    def __init__(self, key, func):
        self.key = key
        self.func = func


funcFilter = []
funcFilter.append(objectOfFunc("images" or "img", filterImage))
funcFilter.append(objectOfFunc("img", filterImage))
funcFilter.append(objectOfFunc("word" or "docx", filterWord))
funcFilter.append(objectOfFunc("docx", filterWord))
funcFilter.append(objectOfFunc("powerpoints", filterPowerpoint))
funcFilter.append(objectOfFunc("pptx", filterPowerpoint))
funcFilter.append(objectOfFunc("pdfs", filterPdf))
funcFilter.append(objectOfFunc("zips", filterZip))
funcFilter.append(objectOfFunc("rar4", filterZip))
funcFilter.append(objectOfFunc("exe", filterExe))


if __name__ == "__main__":
    try:
        while (error != "" or True):
            print(
                "Press Enter to filter all the path file or filter something that you want")
            filters = input()
           
            # split input to array with no ,.>?:"';[]{}+_-)("
            array = re.split("\W", filters)
            # remove blank space value in array
            while("" in array):
                array.remove("")

            subs = " ".join(array).lower()

            if (filters == "" or filters == "all"):
                # try:
                filterExe()
                filterImage()
                filterPdf()
                filterPowerpoint()
                filterWord()
                filterZip()
                filterOtherFile()
                time.sleep(3)
                
            # except ValueError as e:
            #     print (e)
            else:
                for obj in funcFilter:
                    for value in array:
                        if value in obj.key:
                            # print(obj.key)
                            obj.func()
            if(error == ""):
                break
            else: 
                error = ""
    except ValueError as e:
        print(e)
    else:
        print('all done, bye')
        os.system('pause')
