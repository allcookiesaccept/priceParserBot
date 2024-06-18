import requests.models
from bs4 import BeautifulSoup
from .parser import Parser
from selenium import webdriver

class Vek21Parser(Parser):

    def __init__(self):
        super().__init__()

    def __call__(self, url):
        page_src = self.request_url(url)
        soup = self.create_soup(page_src)
        products = self.extract_products_from_soup(soup)

        return products


    def create_soup(self, page_src):
        soup = BeautifulSoup(page_src, 'html.parser')
        return soup

    def extract_products_from_soup(self, soup):

        data = []

        products = soup.find_all('div', attrs={"class": "ListingProduct_product__WBPsd"})

        for product in products:

            name_tag = product.find('p', attrs={"class":'CardInfo_info__cUeVj ListingProduct_fullNameContainer__dr86y'})
            name = name_tag.text.strip() if name_tag else "Не удалось спарсить название"

            price_tag = product.find('p', attrs={"class": "CardPrice_currentPrice__EU_7r"})
            price = price_tag.text.strip() if price_tag else "Нет в наличии"

            old_price_tag = product.find('p', attrs={"class": "CardPrice_oldPrice__dc0rb"})
            old_price = old_price_tag.text.strip() if old_price_tag else "--"

            sales_tag = product.find('span', attrs={"class": "CardDiscountLabel_discount__IpIhG CardDiscountLabel_bottom-left__gHopN ListingProduct_discountLabel__fgbaF Text-module__text Text-module__body"})
            sales = sales_tag.text if sales_tag else '0%'

            action_tag = product.find('div', attrs={"class": "ListingProduct_discountTypes__RlKDP"})

            if action_tag:
                actions = action_tag.find_all('div')
                actions_string = [action.text for action in actions]

            link = name_tag.find('a')
            product_url = link.get('href')

            data.append([name, price, old_price, sales, actions_string, product_url])

        return data
