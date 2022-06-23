from tkinter import *
from initialize import check
from initialize import upgrade
import getHtml
import os


class GUI:

    def __init__(self, master):
        frame = Frame(master, width=700, height=700, bg="green")
        frame.pack()

        self.chromeBtn = Button(frame, text="Chrome", command=self.selectChrome)
        self.firefoxBtn = Button(frame, text="Firefox", command=self.selectFirefox)
        self.edgeBtn = Button(frame, text="Microsoft Edge", command=self.selectEdge)
        self.ieBtn = Button(frame, text="Internet Explorer", command=self.selectIe)
        self.operaBtn = Button(frame, text="Opera", command=self.selectOpera)

        self.chromeBtn.grid(row=0, column=0, sticky=W)
        self.firefoxBtn.grid(row=1, sticky=W)
        self.edgeBtn.grid(row=2, sticky=W)
        self.ieBtn.grid(row=3, sticky=W)
        self.operaBtn.grid(row=4, sticky=W)

        self.quit = Button(frame, text="Quit", command=frame.quit)
        self.quit.grid(row=0, column=3, sticky=E)

    def selectChrome(self):
        getHtml.getHtmlChrome()
        print("done")

    def selectFirefox(self):
        getHtml.getHtmlFirefox()
        print("done")

    def selectEdge(self):
        getHtml.getHtmlEdge()
        print("done")

    def selectIe(self):
        getHtml.getHtmlIe()
        print("done")

    def selectOpera(self):
        getHtml.getHtmlOpera()
        print("done")


def main():
    check()

    root = Tk()
    root.geometry("400x400")
    b = GUI(root)
    root.mainloop()



if __name__ == "__main__":
    main()
