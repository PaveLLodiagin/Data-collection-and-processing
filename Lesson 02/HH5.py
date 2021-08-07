from bs4 import BeautifulSoup as bs
import requests
import re
from pprint import pprint

url = 'https://hh.ru'

params = {'fromSearchLine':'true',
          'st':'searchVacancy',
          'text':'Data science',
          'page': ''}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

responce = requests.get(url + '/search/vacancy', params = params, headers = headers)

dom = bs(responce.content, 'html.parser')

block_list = dom.find_all('div', {'class': 'vacancy-serp-item'})
button = dom.find('a', {'data-qa': 'pager-next'})
vacancy = []
for block in block_list:
    block_data = {}
    params['page'] = -1
    if button != button:
        break
    else:
        next_link = dom.find('a', {'data-qa': 'pager-next'})['href']
        responce = requests.get(url + next_link, headers=headers)
        dom = bs(responce.content, 'html.parser')
        params['page'] += 1
        print(url + next_link)

        block_name = block.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).getText()

        block_link = block.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})['href']

        block_salary = block.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

        if not block_salary:
            salary_min = None
            salary_max = None
            salary_interval = None

        else:
            block_salary = block_salary.getText().replace(u'[–,\xa0]', u' ')
            block_salary = re.split(r'\s|-', block_salary)

            if block_salary[0] == 'до':
                salary_min = None
                salary_max = int(block_salary[1] + block_salary[2])

            elif block_salary[0] == 'от':
                salary_min = int(block_salary[1] + block_salary[2])
                salary_max = None

            else:
                salary_min = int(block_salary[0] + block_salary[1])
                salary_max = int(block_salary[3] + block_salary[4])

        block_data['name'] = block_name
        block_data['link'] = block_link
        block_data['salary_min'] = salary_min
        block_data['salary_max'] = salary_max
        vacancy.append(block_data)
    pprint(vacancy)

#1,2,3