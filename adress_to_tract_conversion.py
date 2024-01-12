from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver_path = r'C:\Users\vishw\Downloads\chromedriver_win32 (1)\chromedriver.exe'
from selenium.webdriver.chrome.service import Service

service_gecko = Service(executable_path=r'C:\Users\vishw\Downloads\chromedriver_win32 (1)\chromedriver.exe')

driver = webdriver.Chrome(service=service_gecko)


# Navigate to the web page to scrape
driver.get('https://geomap.ffiec.gov/ffiecgeomap/')
from time import sleep

import csv
with open(r'C:\Users\vishw\OneDrive\Desktop\scrape_crime_sample_pds.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    # Extract the column of data you want to copy
    data_to_copy = [row[15] for row in reader]

tract_list=[]
counter=0


data_to_copy=data_to_copy[600:900]
print(data_to_copy)



for a in data_to_copy:

    driver.get('https://geomap.ffiec.gov/ffiecgeomap/')
    WebDriverWait(driver, timeout=45).until(lambda d: d.find_element(By.CSS_SELECTOR,'input#searchDiv-input'))
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#searchDiv-input')))
    search_box.send_keys(a)
    search_box.send_keys(Keys.RETURN) 
    sleep(5)
    tract = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#TractCode')))
    tract_list.append(tract.text)
    search_box.send_keys(Keys.BACKSPACE * 100)
    

import pandas as pd 
print(tract_list)
df=pd.DataFrame()  

df['tract_Code']=tract_list
print(df)

df.to_csv(r"C:\Users\vishw\OneDrive\Desktop\Tract.csv",sep=',',index=None)