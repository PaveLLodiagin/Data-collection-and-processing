from bs4 import BeautifulSoup as bs
import requests
import re
from pprint import pprint

url = 'https://hh.ru'

params = {'fromSearchLine':'true',
          'st':'searchVacancy',
          'text':'Data science',
          'from' : 'suggest_post',
          'page':'0'}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

responce = requests.get(url + '/search/vacancy', params=params, headers=headers)

dom = bs(responce.content, 'html.parser')

next_link = dom.find('a', {'data-qa':'pager-next'})['href']

i = 0
while next_link != None:
    if next_link == None:
        print('end')
    else:
        print(params['page'])
        print(next_link)
    i +=1
    params['page'] = str(i)
next_link = dom.find('a', {'data-qa': 'pager-next'}).getText()