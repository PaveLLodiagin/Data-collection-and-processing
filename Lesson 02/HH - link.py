from bs4 import BeautifulSoup as bs
import requests
import re
from pprint import pprint

url = 'https://hh.ru'

params = {'fromSearchLine':'true',
          'st':'searchVacancy',
          'text':'Data science',
          'from' : 'suggest_post',
          'page': 3 }

headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

responce = requests.get(url + '/search/vacancy', params = params, headers = headers)

dom = bs(responce.content, 'html.parser')

next_link = dom.find('a', {'data-qa':'pager-next'})['href']
print(params)