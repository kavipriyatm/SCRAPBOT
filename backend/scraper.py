from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests

CHROMEDRIVER_PATH = "D:/chromedriver_win32/chromedriver.exe"

def scrape_static(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return {"title": soup.title.string, "content": soup.get_text()}
    except Exception as e:
        return {"error": str(e)}

def scrape_dynamic(url):
    try:
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        content = driver.page_source
        driver.quit()
        soup = BeautifulSoup(content, 'html.parser')
        return {"title": soup.title.string, "content": soup.get_text()}
    except Exception as e:
        return {"error": str(e)}