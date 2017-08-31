# reference for google search
# https://github.com/DanMcInerney/search-google/blob/master/search-google.py#L17

def get_link(company_name):

	from selenium import webdriver
	import time
	from bs4 import BeautifulSoup
	import re

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	linkedin_link_list = []
	
	if len(company_name.split(" ")) == 2:
		company_name = company_name.split(" ")
		search_key_words = '{}+{}+Linkedin'.format(company_name[0], company_name[1])
	else:
		search_key_words = '{}+Linkedin'.format(company_name)


	url = 'https://www.google.com/search?source=hp&q={}'.format(search_key_words)

	time.sleep(3)

	driver.get(url)

	# Xpath will find a subnode of h3, a[@href] specifies that we only want <a> nodes with
	# any href attribute that are subnodes of <h3> tags that have a class of 'r'

	links = driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")
	if links:
		pass
	else:
		print ("Failed to get the links")

	link = links[0].get_attribute('href')
	regex = '(https:\/\/www\.linkedin\.com\/company\/\w+-*\w*-*\w*-*\w*-*\w*)&'
	link = re.search(regex, link)

	# try three links
	num_trials = 0
	if link:
		link = link.group(1)
	else:
		while not link and num_trials < 3:
			num_trials += 1
			link = links[num_trials].get_attribute('href')


	print (link)

	driver.quit()

	return link

