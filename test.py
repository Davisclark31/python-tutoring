from selenium import webdriver


category = str(input("Enter category: "))
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.supremenewyork.com/shop/all/"+str(category))
elems = driver.find_elements_by_class_name("inner-article")

#for i in elems:
#    print(i.find_elements_by_tag_name("a"))

#driver.close()

for elem in elems:
    if "Eyelet" in elem.find_element_by_class_name("product-name") in elem.find_element_by_class_name("name-link") and "Red" in elem.find_element_by_class_name("product-style") in elem.find_element_by_class_name("name-link"):
        print(elem.get_attribute("href"))


#       driver.get(elem.get_attribute("href"))
#    driver.get("https://www.supremenewyork.com/shop/all/sweatshirts")

#1: go to specified page (category)
#2: get all links on page
#3: filter only category links
#4: filter to specified product (product-name)
# #5: filter to specified colour (product-style)
#6: open final list of links