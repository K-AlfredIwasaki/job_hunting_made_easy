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
		self.specialities = ""
		self.industry = ""
		self.website = ""
		self.country = ""
		self.state = ""
		self.city = ""
		self.company_size = ""
		self.desc = ""
		self.founded = ""
		self.also_viewed = {}


url = 'https://www.linkedin.com/company/bank_bazaar'

def get_company_info(url):

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	company = Company()

	company.linkedin = url

	header = soup.find('div', class_ = "top-bar with-wide-image with-nav big-logo")

	company.name = header.find('h1', class_ = "name").text
	print (company.name)

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
	print (specialty.text)
	if specialty:
		print(True)
		specialty = specialty.text.replace("Specialties","")
		print (specialty)
	else:
		pass
	company.specialities = specialty
	print (company.specialities)

	industry = div_other.find("li", class_ = "industry").text.replace("Industry","")
	company.industry = industry

	website = div_other.find("li", class_ = "website").text.strip("Website")
	company.website = website

	li = div_other.find("li", class_ = "vcard hq")
	if li:
		hq = li.text.strip("HeadquartersBank")
		city = li.find_all("span")[-4].text
		state = li.find_all("span")[-3].text
		country = li.find_all("span")[-1].text
		
	else:
		hq = None
		city = None
		state = None
		country = None

	company.city = city
	company.state = state
	company.country = country
	company_size = div_other.find("li", class_ = "company-size").text.strip("Company Size").replace(" employees", "")
	company.company_size = str(company_size)

	founded = div_other.find("li", class_ = "founded").text.strip("Founded")
	company.founded = founded

	also_viewed_block = soup.find('div', class_ = "also-viewed module")
	associated_company_names = also_viewed_block.find_all('img')
	associated_company_websites = also_viewed_block.find_all('a')
	also_viewed = {}
	for i, firm in enumerate (associated_company_names):
		also_viewed[firm.get("alt")] = associated_company_websites[i]["href"].replace('?trk=extra_biz_viewers_viewed',"")
		
	company.also_viewed = also_viewed

	driver.quit()

	print ("done scraping for {}".format(company.name))

	return company

# get_company_info('https://www.linkedin.com/company/hourlynerd')

def write_company_info(list_company_urls):
	import csv
	csvFile = open("company_profile.csv", 'a', newline='', encoding="utf8")
	try:
		writer = csv.writer(csvFile)
		for url in list_company_urls:
			company = get_company_info(url)
			writer.writerow( (
				company.linkedin,
				company.name,
				company.specialities,
				company.industry,
				company.website,
				company.country,
				company.state,
				company.city,
				company.company_size,
				company.desc,
				company.founded,
				company.also_viewed
				) )
			time.sleep(2)
	finally:
		csvFile.close()	


list_company_urls = [
# 'https://www.linkedin.com/company/cloudphysics',
# 'https://www.linkedin.com/company/docplanner',
# 'https://www.linkedin.com/company/cb-insights',
# 'https://www.linkedin.com/company/quiqup',
# 'https://www.linkedin.com/company/instart-logic',
# 'https://www.linkedin.com/company/tivo',
'https://www.linkedin.com/company/farmdrop-ltd'
]

write_company_info(list_company_urls=list_company_urls)

 