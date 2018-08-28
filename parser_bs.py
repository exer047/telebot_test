# сменил ментод с BeautifulSoup на lxml.html потому что не смог удобно вытащить ссылку из Тега
# парсер нужен что бы добавить в бот функцию сбрасывания случайной новости
import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuVnJHZ0pWUVNnQVAB?hl=uk&gl=UA&ceid=UA%3Auk'


# наша ссылка с гугла


def get_page(url):
    # скачиваем страницу
    try:
        res = requests.get(url)
        html = res.text
    except requests.ConnectionError as e:
        print('error', e)
        html = ''
    return html


def get_tags(html):
    # создаем список тегов в которых содержатся ссылки на новость
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a', 'VDXfz', 'href')
    print(tags)
    return tags


if __name__ == '__main__':
    page = get_page(url)
    my_list = get_tags(page)
