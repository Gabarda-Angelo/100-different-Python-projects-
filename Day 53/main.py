'''
When to use BS4? --> if the website is static(e.g html, xml not changing)
When to use selenium? --> if the website is dynamic(e.g javascript, react, changing..)

who is strongest and flexible ? ---> selenium
who is efficient and fast? ----? BS4
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

GOOGLE_SHEET_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdr3R0qMQk_9otzJUSm5ke1T1693X7EcY_xysv2yZFEs42GyA/viewform?usp=header"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
          "Accept-Language": "en-US,en;q=0.9",
          }

URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(URL,headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")


# Part 1 - Scrape the links, addresses, and prices of the rental properties using BS4

#scrape all links
scraped_links = soup.find_all(name="a", class_="property-card-link")
all_rental_links = [link.get("href") for link in scraped_links]

# print(f"There are {len(all_rental_links)} links to individual listings in total: \n")
# print(all_rental_links)

#scrape all addresses
scraped_address = soup.find_all(name="address")
all_rental_address =  [address.get_text().strip().replace("|","") for address in scraped_address]


#scrape all price
scraped_price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
all_rental_price = [price.get_text().replace("/mo","").split("+")[0] for price in scraped_price]



#part 2 using selenium , automatically putting all of the data into google sheet , thatwe scrape from the website

# Optional - Keep browser open (helps diagnose issues during a crash)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(driver, 60)

for i in range(len(all_rental_links)):
    driver.get(GOOGLE_SHEET_URL)
    time.sleep(2)
#adress input field
    # Wait for the address input field to be visible and interactable
    address_input_field = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    # Clear any existing text (optional, but recommended)
    address_input_field.clear()

    # putting text in input field
    address_input_field.send_keys(all_rental_address[i])

#price input field
# Wait for the price input field to be visible and interactable
    price_input_field = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    # Clear any existing text (optional, but recommended)
    price_input_field.clear()

    # putting text in input field
    price_input_field.send_keys(all_rental_price[i])

#link input field
# Wait for the link input field to be visible and interactable
    link_input_field = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    # Clear any existing text (optional, but recommended)
    link_input_field.clear()

    # putting text in input field
    link_input_field.send_keys(all_rental_links[i])

    time.sleep(1)
#submit button
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
    submit_button.click()
