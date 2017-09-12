
def get_location(url):

	from selenium import webdriver
	from bs4 import BeautifulSoup
	import re
	from selenium.common.exceptions import TimeoutException

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	try:
		driver.set_page_load_timeout(30)
		driver.get(url)
		src = driver.page_source
		regex = re.compile(r"\w+\s*\w*, ([A-Z]{2}) [0-9]{5}(-[0-9]{4})?")
		match = re.search(regex, src)
		driver.close()

	except TimeoutException as ex:
	    isrunning = 0
	    print("Exception has been thrown. ")
	    driver.close()
	    match = None


	if match:
		print (match.group(0))
		return match.group(0)
	else:
		print ("not found")
		return "not found"

def get_location_trials(url):
	result1 = get_location(url)
	if result1 != "not found":
		return result1
	else:
		print ("move onto to second trial")
		if url[-1] != "/":
			url = url + "/"
		contact_url = url + "contact/"

		result2 = get_location(contact_url)

		if result2 != "not found":
			return result2

		else: 
			print ("move onto to third trial")
			about_url = url + "about/"

			return get_location(about_url)


# print (trials("http://www.scribblelive.com/"))

