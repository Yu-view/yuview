import typing
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions();
options.add_argument('headless')
options.add_argument('disable-notifcations')
options.add_argument('disable-infobars')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def searchProduct(query: str):
        query = query.replace(' ', '+')
        url = f"https://shopee.sg/search?keyword={query}"
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "shopee-search-item-result__item")))
        return searchListing(driver)

def searchListing(driver: webdriver):
        driver.execute_script("""
        window.scrollBy({top: document.body.scrollHeight, left: 0, behavior: 'smooth'});
        """)
        time.sleep(0.5)
        listings = driver.find_elements(by=By.XPATH, value="//a[@data-sqe='link']")
        print(len(listings))
#        for listing in listings:


        """
        soup = BeautifulSoup(driver.page_source, "html.parser")
        i = 1
        for item in soup.find_all('a', {'data-sqe': 'link'}):
            print(str(i) + ": " + item.get('href'))
            i+=1
        """

searchProduct("keyboard")