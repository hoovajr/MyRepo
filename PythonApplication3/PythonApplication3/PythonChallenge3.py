import re
from lxml import html
import requests

page = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
text = page.text

print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text)))
