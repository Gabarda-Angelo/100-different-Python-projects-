'''
MY NOTES:
BE CAREFUL! YOU MIGHT USE THE INSTAGRAM ACCOUNT THAT HAS ALREADY FOLLOWERS
AND FOLLOWING AND HAVE SOME PHOTOS TO AVOID INSTAGRAM LABELING YOU AS A BOT!

'''

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

SIMILAR_ACCOUNT = "https://www.instagram.com/artificialintelligencenews.in/"
USERNAME ="gelo.gabarda@gmail.com"
PASSWORD ="15Minuterule"
INSTAGRAM_URL="https://www.instagram.com/accounts/login/"


class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        wait = WebDriverWait(self.driver, 60)

        time.sleep(2)
        # Wait for the email input field to be visible and interactable
        email_input_field = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')))

        # Clear any existing text (optional, but recommended)
        email_input_field.clear()

        # putting text in input field
        email_input_field.send_keys(USERNAME)

        time.sleep(2)
        # Wait for the password input field to be visible and interactable
        password_input_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')))

        # Clear any existing text (optional, but recommended)
        password_input_field.clear()

        # putting text in input field
        password_input_field.send_keys(PASSWORD)
        time.sleep(2)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button')))
        login_button.click()
    def find_followers(self):
        #use sleep to not appear you are a bot, because it will detected by IG so you will need to login again,
        #and also depends on your internet speed, mine I delay for 10s because I have low bandwidth internet
        time.sleep(10)
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(5)

        wait = WebDriverWait(self.driver, 60)

        # Locate followers button using partial matching instead of full path
        '''
            # Locate the "Followers" button on the Instagram profile page.
            # We use a relative XPath with 'contains(@href, "/followers")' instead of an absolute path(THE ONE WITH TOO LONG ELEMENTS)
            # because Instagram's DOM structure changes frequently, and dynamic IDs can break absolute XPaths.
            # This approach finds any <a> tag whose 'href' attribute contains '/followers', making it more reliable.
            # Once the button is located and clickable, we click it to open the followers list.
        '''
        followers_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/followers')]")
        ))
        followers_button.click()
        time.sleep(3)

        # Wait for the followers modal to load completely
        modal = wait.until(EC.presence_of_element_located((
            By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        )))

        # Scroll inside the followers modal to load more users
        for _ in range(20):  # Adjust the range based on how many followers you want to load
            #means: “Scroll this modal down to the very bottom of its content.”
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1.5)  # Allow new followers to load


    def follow(self):


        all_buttons = self.driver.find_elements(By.XPATH, "//button[.//div[text()='Follow']]")
        time.sleep(5)
        for button in all_buttons:
            try:
                button.click()
                time.sleep(5)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                print("something wrong")
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
