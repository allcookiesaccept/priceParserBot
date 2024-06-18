from abc import ABC, abstractmethod
import requests
from config.logger import logger
from selenium import webdriver


class Parser(ABC):
    def __init__(self):
        self.headers = {"User-Agent":
                            "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; "
                            "+http://www.google.com/bot.html) Chrome/126.0.0.0 Safari/537.36"}

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--window-size=1920,1080")
        # self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def __call__(self, url):

        page_src = self.get_page_html(url)
        soup = self.create_soup(page_src)
        products = self.extract_products_from_soup(soup)

        self.driver.quit()

        return products


    def request_url(self, url):
        self.driver.get(url)
        status_code = self.check_status_code()

        if status_code != 200:
            return None

        return self.driver.page_source


    def check_status_code(self):
        response_code = self.driver.execute_script("""
            var http = new XMLHttpRequest();
            http.open('GET', window.location.href, false);
            http.send(null);
            return http.status;
            """)
        logger.info(f"Response code: {response_code}")
        return response_code

    def get_page_html(self, url):
        ...


    def create_soup(self, page_src):
        ...


    def extract_products_from_soup(self, soup):
        ...

