from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import json


def writeProducts(config):
    #создаётся или дописывается файл
    with open(config['path'] + config['filename'], 'a', newline='') as csvfile:
        #изменение url для избежания редиректа
        url = "https://" + config['url'][config['url'].find("gradusi.net") + 0:]
        #парсинг html-страницы
        products = BeautifulSoup(urlopen(url), features="html.parser").findAll(class_='products-of-the-day__item')

        writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Price'], delimiter=";")
        #проверка на существование файла, и если его нет, то в файле запишутся названия колонок
        if (csvfile.tell() == 0):
            writer.writeheader()
        #запись названий и цен товаров дня в файл
        for i in range(len(products)):
            name = products[i].findChildren(class_='product-of-the-day__name')[0].get_text('\n', strip='True')
            price = products[i].findChildren(class_='price_default')[0].get_text('\n', strip='True').strip('₽')
            writer.writerow({'Name': name, 'Price': price})

#открытие конфига и передача его параметров в функцию writeProducts()
def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    writeProducts(config)

if __name__ == "__main__":
    main()
