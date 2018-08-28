import requests
import lxml.html
import random


class Parser:

    def __init__(self, url):
        self.url = url

    def get_tree(self):
        # метод для парсинга страницы
        try:
            res = requests.get(self.url)
            tree = lxml.html.fromstring(res.text)
        except requests.ConnectionError as e:
            print('error', e)
            tree = ''
        return tree


url = 'http://news.bigmir.net/'
parser = Parser(url)
html = parser.get_tree()
path = '//*[@id="last-news-feed"]/div/div/ul/li/div/a/@href'
link_list = html.xpath(path)


def return_random_link(link_list):
    return 'http://news.bigmir.net' + link_list[random.randint(0, len(link_list))]


if __name__ == '__main__':
    print(return_random_link(link_list))
