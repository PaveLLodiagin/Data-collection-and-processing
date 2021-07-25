# Возьмите API вконтакте (https://vk.com/dev/first_guide).
# Сделайте запрос, чтобы получить список всех сообществ на которые вы подписаны.
# https://api.vk.com/method/METHOD?PARAMS&access_token=TOKEN&v=V
import requests
import json
from pprint import pprint
# https://api.vk.com/method/groups.get
chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
user_params = {'PARAMS': 'PARAMS',
               'access_token' : 'ACCESS_TOKEN',
               'expires_in': '0',
               'user_id': 'USER_ID',
               'email': 'EMAIL',
               'v':'5.131'}
#access_token=a674e7fb796f421b3773872656ba7129e512307805f7381560209d1c20cd89ec866989909fed21cd80f02&expires_in=0&user_id=173843141&email=wonderwaffe23@gmail.com

url = 'https://api.vk.com/method/groups.get'

response = requests.get(url, params=user_params)
j_data = response.json()
pprint(j_data)