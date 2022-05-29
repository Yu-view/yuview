from lib2to3.pgen2 import driver
from multiprocessing.spawn import _main
from tokenize import String
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def searchProduct(query: String):
        query = query.replace(' ', '+')
        url = f"https://shopee.sg/search?keyword={query}"
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "shopee-search-item-result__item")))
        return searchListing(driver)

def searchListing(driver: webdriver):
        driver.execute_script("""
        var scroll = document.body.scrollHeight / 10;
        var i = 0;
        function scrollit(i) {
           window.scrollBy({top: scroll, left: 0, behavior: 'smooth'});
           i++;
           if (i < 10) {
            setTimeout(scrollit, 500, i);
            }
        }
        scrollit(i);
        """)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for item in soup.find_all('a', {'data-sqe': 'link'}):
            print(item.get('href'))

searchProduct("keyboard")