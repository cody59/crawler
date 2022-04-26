from initialize import check
from initialize import upgrade
import getHtml

def main():
    check()

    start = 1

    while start == 1:

        user = input("Select a Browser:")

        if user.lower() == "upgrade":
            upgrade()

        elif user.lower() == "chrome":

            getHtml.getHtmlChrome()

        elif user.lower() == "firefox":

            getHtml.getHtmlFirefox()

        elif user.lower() == "chromium":

            getHtml.getHtmlChromium()

        elif user.lower() == "edge":

            getHtml.getHtmlEdge()

        elif user.lower() == "ie":

            getHtml.getHtmlIe()

        elif user.lower() == "brave":

            getHtml.getHtmlBrave()

        elif user.lower() == "opera":

            getHtml.getHtmlOpera()

        elif user == "exit":

            start = 0

        else:
            print("\ninvalid command\n")
            print("COMMANDS:\n\tchrome\n\tfirefox\n\tchromium\n\tedge\n\tie (internet explorer)\n\tbrave\n\topera\n\tupdate\n\texit\n ")


if __name__ == "__main__":

    main()