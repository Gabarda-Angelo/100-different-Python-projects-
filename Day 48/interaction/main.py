from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to Wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

#Navigate to sign - up challenge web
driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(article_count.text)

#Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Find the "Search" <input> by Name
# search = driver.find_element(By.NAME, value="search")
#
# #Sending keyboard input to Selenium
# search.send_keys("Python",Keys.ENTER)

#Find the fields
firstname_text_input = driver.find_element(By.NAME, value="fName")
lastname_text_input = driver.find_element(By.NAME, value="lName")
email_text_input = driver.find_element(By.NAME, value="email")

#Fill out the form
firstname_text_input.send_keys("Angelo")
lastname_text_input.send_keys("Gabarda")
email_text_input.send_keys("gelo.gabarda@gmail.com")


#Locate sign-up and click on it
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()







