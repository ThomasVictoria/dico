from lxml import html
from lxml import etree
import requests
import string
from data import Data

class LarousseParser():
	alpha = list(string.ascii_lowercase)

	def __init__(self):
		# Loop through letters
		for letter in self.alpha:
			self.parse_pages('http://www.larousse.fr/index/dictionnaires/francais/'+letter, letter)

	def parse_pages(self, url, letter):
		exist = True
		number = 1
		while exist == True:
			page = requests.get(url+str(number))
			# Check if page index exist by checking the error div
			tree = html.fromstring(page.content).xpath('//h1[@class="icon-warning-sign"]')
			if len(tree) == 0:
				self.parse_word(page, letter)
			else:
				exist = False
			number = number + 1

	def parse_word(self, page, letter):
		menu = html.fromstring(page.content).xpath('//section[@class="content olf"]/ul/li/a')
		for elem in menu:
			url = elem.attrib['href']
			self.word_page(url, letter)

	def word_page(self, url, letter):
		page = requests.get('http://www.larousse.fr/'+url)
		word = html.fromstring(page.content).xpath('//h2[@class="AdresseDefinition"]/text()')
		definitions = html.fromstring(page.content).xpath('//ul[@class="Definitions"]/li')
		print(word[0])
		Data(word[0], letter, definitions)

LarousseParser()