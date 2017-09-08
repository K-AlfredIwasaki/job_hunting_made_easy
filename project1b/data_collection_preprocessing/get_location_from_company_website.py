


def get_location(url):

	from selenium import webdriver
	from bs4 import BeautifulSoup
	import re

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	src = driver.page_source

	regex = re.compile(r"\w+\s*\w*, ([A-Z]{2}) [0-9]{5}(-[0-9]{4})?")

	match = re.search(regex, src)
	print ("-")

	if not match:
		if url[-1] != "/":
			url = url + "/"
		
		contact_url = url + "contact/"
		print ("--")
		driver.get(contact_url)
		src = driver.page_source
		match = re.search(regex, src)

		if not match:
			about_url = url + "about/"
			driver.get(about_url)
			src = driver.page_source
			match = re.search(regex, src)

	driver.close()


	if match:
		print (match.group(0))
		return match.group(0)
	else:
		print ("not found")
		return "not found"


# print (get_location("http://www.scribblelive.com/"))

