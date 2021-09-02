from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['parsLenta']
news = db.news_List
url = 'https://lenta.ru'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

response = requests.get(url, headers=headers )

dom = html.fromstring(response.text)

items = dom.xpath("//time[@class='g-time']")

for item in items:
    info = item.xpath("./../text()")
    link = item.xpath("./../@href")
    time = item.xpath('./text()')

    news.insert_one(
        {'source': 'Lenta.ru', 'time': time,'link': link, 'info':str(info).replace('\\xa0' or '\xa0',' ')}
                )

for doc in news.find():
    pprint(doc)
