import numpy as np
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import itertools

df_link = pd.read_csv('product_link_chamsocnhacua.csv')
p_link = df_link['link_item'].to_list()
a = p_link[0]
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome("C:\\Games\\chromedriver.exe" , options=chrome_options)

driver.get("https://tiki.vn/tui-vien-giat-xa-da-nang-4-trong-1-ka-universal-5-vien-tui-p179512961.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.195087_Y.1777414_Z.3502554_CN.Product-Ads-08%2F11%2F2022&itm_medium=CPC&itm_source=tiki-ads&spid=179512962")
sleep(random.randint(1,3))
prices_list = [] 
discount_list = []
review_count_list = []
quantity_sold_list = []
prices = driver.find_elements(By.CLASS_NAME , "product-price__current-price")
prices_list = [prices] + prices_list
discounts = driver.find_elements(By.CLASS_NAME , "product-price__discount-rate")
discount_list = [discount.text for discount in discounts] + discount_list

review_counts = driver.find_elements(By.CLASS_NAME , "number")
review_count_list = [int(review_count.text.split()[1]) for review_count in review_counts]+review_count_list
quantity_sold = driver.find_element(By.CSS_SELECTOR, 'div[data-view-id="pdp_quantity_sold"].styles__StyledQuantitySold-sc-1u1gph7-2.exWbxD')
sold_number = quantity_sold.get_attribute("innerText").split()[2]
quantity_sold_list.append(sold_number)
df1 = pd.DataFrame({ 'price': prices_list , 'discount': discount_list , 'review_count': review_count_list , 'quantity_sold': quantity_sold_list} )
df1.to_csv('all_item_chamsocnhacua.csv', index=True)
