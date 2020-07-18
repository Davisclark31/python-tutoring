from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def testUserLocationDenver(self):
	self.chrome.get(self.url)
	search = self.chrome.find_element_by_id('user-city')
	self.assertIn('Denver', search.text)

PROXY = "12.345.678.910:8080"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

chrome = webdriver.Chrome("./chromedriver",chrome_options=chrome_options)
chrome.get("https://www.google.com")
chrome.find_element_by_id("user-city")




