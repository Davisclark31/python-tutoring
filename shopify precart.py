import json
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

path = "/Users/CreeperFire/Desktop/PythonT/chromedriver"

driver = webdriver.Chrome(path)
#def getToken:
driver.get('https://kith.com/collections/kith-summer-2020/products/kh1257-109')
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="globale_popup"]/div/div/div/div/div[5]/a').click()
driver.find_element_by_xpath('//*[@id="gle_selectedCountry"]').send_keys("United States")
driver.find_element_by_xpath('//*[@id="globale_csc_popup"]/div/div/div/div/div[4]/input[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="shopify-section-product"]/section[1]/div[4]/form/button').click()
time.sleep(2)
driver.get('https://kith.com/checkout')
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_country"]/option[1]').click()
driver.find_element_by_xpath('//*[@id="checkout_email"]').click()
driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys("davisc3126@gmail.com")
driver.find_element_by_xpath('//*[@id="checkout_buyer_accepts_marketing"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys("yes")
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys("yes")
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys("1770 Front Street")
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address2"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address2"]').send_keys("#652")
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys("Lynden")
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]/option[57]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys("98264")
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').click()
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys("7789992299")
driver.find_element_by_xpath('//*[@id="continue_button"]').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="continue_button"]').click()
url = driver.current_url
driver.get("https://www.kith.com/cart/change?line=1&quantity=0")
keyword = str(input("enter"))
keywordurl = "https://kith.com/pages/search-results-page?q="
keywords = keyword.split(',')
g = 0
for i in keywords:
    if g >= 1:
        keywordurl += "+"
    keywordurl += i
    g += 1
driver.get(keywordurl)

pds = {}
products_list = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div[1]/div[3]/div/ul')
products_list = products_list.find_elements_by_tag_name('li')
for list_items in products_list:
    link = list_items.find_element_by_tag_name('a').get_attribute('href')
    text = list_items.find_element_by_class_name('snize-title').text
    pds[text]=link






"""


>>get_token()
>> www.kith.com/2130-9uqpwoje1230122123/

driver.get_url(www.kith.com)

def get_token(driver):
	driver.get_page()
	form code
	url = current.url()
	return url



get_token(driver)
"""