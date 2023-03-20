import numpy as np
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import itertools

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome("C:\\Games\\chromedriver.exe" , options=chrome_options)
# Open URL
driver.get("https://tiki.vn/giay-dep-nu/c1703")
sleep(random.randint(5,10))

# ================================ GET link/title
# elems = driver.find_elements(By.CLASS_NAME , "product-item")
# titles = [elem.text for elem in elems]
# links = [elem.get_attribute('href') for elem in elems]
# elems_price = driver.find_elements(By.CSS_SELECTOR , ".price-discount__price")
# len(elems_price)
# price = [elem_price.text for elem_price in elems_price]
# elems_discount_rates = driver.find_elements(By.CSS_SELECTOR , ".price-discount__discount")

# # discount_rate = [elem.text if elem else '' for elem in elems_discount_rates]

# data = zip(links, elems_price, elems_discount_rates)

# Sử dụng list comprehension để trích xuất thông tin về giá và tỷ lệ giảm giá
# và loại bỏ các cặp giá trị thừa
# price = [elem_price.text for _, elem_price, _ in data]

# discount_rate = [elem_rate.text if elem_rate else '' for _, _, elem_rate in data]
# discount_rate = []
# for elem_discount_rate in elems_discount_rates:
#     if elem_discount_rate:
#         discount_rate.append(elem_discount_rate.text)
#     else:
#         discount_rate.append(None)
# Tạo DataFrame từ thông tin về liên kết, giá và tỷ lệ giảm giá
# df1 = pd.DataFrame({'link_item': links, 'price': price, 'discount_rate': discount_rate})
# df1 = pd.DataFrame({'discount_rate': discount_rate})

# product_id = []
# for link in links:
#     product_id.append({'link':link})

# print('\n'.join(title))
# df = pd.DataFrame(product_id)
# df1.to_csv('product_link_discount.csv', index=False)
# x_path_next_page = '/html/body/div[1]/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ul/li[9]/a/img'
# x_path_next_page.click()
# sleep(random.randint(1,3))
count = 1
links = []
prices = []
for i in range(2, 49):
    # Truy cập trang Tiki có chỉ số i
    driver.get('https://tiki.vn/giay-the-thao-nu/c27604?sort=default&page=' + str(i))
    sleep(random.randint(1,3))
    elems = driver.find_elements(By.CLASS_NAME , "product-item")
    for elem in elems: 
        link  = elem.get_attribute('href')
        links.append(link)         
    elems_prices = driver.find_elements(By.CSS_SELECTOR , ".price-discount__price")
    for elem_price in elems_prices:
        price = elem_price.text
        prices.append(elem_price)
df1 = pd.DataFrame({'link_item': links, 'price': prices} )
df1.to_csv('product_link_giaydep2.csv', index=True)

# while True:
#     try:
#         print("Crawl Page " + str(count))
#         elems = driver.find_elements(By.CLASS_NAME , "product-item")
#         links = [elem.get_attribute('href') for elem in elems]+ links
        
#         elems_price = driver.find_elements(By.CSS_SELECTOR , ".price-discount__price")
        
#         prices = [elem_price.text for elem_price in elems_price] +prices
#         x_path_next_page = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ul/li[9]/a/img")
#         # x_path_next_page = '/html/body/div[1]/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ul/li[9]/a'
#         x_path_next_page.click()
        # sleep(random.randint(1,3))
#         # try:
#         #     close_btn = driver.find_element("xpath", "/html/body/div[7]/div[2]/div") 
#         #     close_btn.click()
#         #     print("Clicked on button exit!")
#         #     sleep(random.randint(1,3))
#         # except ElementNotInteractableException:
#         #     continue
#         # sleep(random.randint(1,3))
#         count += 1
#     except ElementNotInteractableException:
#         print("Element Not Interactable Exception!")
#         break




