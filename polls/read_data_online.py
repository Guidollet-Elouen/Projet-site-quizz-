from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "https://fr.wikipedia.org/wiki/Volcan"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())