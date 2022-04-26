import os

def check():
    flag = 0

    webMan = os.popen("pip show webdriver-manager").read()
    sel = os.popen("pip show selenium").read()

    if os.path.isdir(".\\log") == False:
        os.mkdir(".\\log")
    if os.path.isdir(".\\page_source") == False:
        os.mkdir(".\\page_source")

    fwrite = open(".\\log\\tmp", "w")
    fwrite.write(webMan)
    fwrite.write("\n")
    fwrite.write(sel)
    fwrite.close()

    fread = open(".\\log\\tmp", "r")
    if "webdriver-manager" in fread.read():
        flag = 1
    else:
        installwebdriver()
    fread.close()

    fread = open(".\\log\\tmp", "r")
    if "selenium" in fread.read():
        flag = 2
    else:
        installselenium()
    fread.close()

    os.remove(".\\log\\tmp")


def installwebdriver():

    os.system("pip install webdriver-manager")


def installselenium():

    os.system("pip install selenium")


def upgrade():

    os.system("pip install --upgrade pip")
    os.system("pip install --upgrade webdriver-manager")
    os.system("pip install --upgrade selenium")


check()