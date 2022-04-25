import re


def main(user_input):

    f = open(".\page_source\\"+user_input, "r")
    for line in f.readlines():
        pricematch = re.search('(price-whole[<\/a-zA-Z>"&;]{0,50})([\d]+,?[\d]+)', line)
        namematch = re.search('(a-text-normal[">]+)([\w\s\-\/\(\)\.,\+]+)(<)', line)
        if namematch:
            if pricematch:
                print(namematch.group(2))
                print(pricematch.group(2))
    f.close()

if __name__ == "__main__":

    main()