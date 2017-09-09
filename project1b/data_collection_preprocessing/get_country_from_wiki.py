from bs4 import BeautifulSoup
from selenium import webdriver
import re
import csv

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

def get_table(url, filename):
	
	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, "lxml")

	table = soup.find('table', class_ = "wikitable sortable jquery-tablesorter")

	tbody = table.find('tbody')

	trs = tbody.find_all('tr')

	csvFile = open(filename, 'w', newline='', encoding="utf8")
	
	try:
		writer = csv.writer(csvFile)
		writer.writerow(("Ranking", "Country", "GDP"))
		for tr in trs:
			# atag = tr.find('a')
			# if atag:
			# 	print (atag.get("title")) # country
			tdtag = tr.find_all('td')
			if tdtag and not re.search(r'(World|European Union)', tdtag[1].text):
				ranking = tdtag[0].text
				print (ranking)
				country = re.sub(r'\[.+\]', '', tdtag[1].text).strip(' ')
				print (country)
				gdp = tdtag[2].text
				print (gdp)
				writer.writerow( (ranking, country, gdp) )
	finally:
		csvFile.close()

	driver.quit()

	return None


get_table(url, "countries_w_gdp.csv")