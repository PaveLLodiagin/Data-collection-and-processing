from lxml import html
import requests
from pprint import pprint
import re
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['parsYandex']
news = db.news_List

url = 'https://yandex.ru/news/'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

response = requests.get(url, headers=headers )

dom = html.fromstring(response.text)

items = dom.xpath("//article[contains(@class,'mg-card mg-card_flexible-')]")

for item in items:

    info  = str(item.xpath(".//h2[@class='mg-card__title']/text()")).replace('\\xa0',' ')
    source = item.xpath(".//a[@class='mg-card__source-link']/text()")
    link = item.xpath(".//a[@class='mg-card__link']/@href")
    data = item.xpath(".//span[@class='mg-card-source__time']/text()")

news.insert_one(
        {'source': source, 'data': data,'link': link, 'info':info}
                )

for doc in news.find():
    pprint(doc)
