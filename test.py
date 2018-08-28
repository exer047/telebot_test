import requests
import lxml.html

url = 'https://woman-gu.ru/dlya-prazdnika/pozhelaniya/365-predskazanij-spisok/'


class Parser:

    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout

    def get_tree(self):
        # метод для парсинга страницы
        try:
            res = requests.get(self.url)
            tree = lxml.html.fromstring(res.text)
        except requests.ConnectionError as e:
            print('error', e)
            tree = ''
        return tree


parser = Parser(url, 5)
path = '//*[@id="content"]/article/div[1]/div[2]/ol/li/text()'
tree = parser.get_tree()
lalala = tree.xpath(path)

with open('predictions.txt', 'w') as file:
    for item in lalala:
        file.write("{}\n".format(item))
file.close()
