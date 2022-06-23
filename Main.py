from initialize import check
from initialize import upgrade
from tkinter import *
import getHtml
from GUI import GUI

def main():
    check()

    root = Tk()
    root.geometry("400x400")
    b = GUI(root)
    root.mainloop()

    start = 1

    while start == 1:

        user = input("Select a Browser:")

        if user.lower() == "upgrade":
            upgrade()

        elif user.lower() == "chrome":

            getHtml.getHtmlChrome()

        elif user.lower() == "firefox":

            getHtml.getHtmlFirefox()

        elif user.lower() == "edge":

            getHtml.getHtmlEdge()

        elif user.lower() == "ie":

            getHtml.getHtmlIe()

        elif user.lower() == "opera":

            getHtml.getHtmlOpera()

        elif user == "exit":

            start = 0

        else:
            print("\ninvalid command\n")
            print("COMMANDS:\n\tchrome\n\tfirefox\n\tchromium\n\tedge\n\tie (internet explorer)\n\tbrave\n\topera\n\tupdate\n\texit\n ")

