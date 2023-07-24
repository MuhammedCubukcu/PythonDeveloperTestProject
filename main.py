import csv
from selenium.webdriver.common.by import By
import Database.MongoDb as mongo_db
from selenium import webdriver
import time
import numpy as np



# KİTAP YURDU

driver = webdriver.Chrome()
driver.get('https://www.kitapyurdu.com/')

# Select Item
select_search_input = driver.find_element(By.CSS_SELECTOR, 'input#search-input')
select_search_input.send_keys('python')

select_search_btn = driver.find_element(By.CSS_SELECTOR, 'div#search > .button-search.common-sprite')
select_search_btn.click()

select_on_sale = driver.find_element(By.CSS_SELECTOR, 'label:nth-of-type(1) > .custom-checkmark')
select_on_sale.click()

select_next_page = driver.find_element(By.XPATH, f"/html//div[@id='content']/div[@class='grid_9']//div[@class='links']/a[1]")


# Get values and Edit values
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



"""
for value in update_db:
    mongo_db.col_name_kitap_yurdu.insert_one(value)
"""

# kitap sepeti

driver.get('https://www.kitapsepeti.com/')
# Select Item
selected_input_search = driver.find_element(By.CSS_SELECTOR, "input#live-search")
selected_input_search.send_keys('python')

selected_input_search_button = driver.find_element(By.CSS_SELECTOR, "input#searchBtn")
selected_input_search_button.click()

driver.find_element(By.XPATH, "/html//div[@id='filtreStock']/div[@class='row stoktakiler']//label/span/i[1]").click()


# Get values and Edit values
kitap_sepeti_books = []
kitap_sepeti_update_books = []
strs_1 = [f"{x}" for x in range(1,55)]
for i in strs_1:
    selected_books = driver.find_elements(By.XPATH, f"/html//div[@id='katalog']/div[@class='col col-12 p-left']/div/div/div[{i}]/div")
    for value in selected_books:
        kitap_sepeti_books.append(value.text)

for i in range(len(kitap_sepeti_books)):
    value = kitap_sepeti_books[i].split('\n')
    kitap_sepeti_update_books.append(value)

kitap_sepeti_books.clear()

kitap_sepeti_books_dict = {}



for i in range(len(kitap_sepeti_update_books)):
    kitap_sepeti_books_dict = {
        'title' : kitap_sepeti_update_books[i][0],
        'publisher': kitap_sepeti_update_books[i][1],
        'writers': kitap_sepeti_update_books[i][2],
        'price': kitap_sepeti_update_books[i][3]

    }
    kitap_sepeti_books.append(kitap_sepeti_books_dict)



"""
for value in kitap_sepeti_books:
    mongo_db.col_name.insert_one(value)
"""
time.sleep(10)







