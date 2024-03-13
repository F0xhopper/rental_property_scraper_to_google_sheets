from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, 'html.parser')
prices_elements = soup.select(".PropertyCardWrapper__StyledPriceLine")
link_elements = soup.find_all('a',class_='StyledPropertyCardDataArea-anchor')
addres_elements = soup.select('a address')
prices = [price.getText().split('+')[0].split('/')[0] for price in prices_elements]
links = [link['href'] for link in link_elements]
addresss = [address.getText().replace(' |',',').strip() for address in addres_elements]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(prices)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScZoDy-MtwJIJiHxFFowBo4tymSNQKu-_6JjUfOAQ7eoD89_Q/viewform?usp=sf_link")
    time.sleep(2)
    inputs = driver.find_elements(by=By.CSS_SELECTOR, value=".Xb9hP input")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".uArJ5e")
    inputs[0].send_keys(addresss[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(links[i])
    submit_button.click()
    
    

