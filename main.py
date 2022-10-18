from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

with open('products.csv', 'a', newline='') as csvfile:
    products = BeautifulSoup(urlopen(url), features="html.parser").findAll(class_='products-of-the-day__item')

    writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Price'], delimiter=";")
    writer.writeheader()

    for i in range(len(products)):
        name = products[i].findChildren(class_='product-of-the-day__name')[0].get_text('\n', strip='True')
        price = products[i].findChildren(class_='price_default')[0].get_text('\n', strip='True').strip('₽')
        writer.writerow({'Name': name, 'Price': price})

