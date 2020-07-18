import json
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


def buy_item(driver, config):
    start_time = time.time()

    category = config["category"]
    keyword = config["keyword"]
    color = config["color"]
    size = config["size"]

    driver.get("https://www.supremenewyork.com/shop/all/" + str(category))
    elems = driver.find_elements_by_class_name("inner-article")

    for elem in elems:
        product_name = elem.find_element_by_class_name("product-name")
        product_name_link_text = product_name.find_element_by_class_name("name-link").text.lower()
        if keyword.lower() in product_name_link_text:
            product_style = elem.find_element_by_class_name("product-style")
            product_style_link_text = product_style.find_element_by_class_name("name-link").text.lower()
            if color.lower() in product_style_link_text:
                driver.get(product_style.find_element_by_class_name("name-link").get_attribute("href"))
                break

    sizing = Select(driver.find_element_by_xpath('//*[@id="s"]'))
    sizing.select_by_visible_text(size)

    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    driver.implicitly_wait(0.5)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

    name = driver.find_element_by_xpath('//*[@id="order_billing_name"]')
    name.click()
    name.clear()
    name.send_keys(config["name"])

    email = driver.find_element_by_xpath('//*[@id="order_email"]')
    email.click()
    email.clear()
    email.send_keys(config["email"])

    tel = driver.find_element_by_xpath('//*[@id="order_tel"]')
    tel.click()
    tel.clear()
    tel.send_keys(config["tel"])

    address = driver.find_element_by_xpath('//*[@id="bo"]')
    address.click()
    address.clear()
    address.send_keys(config["address"])

    apt = driver.find_element_by_xpath('//*[@id="oba3"]')
    apt.click()
    apt.clear()
    apt.send_keys(config["apt"])

    zipcode = driver.find_element_by_xpath('//*[@id="order_billing_zip"]')
    zipcode.click()
    zipcode.clear()
    zipcode.send_keys(config["zipcode"])

    card = driver.find_element_by_xpath('//*[@id="rnsnckrn"]')
    card.click()
    card.clear()
    card.send_keys(config["card"])

    expmonth = driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[6]')
    expmonth.click()

    expyear = driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[5]')
    expyear.click()

    cvv = driver.find_element_by_xpath('//*[@id="orcer"]')
    cvv.click()
    cvv.send_keys(config["cvv"])

    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

    print(time.time() - start_time)
    driver.implicitly_wait(1.75)
    # payment = driver.find_element_by_xpath('//*[@id="pay"]/input').send_keys(Keys.RETURN)


def log_into_google(driver):
    driver.get("https://www.accounts.google.com")
    return


    # TODO: write code to log in
    # Navigate to google.come
    # Enter username/password
    # Login


with open("/Users/CreeperFire/Desktop/PythonT/config/supreme.json") as json_file:
    CONFIG = json.load(json_file)


# TODO: use os.CWD
PATH_TO_WEBDRIVER = "/Users/CreeperFire/Desktop/PythonT/chromedriver"
SUPREME_URL = 'https://www.supremenewyork.com/shop/all/' + CONFIG['category']

start = False

# TODO: Minimize driver after launch
driver = webdriver.Chrome(PATH_TO_WEBDRIVER)

try:
# log_into_google(driver)

except Exception as e:
    print("There was an error logging into google.")
    break

while start == False:
    # TODO: Make URL Dynamic
    html = requests.get(SUPREME_URL).text
    soup = BeautifulSoup(html)
    links = []
    for tag in soup.find_all('a', {"class": "name-link"}):
        links.append(tag.text)
    if "Eyelet" in " ".join(l).split():
        buy_item(driver, CONFIG)
        start = True
    time.sleep(0.5)

driver.find_element_by_class