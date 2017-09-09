from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

def get_link_to_bloomberg(company_name):

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	
	if len(company_name.split(" ")) > 1:
		company_name = company_name.split(" ")
		search_key_words = '{}+{}+bloomberg+snapshot'.format(company_name[0], company_name[1])
	else:
		search_key_words = '{}+bloomberg+snapshot'.format(company_name)


	url = 'https://www.google.com/search?source=hp&q={}'.format(search_key_words)

	driver.get(url)

	# Xpath will find a subnode of h3, a[@href] specifies that we only want <a> nodes with
	# any href attribute that are subnodes of <h3> tags that have a class of 'r'

	links = driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")



	link = links[0].get_attribute('href')
	# print (link)

	regex = re.compile(r'www\.bloomberg\.com/research/stocks/private/snapshot\.asp%3Fprivcapid%\d\w(\d+)&', flags = re.I)

	privcapid = re.search(regex, link).group(1)

	driver.quit()

	if privcapid:
		# print(privcapid)

		result = "https://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapId={}".format(privcapid)
		print (result)

		return result

	else:
		return "not found"

	

# print (get_link_to_bloomberg("silent circle")) 


def get_address_from_bloomberg(url):

	if url != "not found":

		driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

		driver.get(url)

		time.sleep(3)

		soup = BeautifulSoup(driver.page_source, "lxml")

		driver.quit()

		# print (soup.prettify())

		div = soup.find("div", {'id': 'detailsContainer'})

		# print (div)

		address_div = div.find("div", {'itemprop': 'address'})

		if address_div:
			result = []
			ptags = address_div.find_all('p')
			for ptag in ptags:

				txt = re.sub(r'&nbsp;', ' ', ptag.text)

				result.append(ptag.text)

			print (" ".join(result))
			return " ".join(result)

		else:
			print ("bloomberg profile not found")
			return "not found"

	else:
		print ("google link not found")
		return "not found"



url = "https://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapid=84932083"

# print (get_address_from_bloomberg(get_link_to_bloomberg("PAX Labs, Inc")))

# print (get_address_from_bloomberg("https://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapid=84932083"))

def get_address_from_bloomberg_merged(company_name):

	return get_address_from_bloomberg(get_link_to_bloomberg(company_name))

# print (get_address_from_bloomberg_merged("2U"))