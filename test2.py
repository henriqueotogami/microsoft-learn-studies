import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify ())

title = soup.find(id="productTitle").get_text()
print(title)
