# >> td id = "rhs_block"
# >> span class = "_tA"

from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time

# url = "https://www.google.com/search?rlz=1C1CHBF_enUS741US741&q=2U+company+address"

def get_company_address(company_name):

	url = 'https://www.google.com/search?source=hp&q={}+company+address'.format(company_name)

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, "lxml")

	# print (soup.prettify())

	td = soup.find('td', {'id': 'rhs_block'})

	# print (td)

	if td:
		span = td.find('span', class_ = "_tA")
		# print (span)

		if span:
			print (span.text)
			return span.text
			

		else:
			print ("not found")
			return "not found"

	else:
		print ("not found")
		return "not found"

	

# get_company_address("Fugue, Inc.")

