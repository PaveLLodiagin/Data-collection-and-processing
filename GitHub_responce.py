# 1. Посмотреть документацию к API GitHub,
# 2. Разобраться как вывести список репозиториев для конкретного пользователя,
# 3. Сохранить JSON-вывод в файле *.json.

import requests
import json
from pprint import pprint

def repo_list(url, user):
    "Функция получает список репозиториев и записывает их названия в JSON файл"
    responce = requests.get(f'{url}/users/{user}/repos')

    # Далее создадим пустой список, куда будем добавлять название репозитория
    repository_list = []
    for i in responce.json():
        repository_list.append(i['name'])
        print(i['name']) #Выводим в терминал только название репозитория

    with open('repository_name_list.json', 'w') as file:
        json.dump(repository_list, file)

    with open('full_responce.json', 'w') as file:
        json.dump(responce.json(), file)

repo_list('http://api.github.com', 'PavelLodiagin')  