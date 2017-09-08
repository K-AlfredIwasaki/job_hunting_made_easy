# big container: <div class="tab-panel active" id="relevant">
# small container:<li class="river-block"> 

# article title and link: <h2 class="post-title st-result-title"> => <a href> + text
# summary: <p class="excerpt">


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv

class Article():
	"""docstring for article"""
	def __init__(self):
		self.title = ""
		self.link = ""
		self.excerpt = ""

def get_items(url):
	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')
	# print(soup.prettify())

	div = soup.find('div', class_ = "tab-panel active")

	# print (div.prettify())

	article_list = []

	for li in div.find_all('li', class_ = "river-block"):
		
		# create an object
		new_article = Article()

		# iterate each article to get the items to collect

		h2 = li.find('h2', class_ = "post-title st-result-title")
		a = h2.find('a')

		# get an artitle title and a link
		new_article.title = a.text
		if new_article.title:
			print (a.text)
			new_article.link = a['href']
			print (a['href'])

			# get excerpt
			p = li.find('p', class_ = "excerpt")

			new_article.excerpt = p.text.strip(" 					").replace(" 					Read More","")
			print (new_article.excerpt)

			article_list.append(new_article)
		else:
			pass


	driver.quit()

	return article_list


def write_records(article_list):
	csvFile = open("article.csv", 'a', newline='', encoding="utf8")
	try:
		writer = csv.writer(csvFile)
		writer.writerow(('title', 'link', 'excerpt'))
		for article in article_list:
			writer.writerow( (article.title, article.link, article.excerpt) )

	finally:
		csvFile.close()

for i in range(1, 100):

	num = i
	url = "https://techcrunch.com/search/raises+Series+C#stq=raises Series+C&stp={}".format(num)

	# write records for each page
	write_records( get_items(url) )






