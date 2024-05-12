import requests
import random
from fake_headers import Headers
from task_2 import logger

LOGFILE = 'main_3.log'


@logger(LOGFILE)
def gen_headers():
    browser = random.choice(['chrome', 'firefox', 'opera'])
    os = random.choice(['win', 'mac', 'lin'])
    headers = Headers(browser=browser, os=os)
    return headers.generate()


# gen_headers()

list_urls = ['yandex.ru', 'mail.ru', 'habr.com', 'stackoverflow.com']


# response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=gen_headers())

@logger(LOGFILE)
def test_request(url):
    response = requests.get(f'https://{url}/', headers=gen_headers())
    print(response.status_code)
    return f'STATUS CODE - {response.status_code}'


for url in list_urls:
    test_request(url)
