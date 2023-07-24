import csv
from selenium.webdriver.common.by import By
import Database.MongoDb as mongo_db
from selenium import webdriver
import pandas as pd
import time
import numpy as np



# KİTAP YURDU


driver = webdriver.Chrome()
driver.get('https://www.kitapyurdu.com/')

select_search_input = driver.find_element(By.CSS_SELECTOR, 'input#search-input')
select_search_input.send_keys('python')

select_search_btn = driver.find_element(By.CSS_SELECTOR, 'div#search > .button-search.common-sprite')
select_search_btn.click()

select_on_sale = driver.find_element(By.CSS_SELECTOR, 'label:nth-of-type(1) > .custom-checkmark')
select_on_sale.click()

select_next_page = driver.find_element(By.XPATH, f"/html//div[@id='content']/div[@class='grid_9']//div[@class='links']/a[1]")



books = []
update_books = []
slice_books = []
strs = [f"{x}" for x in range(1,28)]

for i in strs:
    select_books_title = driver.find_elements(By.XPATH, f"//div[@id='product-table']/div[{i}]//a/span")
    for value in select_books_title:
        books.append(value.text)

for value in books:
    if value != "":
        update_books.append(value)


prices_dict = {}
prices = []
for i in strs:
    select_price = driver.find_elements(By.XPATH, f"/html//div[@id='product-table']/div[{i}]//div[@class='price']/div[2]/span[@class='value']")
    for value in select_price:
        prices_dict = {
            "price" : value.text
        }
        prices.append(prices_dict)

books.clear()

book = np.array(update_books)
books = np.array_split(book,21)

db = {}
update_db = []

for i in range(20):
    db = {
        "title": books[i][0],
        "publisher": books[i][1],
        "writers": books[i][2]

    }
    update_db.append(db)



for i in range(20):
    update_db[i].update(prices[i])

print(update_db)

"""
for value in update_db:
    mongo_db.col_name_kitap_yurdu.insert_one(value)
"""

# Kitap sepeti

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


with open('books.csv') as f:
    read = csv.DictReader(f)
    for row in read:
        mongo_db.col_name.insert_one(row)



time.sleep(10)







