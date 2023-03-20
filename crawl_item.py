import numpy as np
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import itertools

df_link = pd.read_csv('product_link_giaydep2.csv')
p_link = df_link['link_item'].to_list()
a = p_link[0]
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome("C:\\Games\\chromedriver.exe" , options=chrome_options)
driver.get(a)
sleep(random.randint(1,3))

prices = driver.find_elements(By.CLASS_NAME , "product-price__current-price")
prices_list = [price.text for price in prices]

df1 = pd.DataFrame({ 'price': prices_list} )
df1.to_csv('all_item_giaydep2.csv', index=True)

