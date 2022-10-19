from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import json

def writeProducts(config):
    with open(config['path'] + config['filename'], 'a', newline='') as csvfile:
        url = "https://" + config['url'][config['url'].find("gradusi.net") + 0:]

        products = BeautifulSoup(urlopen(url), features="html.parser").findAll(class_='products-of-the-day__item')

        writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Price'], delimiter=";")

        if (csvfile.tell() == 0):
            writer.writeheader()

        for i in range(len(products)):
            name = products[i].findChildren(class_='product-of-the-day__name')[0].get_text('\n', strip='True')
            price = products[i].findChildren(class_='price_default')[0].get_text('\n', strip='True').strip('₽')
            writer.writerow({'Name': name, 'Price': price})

def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    writeProducts(config)

if __name__ == "__main__":
    main()
