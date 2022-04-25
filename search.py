import re


def main(user_input):

    f = open(".\page_source\\"+user_input, "r")
    for line in f.readlines():
        #nameline = line
        pricematch = re.search('(price-whole[<\/a-zA-Z>"&;]{0,50})([\d]+,?[\d]+)', line)
        namematch = re.search('(a-size-medium a-color-base a-text-normal[">]+)([\w\s\-\/\(\)\.,\+]+)(<)', line)
        #match = re.search('(price-whole[<\/\w>"&;]*)([\d]+,*[\d]+)', line)
        if namematch:
            #print(line)
            print(namematch.group(2))
            if pricematch:
                print(pricematch.group(2))
            #print(pricematch.group(2))
            #print(re.search('price(\w//)+(/d)+', line))
    f.close()

if __name__ == "__main__":

    main()