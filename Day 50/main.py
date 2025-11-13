from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from time import sleep


# --------------------------------
# STEP 1 — Configure Chrome Profile
# --------------------------------
'''
how to automatically loged in to FB?
steps:
1.)I added the SeleniumProfile folder to my Chrome User Data; you can locate it at that path.
2.)Run this script.
3.)If it navigates to Tinder.com, then manually log in with your FB account.
4.)Now, every time you run this script, it will automatically log in to your Tinder via FB because you have already logged in before, using the User Data in the SeleniumProfile folder.
5.)Don't forget to close Chrome before running your code.

'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"--user-data-dir=C:\Users\Angelo\AppData\Local\Google\Chrome\User Data\SeleniumProfile")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
wait = WebDriverWait(driver, 15)


try:
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')))
    print("Logged in successfully using saved Facebook session!")
except TimeoutException:
    print(" Session expired. Please log in manually.")
    sleep(760)
    driver.quit()
    exit()

# Swiping

'''
Now the challenging parts here is geting the correct XPATH from the Tinder website
maybe in the future they update the codes and couldn't locate the exact path.

-some of the browser will not give you correct XPATH so try different browser.
in my case my chrome didnt give me the correct XPATH,which I consume alot of time to figure it out.

I tried CCleaner browser and get tinder's XPATH and yeah it give's me the correct XPATH (E.G @id="main-content) 
and not the Dynamic one (E.G  [@id="c-970930519"])
'''

left_swipe = driver.find_element(By.XPATH, value='//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/button')
for i in range(100):#Tinder limit the unsubsribe people 100 likes only a day
    try:
        right_swipe = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')))
        right_swipe.click()
        print("Liked successful!")
    except ElementClickInterceptedException:
        '''
        -Selenium bot sometimes fails is because Tinder’s DOM is highly dynamic.
        -Tinder’s web app is built using ReactJS, which means the entire page isn’t static HTML
        so we need to locate where is it when it change the location, now I found it here this path
        '''
        right_swipe_version_two = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c-970930519"]/div/div[1]/div/div/div/main/div/div/div/div/div[5]/div/div[4]')))
        right_swipe_version_two.click()


driver.quit()
