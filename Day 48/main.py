'''
selenium is much better to BeautifulSoup, because it can work effectively not just by html
but in React, Angular, JavaScript

'''

from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to website
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1?adgrpid=137939573890&dib=eyJ2IjoiMSJ9.wTCF6gMg7SkL5z4yCuOudViup8kIDYZcn0ztYcs4jzgSkqkIlLUuqVbz_cAhnMlxKqDtznRjaDAnNkrvYRVwnJ1Vkr_TcR6q2Rkgw7lCtYI1nkVa-r25N_vrt3v6BnNdCf_JaBbJ5y50NaxvxbFu_EBiZEqdcIjoRwgqB9OSl7rrIzVQjyeTxw8dslfcQJLH_cKiiFmEZTgX3KPY07UKn9qL_yQrd7Cw6nUQSH3JeD8.k8IxE84VEuZu33gQXEo_irg5GQK0L_UE2IJ2Ik9I2IA&dib_tag=se&hvadid=630081763194&hvdev=c&hvlocphy=9067168&hvnetw=g&hvqmt=b&hvrand=9779465072002330516&hvtargid=kwd-360190606036&hydadcr=20904_13407875&keywords=instant%2Bpot%2Bmulticooker&mcid=beb5be9523c3354fb227ac9e8ebcd81b&qid=1756585217&sr=8-1&th=1")
driver.get("https://www.python.org/")

# price_tag = driver.find_element(By.CLASS_NAME, value="olpWrapper")
# print(price_tag.text)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

#By.CSS_SELECTOR
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

#By.XPath
#bug_link = driver.find_element(By.XPATH, value='//*[@id="_price"]/span')
#print(bug_link.text)
'''
note: find_element is different from find_elements
'''
#Finding multiple elements
# tier_1 = driver.find_element(By.CSS_SELECTOR, value=".tier_1 a")

#Challenge: Print the event dates from python.org
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
#

# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
# print(events)


#driver.close() #close tab
#close crome browser
driver.quit()