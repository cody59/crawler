#Ver 1 of the script
import lxml.html
import requests

def main():
	userInput = raw_input("Enter the website you want to scrape (ex Amazon.com): ")
	userInput='https://www.'+userInput
	print(userInput)
	
	product = raw_input("What product would you like to search for: ")
	print(product)
	
	page = requests.get(userInput)
	tree = lxml.html.fromstring(page.content)
	print(tree)

if __name__ == "__main__":
	main()
