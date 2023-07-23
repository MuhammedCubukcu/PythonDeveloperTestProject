import csv
from selenium.webdriver.common.by import By
import Database.MongoDb as mongo_db
from selenium import webdriver
import pandas as pd



kitap_sepeti = 'https://www.kitapsepeti.com/'
driver = webdriver.Firefox()
driver.get(kitap_sepeti)


selected_html_element_input_search = driver.find_element(By.ID, 'live-search')
selected_html_element_input_search.send_keys('python')

# select search button
selected_html_element_search_btn = driver.find_element(By.ID, 'searchBtn')
selected_html_element_search_btn.click()


selected_html_element_on_sale = driver.find_element(By.XPATH, "//label[@for='stock']")
selected_html_element_on_sale.click()


# title array
books_title = []
update_title = []
# select title
selected_html_element_title = driver.find_elements(By.CLASS_NAME, 'detailLink')
# get title value
for title in selected_html_element_title:
    books_title.append(title.text)

# delete empty value title
for title in books_title:
    if title != "":
        update_title.append(title)
update_title.pop(0)


# publisher array
publishers = []
update_publishers = []
# select get title
selected_html_element_publisher = driver.find_elements(By.CLASS_NAME, 'text-title')
for publisher in selected_html_element_publisher:
    publishers.append(publisher.text)


# writers array
writers = []
update_writers = []
# select writers
selected_html_element_writers = driver.find_elements(By.ID, 'productModelText')
for author in selected_html_element_writers:
    writers.append(author.text)
# delete empty value writers
for author in writers:
    if author != "":
        update_writers.append(author)

# Author values were on the agenda at the publisher. I deleted the authors values to clean up the array.
for value in writers:
    publishers.remove(value)

# delete empty value publisher
for publisher in publishers:
    if publisher != "":
        update_publishers.append(publisher)


prices = []
update_prices = []
selected_html_element_price = driver.find_elements(By.CLASS_NAME, 'currentPrice')
for price in selected_html_element_price:
    prices.append(price.text)

for price in prices:
    if price != "":
        update_prices.append(price)

# slicing process
update_title = update_title[0:54]
update_publishers = update_publishers[0:54]
update_writers = update_writers[0:54]
update_prices = update_prices[0:54]



df = pd.DataFrame({"title": update_title, "publisher": update_publishers, "writer": update_writers, "price": update_prices})

df.to_csv('books.csv')

"""
with open('books.csv') as f:
    read = csv.DictReader(f)
    for row in read:
        mongo_db.col_name.insert_one(row)
"""