from lxml import html
import requests

page = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
text = page.text
print(text)