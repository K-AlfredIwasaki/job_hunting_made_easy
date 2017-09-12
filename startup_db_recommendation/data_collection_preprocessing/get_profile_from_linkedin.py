# header <div class="top-bar with-wide-image with-nav big-logo">
# company name <h1 class="name" itemscope="" itemtype="http://schema.org/Corporation">

# big container <div id="hero-img-about-section-wrapper">
# company desc <div class="basic-info-description">
# other info <div class="basic-info-about">
# other info including
# specialties
# website
# industry
# headquarters location
# company size
# founded
# companies that also viewed

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

class Company():
	"""docstring for Company"""
	def __init__(self):
		self.linkedin = ""
		self.name = ""
		self.specialties = ""
		self.industry = ""
		self.website = ""
		# self.country = ""
		# self.state = ""
		# self.city = ""
		self.location = ""
		self.company_size = ""
		self.desc = ""
		self.founded = ""
		self.also_viewed = {}



def get_company_info(url):

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	time.sleep(5)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	company = Company()
	company.linkedin = url

	header = soup.find('div', class_ = "top-bar with-wide-image with-nav big-logo")

	trial = 2
	while not header and trial > 0:
		print ("start to sleep for 1 min")

		time.sleep(60)

		print ("done for sleeping")

		driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
		driver.get(url)
		time.sleep(5)
		soup = BeautifulSoup(driver.page_source, 'lxml')
		header = soup.find('div', class_ = "top-bar with-wide-image with-nav big-logo")

		print ("middle check")

		trial += -1

	if not header:
		return company


	name_h = header.find('h1', class_ = "name")
	if name_h:
		company.name = name_h.text
	else:
		pass
	# print (company.name)

	big_container = soup.find('div', {'id': "hero-img-about-section-wrapper"})

	div_desc = big_container.find('div', class_ = "basic-info-description").text
	company.desc = div_desc

	div_other = big_container.find('div',class_ = "basic-info-about")
	# print (div_other.prettify())


	# <div class="specialties">
	# <li class="industry">
	# <li class="website">
	# <li class="vcard hq"> many <span> last one is country
	# <li class="company-size">desc
	# <li class="founded">

	specialty = div_other.find("div", class_ ="specialties")
	# print (specialty.text)
	if specialty:
		# print(True)
		company.specialties = specialty.text.replace("Specialties","")
		# print (specialty)
	else:
		pass
	# print (company.specialties)

	industry = div_other.find("li", class_ = "industry")
	if industry:
		company.industry = industry.text.replace("Industry","")
	else:
		pass

	website = div_other.find("li", class_ = "website")
	if website:
		company.website = website.text.strip("Website")
	else:
		pass

	li = div_other.find("li", class_ = "vcard hq")
	if li:
		hq = li.text.replace("Headquarters","")
		company.location = hq
		# hq = li.text.strip("HeadquartersBank")
		# city = li.find_all("span")[-4].text
		# state = li.find_all("span")[-3].text
		# country = li.find_all("span")[-1].text
		
	else:
		pass
		# city = None
		# state = None
		# country = None

	# company.city = city
	# company.state = state
	# company.country = country

	company_size = div_other.find("li", class_ = "company-size")
	if company_size:
		company.company_size = str(company_size.text.strip("Company Size").replace(" employees", ""))

	founded = div_other.find("li", class_ = "founded")
	if founded:
		company.founded = founded.text.strip("Founded")
	else:
		pass

	also_viewed_block = soup.find('div', class_ = "also-viewed module")
	if also_viewed_block:
		associated_company_names = also_viewed_block.find_all('img')
		associated_company_websites = also_viewed_block.find_all('a')
		also_viewed = {}
		for i, firm in enumerate (associated_company_names):
			also_viewed[firm.get("alt")] = associated_company_websites[i]["href"].replace('?trk=extra_biz_viewers_viewed',"")
	
		company.also_viewed = also_viewed

	else:
		pass

	driver.quit()

	return company


# co = get_company_info('https://www.linkedin.com/company/fugue-inc-')
# print (co.location)

def write_company_info(list_company_urls):
	import csv
	i = 1
	csvFile = open("company_profile.csv", 'a', newline='', encoding="utf8")
	try:
		writer = csv.writer(csvFile)
		for url in list_company_urls:
			company = get_company_info(url)
			writer.writerow( (
				company.linkedin,
				company.name,
				company.specialties,
				company.industry,
				company.website,
				# company.country,
				# company.state,
				# company.city,
				company.location,
				company.company_size,
				company.desc,
				company.founded,
				company.also_viewed
				) )
			print ("{} done for {}".format(i ,company.name))
			time.sleep(2)
			i += 1
	finally:
		csvFile.close()	


if __name__ == "__main__":
	import pandas as pd
	import re
	data = pd.read_csv("article_after_processing5.csv", encoding='iso-8859-1')

	write_company_info(list_company_urls=data.linkedin_link[239:])

