from bs4 import BeautifulSoup as bs
import requests
import re
from pprint import pprint

#https://spb.hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=Data+science

# Передаем доменную часть
# все остальное в виде параметров, либо в виде дополнительной составляющей
url = 'https://hh.ru'

params = {'fromSearchLine':'true',
          'st':'searchVacancy',
          'text':'Data science',
          'page': 0 }

# укажем заголовки, User-Agent - не будет лишним
headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

responce = requests.get(url + '/search/vacancy', params = params, headers = headers)

# создаем дом из библиотеки bs, строки с HTMl кодом - responce.text, и модуля из библиотеки html.parser
dom = bs(responce.content, 'html.parser')


# смотрим на сайте и видим тег  class="vacancy-serp-item" - он будет для нас опредиляющим
# с ним составляем список, ищем все заголовки div c классом class="vacancy-serp-item"

block_list = dom.find_all('div', {'class':'vacancy-serp-item'})
# pprint(len(block_list)) - можно проверить если все возвращает какую то длинну, то идём дальше

#создадим пустой список куда закинем данные (Название вакансии, ссылку, и зарплату)

next_link = dom.find('a', {'data-qa':'pager-next'})['href']
vacancy = []
for params['page'] in range(0, params['page']):

    while next_link != None:
        for block in block_list:
            block_data = {} # создаем каждый раз над каждой итерацией отдельный словарь
                        # когда дойдем до конца у нас будет список из 20 словарей по каждой вакансии.

                    #Имя - в имени нам нужно получить текстовую составляющию, по этому в конце getText()
            block_name = block.find('a', {'data-qa':'vacancy-serp__vacancy-title'}).getText()

                    #Ссылка - с полученным э-ом надо обращаться как со словарем, допишем в конце ['href'], и допишем url, для кликабельности.
            block_link = block.find('a', {'data-qa':'vacancy-serp__vacancy-title'})['href']

                    #Зарплата ,достаем сначало блок
            block_salary = block.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

            if not block_salary: # исключаем отсутствие
                salary_min = None
                salary_max = None
                salary_interval = None

            else:
                block_salary=block_salary.getText().replace(u'\xa0', u' ')

                block_salary = re.split(r'\s|-', block_salary)

            if block_salary[0] == 'до':
                salary_min = None
                salary_max = int(block_salary[1]+block_salary[2])
                if block_salary[3] == 'USD':
                    salary_max = salary_max * 70

            elif block_salary[0] == 'от':
                salary_min = int(block_salary[1]+block_salary[2])
                if block_salary[3] == 'USD':
                    salary_min = salary_min * 70
                salary_max = None

            else:
                salary_min = int(block_salary[0]+block_salary[1])
                if block_salary[5] == 'USD':
                    salary_min = salary_min * 70
                salary_max = int(block_salary[3] + block_salary[4])
                if block_salary[5] == 'USD':
                    salary_max = salary_max * 70

                    # сохраняем serial_data
                block_data['name'] = block_name
                block_data['link'] = block_link
                block_data['salary_min'] = salary_min
                block_data['salary_max'] = salary_max
            vacancy.append(block_data) # добавляем наше все в начальный список
        params['page'] += 1
    else:
        break
print(next_link)