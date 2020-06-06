from selenium import webdriver


category = str(input("Enter category: "))
keyword = str(input("Enter keyword: "))
color = str(input("Enter color: "))

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.supremenewyork.com/shop/all/"+str(category))
elems = driver.find_elements_by_class_name("inner-article")

links = []
for elem in elems:
    product_name = elem.find_element_by_class_name("product-name")
    product_name_link_text = product_name.find_element_by_class_name("name-link").text.lower()
    if keyword.lower() in product_name_link_text:
        product_style = elem.find_element_by_class_name("product-style")
        product_style_link_text = product_style.find_element_by_class_name("name-link").text.lower()
        if color.lower() in product_style_link_text:
            links.append(product_style.find_element_by_class_name("name-link").get_attribute("href"))

for link in links:
    driver.get(link)
