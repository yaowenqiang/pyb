from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
	soupe = BeautifulSoup(html_file, 'lxml')

# print(soupe.prettify())

# match = soupe.title.text

# match = soupe.find('div', class_='footer')

match = soupe.find_all('div', class_='footer')
print(match)

article = soupe.find('div', class_='article')
print(article)

headline = article.h2.a.text
print(headline)

# python -m pip install beautifulsoup4
# python -m pip install lxml
# python -m pip install requests


# source = requests.get('http://coreyms.como').text
source = requests.get('http://localhost').text

print(source)

soap2 = BeautifulSoup(source, 'lxml')
print(soap2.prettify())