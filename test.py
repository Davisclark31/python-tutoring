import json
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.keys import Keys

start_time = time.time()

with open("/Users/CreeperFire/Desktop/PythonT/config/supreme.json") as json_file:
    CONFIG = json.load(json_file)

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--disable-extensions')
#chrome_options.add_argument('--profile-directory=Default')
#chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--disable-plugins-discovery");
#chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("/Users/CreeperFire/Desktop/PythonT/chromedriver")#,chrome_options=chrome_options)

category = CONFIG["category"]
keyword = CONFIG["keyword"]
color = CONFIG["color"]
size = CONFIG["size"]

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
name.send_keys(CONFIG["name"])

email = driver.find_element_by_xpath('//*[@id="order_email"]')
email.click()
email.clear()
email.send_keys(CONFIG["email"])

tel = driver.find_element_by_xpath('//*[@id="order_tel"]')
tel.click()
tel.clear()
tel.send_keys(CONFIG["tel"])

address = driver.find_element_by_xpath('//*[@id="bo"]')
address.click()
address.clear()
address.send_keys(CONFIG["address"])

apt = driver.find_element_by_xpath('//*[@id="oba3"]')
apt.click()
apt.clear()
apt.send_keys(CONFIG["apt"])

zipcode = driver.find_element_by_xpath('//*[@id="order_billing_zip"]')
zipcode.click()
zipcode.clear()
zipcode.send_keys(CONFIG["zipcode"])

card = driver.find_element_by_xpath('//*[@id="rnsnckrn"]')
card.click()
card.clear()
card.send_keys(CONFIG["card"])

expmonth = driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[6]')
expmonth.click()

expyear = driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[5]')
expyear.click()

cvv = driver.find_element_by_xpath('//*[@id="orcer"]')
cvv.click()
cvv.send_keys(CONFIG["cvv"])

driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

print(time.time() - start_time)
driver.implicitly_wait(1.75)
#payment = driver.find_element_by_xpath('//*[@id="pay"]/input').send_keys(Keys.RETURN)